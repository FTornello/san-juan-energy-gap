#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 10 — Escenario solar + BESS para Los Azules (119 MW continuos 24/7).

CORRECCIONES respecto de gen_figures_v3.py:
  1. FC solar real calculado desde datos CAMMESA:
       Generación solar SJ 2024 = 1.372.040 MWh (portal EPSE / CAMMESA, dic 2024)
       Instalado EPSE = 603 MW
       FC_real = 1.372.040 / (603 × 8.760) = 26.0%
  2. Horas nocturnas: ~13,5 h reales (promedio anual San Juan, ~31,5° S lat.)
     NO se usa FC × 24 para la noche — eso es un error conceptual.
  3. Balance energético diario explícito:
       Energía que la solar debe producir por día =
         (demanda diurna directa) + (carga de batería para la noche)
       Con eficiencia round-trip 87%:
         carga_bateria_MWh = (119 MW × hs_noche) / 0.87
         solar_diario_MWh  = 119 × hs_dia + carga_bateria_MWh
         MW_solar = solar_diario_MWh / (FC × 24)
  4. BESS capacity = 119 MW × hs_noche (energía que debe poder descargar).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

REPORTS = "/sessions/sweet-nifty-hopper/mnt/reports"
DARK_BLUE  = "#1a3a5c"
MID_BLUE   = "#2e6da4"
GOLD       = "#c8972a"
RED        = "#c0392b"
GREEN      = "#27ae60"
GREY       = "#7f8c8d"

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.titlecolor': DARK_BLUE,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.facecolor': 'white',
})

# ── Factor de capacidad real (CAMMESA / EPSE) ─────────────────────────────────
ENERGIA_SOLAR_SJ_2024_MWH = 1_372_040.0  # MWh — portal EPSE/CAMMESA, dic. 2024
INSTALADO_EPSE_MW          = 603.0         # MW — EPSE San Juan, feb. 2025
HORAS_ANIO                 = 8_760.0
FC_REAL = ENERGIA_SOLAR_SJ_2024_MWH / (INSTALADO_EPSE_MW * HORAS_ANIO)

print("=" * 70)
print("SCRIPT 10 — Escenario solar + BESS para Los Azules (119 MW continuo)")
print("=" * 70)
print(f"\nFC solar real San Juan (CAMMESA/EPSE 2024):")
print(f"  Energía solar SJ 2024: {ENERGIA_SOLAR_SJ_2024_MWH:,.0f} MWh")
print(f"  Instalado EPSE:         {INSTALADO_EPSE_MW:.0f} MW")
print(f"  FC = {ENERGIA_SOLAR_SJ_2024_MWH:,.0f} / ({INSTALADO_EPSE_MW:.0f} × {HORAS_ANIO:.0f}) "
      f"= {FC_REAL:.4f} = {FC_REAL*100:.1f}%")

# ── Parámetros del caso Los Azules ─────────────────────────────────────────────
DEMANDA_MW     = 119.0      # MW continuos 24/7 (NI 43-101, Tier 1)
HORAS_NOCHE    = 13.5       # h reales promedio sin sol (lat ~31,5° S, promedio anual)
HORAS_DIA      = 24.0 - HORAS_NOCHE   # = 10.5 h
EFF_RT         = 0.87       # eficiencia round-trip batería litio-ión

print(f"\nParámetros del caso:")
print(f"  Demanda mina:   {DEMANDA_MW} MW continuos 24/7")
print(f"  Horas diurnas:  {HORAS_DIA:.1f} h  (promedio anual — lat ~31,5° S)")
print(f"  Horas nocturnas:{HORAS_NOCHE:.1f} h")
print(f"  Eficiencia BESS: {EFF_RT*100:.0f}% round-trip")

# ── Balance energético ─────────────────────────────────────────────────────────
# Energía que la mina consume por día
energia_diaria_total = DEMANDA_MW * 24.0   # MWh

# BESS capacity (energía que debe poder descargar de noche)
bess_descarga_mwh = DEMANDA_MW * HORAS_NOCHE     # MWh descarga bruta
bess_carga_mwh    = bess_descarga_mwh / EFF_RT   # MWh que hay que meter

# Solar diaria = demanda diurna directa + energía para cargar BESS
solar_diario_mwh  = DEMANDA_MW * HORAS_DIA + bess_carga_mwh

print(f"\nBalance energético diario:")
print(f"  Energía total mina/día:      {energia_diaria_total:.1f} MWh")
print(f"  BESS debe descargar (noche): {bess_descarga_mwh:.1f} MWh")
print(f"  BESS debe cargar (carga):    {bess_carga_mwh:.1f} MWh  (÷ {EFF_RT} RT)")
print(f"  Solar debe producir/día:     {solar_diario_mwh:.1f} MWh")

# ── Cálculo para rango de FC ───────────────────────────────────────────────────
# Incluimos FC_REAL calculado de CAMMESA + rango de sensibilidad
fc_range   = np.array([0.22, 0.25, FC_REAL, 0.30])
labels_fc  = [f'{fc*100:.0f}%' if fc != FC_REAL
              else f'{FC_REAL*100:.1f}%\n(CAMMESA real)' for fc in fc_range]

# MW solar necesarios
psh_range      = fc_range * 24.0            # peak sun hours por día
mw_solar_range = solar_diario_mwh / psh_range

# BESS: capacidad = lo que hay que descargar cada noche (fijo, no depende del FC)
bess_mwh_range = np.full_like(fc_range, bess_descarga_mwh)

print(f"\nResultados por factor de capacidad:")
print(f"{'FC (%)':>10}  {'PSH (h/día)':>12}  {'MW solar':>10}  {'BESS (MWh)':>12}")
print("-" * 48)
for fc, psh, mw_s, bess_mwh in zip(fc_range, psh_range, mw_solar_range, bess_mwh_range):
    tag = " ← CAMMESA 2024" if abs(fc - FC_REAL) < 0.001 else ""
    print(f"{fc*100:>9.1f}%  {psh:>12.2f}  {mw_s:>10.1f}  {bess_mwh:>12.1f}{tag}")

print(f"\nValores clave para documento (v3.1):")
idx_real = 2   # FC_REAL position
print(f"  FC real CAMMESA ({FC_REAL*100:.1f}%): "
      f"MW solar = {mw_solar_range[idx_real]:.0f} MW | "
      f"BESS = {bess_descarga_mwh:.0f} MWh")
print(f"  Rango sensibilidad FC 22–30%: "
      f"MW solar = {mw_solar_range[0]:.0f}–{mw_solar_range[-1]:.0f} MW | "
      f"BESS = {bess_descarga_mwh:.0f} MWh (fijo)")
print(f"\n  Verificación: 119 MW × 24h = {energia_diaria_total:.1f} MWh/día (consumo total)")
print(f"  Pérdida en BESS/día = {bess_carga_mwh - bess_descarga_mwh:.1f} MWh "
      f"({(bess_carga_mwh/bess_descarga_mwh - 1)*100:.1f}%)")

# Costo estimado BESS (USD/kWh, rango de mercado 2024-2025)
costo_kWh_bajo = 280
costo_kWh_alto = 320
costo_bess_bajo = bess_descarga_mwh * 1000 * costo_kWh_bajo / 1e6  # M USD
costo_bess_alto = bess_descarga_mwh * 1000 * costo_kWh_alto / 1e6
print(f"\nCosto estimado BESS (Tier 3 — precios de mercado 2024–2025):")
print(f"  Rango: USD {costo_bess_bajo:.0f}–{costo_bess_alto:.0f} M "
      f"(@ USD {costo_kWh_bajo}–{costo_kWh_alto}/kWh)")
print("=" * 70)

# ── Figura ─────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

# ── Panel izquierdo: MW solar por FC ──────────────────────────────────────────
ax1 = axes[0]
colors_bars = [MID_BLUE if abs(fc - FC_REAL) > 0.001 else GREEN for fc in fc_range]
bars1 = ax1.bar(np.arange(len(fc_range)), mw_solar_range, color=colors_bars,
                alpha=0.85, edgecolor='white', lw=0.8)
ax1.axhline(DEMANDA_MW, color=RED, lw=1.5, ls='--', label=f'Demanda mina ({DEMANDA_MW:.0f} MW)')
for i, (bar, mw) in enumerate(zip(bars1, mw_solar_range)):
    ax1.text(bar.get_x()+bar.get_width()/2, mw + 8,
             f'{mw:.0f} MW', ha='center', va='bottom', fontsize=9,
             fontweight='bold', color=DARK_BLUE)
ax1.set_xticks(np.arange(len(fc_range)))
ax1.set_xticklabels(labels_fc, fontsize=8.5)
ax1.set_title(f'MW solar de placa necesarios\npara {DEMANDA_MW:.0f} MW firmes 24/7', pad=8)
ax1.set_ylabel('MW solar instalados')
ax1.set_ylim(0, max(mw_solar_range)*1.25)
ax1.legend(fontsize=8.5, loc='upper right')
ax1.text(0.5, -0.12, 'FC solar (factor de capacidad)',
         ha='center', transform=ax1.transAxes, fontsize=9)
ax1.add_patch(plt.Rectangle((2-0.44, 0), 0.88, max(mw_solar_range)*1.24,
                              fill=False, edgecolor=GREEN, lw=1.5, ls='-',
                              transform=ax1.transAxes + ax1.transData - ax1.transAxes,
                              clip_on=False))

# ── Panel derecho: BESS MWh (fijo) ────────────────────────────────────────────
ax2 = axes[1]
ax2.bar(np.arange(len(fc_range)), bess_mwh_range, color=DARK_BLUE,
        alpha=0.75, edgecolor='white', lw=0.8)
for bar in ax2.patches:
    ax2.text(bar.get_x()+bar.get_width()/2, bess_descarga_mwh + 15,
             f'{bess_descarga_mwh:.0f} MWh', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color=DARK_BLUE)
ax2.set_xticks(np.arange(len(fc_range)))
ax2.set_xticklabels(labels_fc, fontsize=8.5)
ax2.set_title(f'Capacidad BESS necesaria\n(cubre {HORAS_NOCHE:.1f} h nocturnas @ {DEMANDA_MW:.0f} MW)', pad=8)
ax2.set_ylabel('MWh (capacidad de descarga)')
ax2.set_ylim(0, bess_descarga_mwh * 1.4)
ax2.text(0.5, -0.12, 'FC solar (no afecta BESS — constante)',
         ha='center', transform=ax2.transAxes, fontsize=9, color=GREY)

# Nota metodológica dentro de la figura
ax2.text(0.5, 0.55,
         f'BESS = {DEMANDA_MW:.0f} MW × {HORAS_NOCHE:.1f} h\n'
         f'= {bess_descarga_mwh:.0f} MWh\n'
         f'(independiente del FC solar)',
         ha='center', va='center', transform=ax2.transAxes,
         fontsize=9, color=GREY, style='italic',
         bbox=dict(boxstyle='round,pad=0.4', fc='white', ec=GREY, alpha=0.7))

fig.suptitle(
    f'Escenario solar + BESS — Los Azules ({DEMANDA_MW:.0f} MW continuos 24/7)\n'
    f'FC real CAMMESA 2024: {FC_REAL*100:.1f}% | Noche: {HORAS_NOCHE:.1f} h | '
    f'Eficiencia BESS: {EFF_RT*100:.0f}% RT — Tier 3 (estimación)',
    fontsize=10, color=DARK_BLUE, fontweight='bold', y=1.02)
fig.text(0.0, -0.04,
         f'FC real calculado: 1.372.040 MWh ÷ (603 MW × 8.760 h) = {FC_REAL*100:.1f}% '
         f'(EPSE/CAMMESA dic. 2024, pipeline propio). '
         f'Horas nocturnas = 13,5 h (promedio anual San Juan ~31,5° S lat.). '
         f'No se modeló degradación de batería. Tier 3.',
         fontsize=7.5, color=GREY, style='italic')
fig.tight_layout()
fig.savefig(f'{REPORTS}/10_01_escenario_bess.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Figura guardada: {REPORTS}/10_01_escenario_bess.png")
