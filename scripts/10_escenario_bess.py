#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
San Juan Energy Gap — Script 10
Escenario solar + BESS: ¿y si ponen baterías?
===============================================
Caso de estudio: Los Azules, 119 MW continuos 24/7.

Objetivo:
  Calcular cuántos MW solares y MWh de baterías se necesitan para
  abastecer Los Azules (119 MW firmes 24/7) con solar + BESS.

  La clave es que el BESS debe almacenar la energía para las horas
  nocturnas (13,5 h), y el solar debe cubrir tanto la demanda diurna
  directa como la carga del BESS.

=== DATOS vs. SUPUESTOS ===

  DATO: DEMANDA_MINA_MW = 119 MW
    Demanda eléctrica Los Azules (McEwen Copper, NI 43-101, nov. 2025 — Tier 1).

  DATO: ENERGIA_SOLAR_MWH = 1.372.040 MWh
    Generación solar San Juan en 2024 (portal EPSE/CAMMESA, dic. 2024 — Tier 1).

  DATO: CAPACIDAD_SOLAR_MW = 603 MW
    Capacidad solar instalada San Juan al 31/12/2024 (EPSE feb. 2025 — Tier 1).
    Nota: este FC asume los 603 MW instalados durante todo 2024. Si hubo altas
    de capacidad a lo largo del año, el valor real difiere levemente.

  DATO: HORAS_AÑO = 8.760
    Horas en un año (365 × 24).

  SUPUESTO: HORAS_NOCTURNAS = 13,5 h/día (promedio anual)
    Latitud ~31,5° S (San Juan). Parámetro real de astronomía — NO se usa
    FC × 24h (ese sería un error conceptual: el FC es equivalencia energética,
    no duración del día).

  SUPUESTO: EFF_BESS = 87%
    Eficiencia round-trip litio-ión, estándar industria.
    Degradación ignorada (supuesto conservador del modelo — Tier 3).

  DATO: COSTO_BESS_MIN = 280 USD/kWh
  DATO: COSTO_BESS_MAX = 320 USD/kWh
    Mercado 2024–2025 (Tier 3 — rango estimado).

  DATO (directo): MW_SOLAR_LOS_AZULES = 497 MW para FC 26,0%
    La guía v3.1 establece 497 MW para FC 26,0%. Este valor se obtiene
    usando el FC exacto sin redondear (0,25974...) en la fórmula de balance,
    y redondeando el resultado al entero más cercano. Ver cálculo explícito abajo.

Balance energético diario:
  Energía total mina = 119 MW × 24 h = 2.856 MWh/día
  Horas diurnas = 24 − 13,5 = 10,5 h
  Demanda diurna directa = 119 MW × 10,5 h = 1.249,5 MWh
  Carga BESS = 119 MW × 13,5 h ÷ 0,87 = 1.846,6 MWh
  Solar debe producir = 1.249,5 + 1.846,6 = 3.096,1 MWh/día
  MW solar = (solar_daily_MWh/día) ÷ (FC × 24 h)
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import datetime

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
REPORTS_DIR = os.path.join(REPO_ROOT, 'reports')
os.makedirs(REPORTS_DIR, exist_ok=True)

# ── Estilo ────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family':       'DejaVu Sans',
    'font.size':         11,
    'axes.titlesize':    12,
    'axes.titleweight':  'bold',
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'figure.dpi':        150,
})

print("=" * 70)
print("SCRIPT 10 — ESCENARIO SOLAR + BESS (caso Los Azules)")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 70)

# ── Parámetros ────────────────────────────────────────────────────────────────
# DATO: Los Azules — McEwen Copper NI 43-101, nov. 2025
DEMANDA_MINA_MW    = 119.0

# DATO: generación + capacidad solar San Juan (EPSE/CAMMESA dic. 2024)
ENERGIA_SOLAR_MWH  = 1_372_040.0   # DATO: generación solar SJ 2024 (EPSE/CAMMESA)
CAPACIDAD_SOLAR_MW = 603.0          # DATO: capacidad solar instalada SJ (EPSE feb. 2025)
HORAS_AÑO          = 8_760.0        # 365 × 24

# SUPUESTO: astronomía latitud ~31,5° S
HORAS_NOCTURNAS    = 13.5           # SUPUESTO: promedio anual, latitud ~31,5° S
HORAS_DIURNAS      = 24.0 - HORAS_NOCTURNAS  # 10.5 h

# SUPUESTO: eficiencia BESS
EFF_BESS           = 0.87           # SUPUESTO: round-trip litio-ión, estándar industria

# DATO: rango de costo BESS (mercado 2024–2025 — Tier 3)
COSTO_MIN_USD_KWH  = 280.0
COSTO_MAX_USD_KWH  = 320.0

# ── Cálculos centrales ────────────────────────────────────────────────────────

# 1. Factor de capacidad solar real San Juan
FC_SOLAR = ENERGIA_SOLAR_MWH / (CAPACIDAD_SOLAR_MW * HORAS_AÑO)
FC_PCT   = FC_SOLAR * 100

# 2. Balance energético diario (Los Azules)
energia_total_dia  = DEMANDA_MINA_MW * 24.0             # MWh/día
demanda_diurna     = DEMANDA_MINA_MW * HORAS_DIURNAS    # MWh
carga_bess_bruta   = DEMANDA_MINA_MW * HORAS_NOCTURNAS  # MWh (energía a descargar)
carga_bess_entrada = carga_bess_bruta / EFF_BESS         # MWh que el solar debe inyectar
solar_debe_producir = demanda_diurna + carga_bess_entrada

# 3. BESS: capacidad de descarga (fija, independiente del FC)
#    = 119 MW × 13,5 h  (exacto: 1606.5 MWh)
bess_mwh = DEMANDA_MINA_MW * HORAS_NOCTURNAS

# 4. MW solar necesarios según FC
def mw_solar(fc):
    """MW solares necesarios para cubrir solar_debe_producir dado el FC."""
    return solar_debe_producir / (fc * 24.0)

MW_SOLAR_REAL = mw_solar(FC_SOLAR)  # usando FC exacto sin redondear

# Tabla sensibilidad FC
FC_TABLA = [0.22, 0.25, FC_SOLAR, 0.30]

# 5. Costo BESS
costo_min_musd = bess_mwh * COSTO_MIN_USD_KWH / 1_000  # USD M (bess en MWh, costo en USD/kWh)
costo_max_musd = bess_mwh * COSTO_MAX_USD_KWH / 1_000

# ── Output textual ────────────────────────────────────────────────────────────
print()
print("ADVERTENCIA DE CALIDAD DE DATOS")
print("-" * 70)
print(f"  DATO     : Energía solar SJ 2024 = {ENERGIA_SOLAR_MWH:,.0f} MWh (EPSE/CAMMESA dic. 2024)")
print(f"  DATO     : Capacidad solar SJ    = {CAPACIDAD_SOLAR_MW:.0f} MW (EPSE feb. 2025)")
print(f"  DATO     : Demanda Los Azules    = {DEMANDA_MINA_MW:.0f} MW (McEwen NI 43-101, nov. 2025)")
print(f"  SUPUESTO : Horas nocturnas       = {HORAS_NOCTURNAS} h/día (latitud ~31,5° S, promedio anual)")
print(f"  SUPUESTO : Eficiencia BESS       = {EFF_BESS*100:.0f}% round-trip (litio-ión, estándar)")
print(f"  DATO     : Costo BESS            = USD {COSTO_MIN_USD_KWH:.0f}–{COSTO_MAX_USD_KWH:.0f}/kWh (mercado 2024–2025, Tier 3)")
print("-" * 70)
print()

print("--- FC SOLAR REAL SAN JUAN ---")
print(f"  Fórmula: {ENERGIA_SOLAR_MWH:,.0f} MWh ÷ ({CAPACIDAD_SOLAR_MW:.0f} MW × {HORAS_AÑO:.0f} h)")
print(f"  FC solar = {FC_SOLAR:.6f}")
print(f"  FC solar = {FC_PCT:.1f}%")
print()

print("--- BALANCE ENERGÉTICO DIARIO (Los Azules, 119 MW firmes 24/7) ---")
print(f"  Energía total mina/día     : {DEMANDA_MINA_MW:.0f} MW × 24 h = {energia_total_dia:,.1f} MWh")
print(f"  Horas diurnas              : {HORAS_DIURNAS} h  |  Horas nocturnas: {HORAS_NOCTURNAS} h")
print(f"  Demanda diurna directa     : {DEMANDA_MINA_MW:.0f} MW × {HORAS_DIURNAS} h = {demanda_diurna:,.1f} MWh")
print(f"  Carga BESS (entrada)       : {DEMANDA_MINA_MW:.0f} MW × {HORAS_NOCTURNAS} h ÷ {EFF_BESS} = {carga_bess_entrada:,.1f} MWh")
print(f"  Solar debe producir/día    : {demanda_diurna:,.1f} + {carga_bess_entrada:,.1f} = {solar_debe_producir:,.1f} MWh")
print()

print("--- BESS CAPACIDAD ---")
print(f"  BESS capacidad: {bess_mwh:.1f} MWh (= {DEMANDA_MINA_MW:.0f} × {HORAS_NOCTURNAS})")
print(f"  Nota: 1.606,5 MWh es el valor exacto. La guía lo redondea a 1.607 MWh en la tabla.")
print()

print("--- TABLA: MW SOLAR NECESARIOS POR FC ---")
print(f"  {'FC solar':>12}  {'MW solar':>10}  {'BESS (MWh)':>12}")
print("  " + "-" * 38)
for fc_val in FC_TABLA:
    mw = mw_solar(fc_val)
    label = " <- FC real CAMMESA 2024" if abs(fc_val - FC_SOLAR) < 1e-6 else ""
    print(f"  {fc_val*100:>10.1f}%  {mw:>10.0f}  {bess_mwh:>12.1f}{label}")
print()

print("--- RESULTADOS CLAVE (FC 26,0% real CAMMESA) ---")
print(f"  FC solar real San Juan       : {FC_PCT:.1f}%  "
      f"(= {ENERGIA_SOLAR_MWH:,.0f} MWh ÷ ({CAPACIDAD_SOLAR_MW:.0f} × {HORAS_AÑO:.0f}))")
print(f"  BESS Los Azules solar        : {round(MW_SOLAR_REAL):.0f} MW solar")
print(f"  BESS capacidad: {bess_mwh:.1f} MWh (= {DEMANDA_MINA_MW:.0f} × {HORAS_NOCTURNAS})")
print(f"  Costo BESS estimado          : USD {costo_min_musd:.0f}–{costo_max_musd:.0f} M")
print(f"    ({COSTO_MIN_USD_KWH:.0f}–{COSTO_MAX_USD_KWH:.0f} USD/kWh × {bess_mwh:.1f} MWh × 1.000 kWh/MWh)")
print()
print("=" * 70)

# ── Gráfico ───────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# Panel izquierdo: MW solar vs FC
ax1 = axes[0]
fc_range = np.linspace(0.18, 0.35, 200)
mw_range = [mw_solar(fc) for fc in fc_range]

ax1.plot(fc_range * 100, mw_range, color='#E67E22', lw=2.5)
ax1.axvline(FC_PCT, color='#C0392B', lw=1.5, linestyle='--',
            label=f'FC real CAMMESA 2024: {FC_PCT:.1f}%')
ax1.axhline(round(MW_SOLAR_REAL), color='#C0392B', lw=1.0, linestyle=':')
ax1.scatter([FC_PCT], [round(MW_SOLAR_REAL)],
            color='#C0392B', s=80, zorder=5)
ax1.annotate(f'{round(MW_SOLAR_REAL):.0f} MW solar\n(FC {FC_PCT:.1f}%)',
             xy=(FC_PCT, round(MW_SOLAR_REAL)),
             xytext=(FC_PCT + 2, round(MW_SOLAR_REAL) + 40),
             fontsize=9, color='#C0392B', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.2))

# Puntos de la tabla
fc_puntos = [0.22, 0.25, 0.30]
for fc_pt in fc_puntos:
    mw_pt = mw_solar(fc_pt)
    ax1.scatter([fc_pt * 100], [mw_pt], color='#2980B9', s=50, zorder=4)
    ax1.text(fc_pt * 100 + 0.4, mw_pt + 5, f'{mw_pt:.0f}',
             fontsize=8, color='#2980B9')

ax1.set_xlabel('Factor de capacidad solar (%)')
ax1.set_ylabel('MW solar necesarios')
ax1.set_title(f'MW solar vs. FC\n(Los Azules: {DEMANDA_MINA_MW:.0f} MW firmes 24/7)')
ax1.legend(fontsize=8.5)
ax1.set_xlim(18, 35)

# Panel derecho: diagrama de balance energético diario
ax2 = axes[1]
categorias = [
    'Demanda\ndiurna directa\n(solar → mina)',
    'Carga BESS\n(solar → batería)',
    'Descarga BESS\n(batería → mina)',
    'Energía total\nmina/día'
]
valores = [demanda_diurna, carga_bess_entrada, carga_bess_bruta, energia_total_dia]
colores = ['#F39C12', '#E74C3C', '#2980B9', '#27AE60']

barras = ax2.bar(categorias, valores, color=colores, width=0.55,
                 edgecolor='white', linewidth=1.5, alpha=0.88)
for barra, val in zip(barras, valores):
    ax2.text(barra.get_x() + barra.get_width() / 2,
             barra.get_height() + 20,
             f'{val:,.1f} MWh',
             ha='center', va='bottom', fontsize=9, fontweight='bold')

ax2.set_ylabel('MWh/día')
ax2.set_title(f'Balance energético diario\n(BESS = {bess_mwh:.1f} MWh — fijo, independiente del FC)')
ax2.set_ylim(0, max(valores) * 1.20)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

nota2 = (
    f'DATO: Los Azules = {DEMANDA_MINA_MW:.0f} MW (McEwen NI 43-101, nov. 2025). '
    f'FC real: {ENERGIA_SOLAR_MWH:,.0f} MWh ÷ ({CAPACIDAD_SOLAR_MW:.0f} MW × 8.760 h) = {FC_PCT:.1f}% (EPSE/CAMMESA dic. 2024). '
    f'SUPUESTOS: {HORAS_NOCTURNAS} h nocturnas (lat. ~31,5° S), EFF BESS {EFF_BESS*100:.0f}% (estándar industria). '
    f'Costo BESS USD {COSTO_MIN_USD_KWH:.0f}–{COSTO_MAX_USD_KWH:.0f}/kWh (Tier 3, mercado 2024–2025).'
)
fig.text(0.5, -0.02, nota2, ha='center', va='top',
         fontsize=7.2, color='#566573', style='italic',
         wrap=True)

fig.suptitle(
    f'San Juan — Escenario solar + BESS para Los Azules ({DEMANDA_MINA_MW:.0f} MW firmes 24/7)\n'
    f'Con FC real CAMMESA {FC_PCT:.1f}%: {round(MW_SOLAR_REAL):.0f} MW solar + {bess_mwh:.1f} MWh BESS',
    fontsize=11, fontweight='bold', y=1.01
)

plt.tight_layout()
ruta_png = os.path.join(REPORTS_DIR, '10_01_escenario_bess.png')
fig.savefig(ruta_png, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"Figura guardada: {ruta_png}")
print("=" * 70)
