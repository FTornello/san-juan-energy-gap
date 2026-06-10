#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 08 — Proyección de demanda provincial con dos escenarios de CAGR.
Fuente base: EPRE San Juan, Anuario 2021 → pico provincial = 551 MW en 2021.
CAGR base:   +2,0% / año  (histórico conservador, sin minería)
CAGR boom:   +3,75% / año (mitad del rango 3,5–4%, supuesto del modelo)

PROPÓSITO: Alimenta la sección 6.5 (brecha firme día/noche).
NO compara contra el plan de 260 MW (eso mezclaría categorías conceptuales distintas).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

REPORTS = "/sessions/sweet-nifty-hopper/mnt/reports"
DARK_BLUE  = "#1a3a5c"
MID_BLUE   = "#2e6da4"
GOLD       = "#c8972a"
GREY       = "#7f8c8d"
RED        = "#c0392b"

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.titlecolor': DARK_BLUE,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.facecolor': 'white',
})

# ── Parámetros ────────────────────────────────────────────────────────────────
BASE_YEAR   = 2021        # EPRE San Juan, Anuario 2021
BASE_MW     = 551.0       # MW pico demanda provincial 2021 (Tier 1)
CAGR_BASE   = 0.020       # +2%/año, histórico conservador
CAGR_BOOM   = 0.0375      # +3,75%/año, escenario boom (supuesto modelo)

anios = np.arange(2021, 2041)
dem_base = BASE_MW * (1 + CAGR_BASE) ** (anios - BASE_YEAR)
dem_boom = BASE_MW * (1 + CAGR_BOOM) ** (anios - BASE_YEAR)

# ── Output textual (FUENTE para documento) ───────────────────────────────────
print("=" * 60)
print("SCRIPT 08 — Demanda provincial proyectada (solo provincial)")
print(f"Base: {BASE_MW} MW en {BASE_YEAR} (EPRE Anuario 2021)")
print("=" * 60)
key_years = [2025, 2028, 2030, 2032, 2035, 2036, 2040]
print(f"{'Año':>6}  {'CAGR 2% (MW)':>14}  {'CAGR 3.75% (MW)':>16}")
print("-" * 42)
for yr in key_years:
    idx = yr - 2021
    v2 = dem_base[idx]
    v375 = dem_boom[idx]
    print(f"{yr:>6}  {v2:>14.1f}  {v375:>16.1f}")
print()
print("Valores clave para documento (v3.1):")
print(f"  2030 CAGR 2%:    {dem_base[2030-2021]:.1f} MW")
print(f"  2030 CAGR 3.75%: {dem_boom[2030-2021]:.1f} MW")
print(f"  2036 CAGR 2%:    {dem_base[2036-2021]:.1f} MW")
print(f"  2036 CAGR 3.75%: {dem_boom[2036-2021]:.1f} MW")
print("=" * 60)

# ── Figura ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))

ax.fill_between(anios, dem_base, dem_boom, alpha=0.15, color=MID_BLUE,
                label='Rango de incertidumbre CAGR')
ax.plot(anios, dem_base, color=MID_BLUE, lw=2.2,
        label=f'Demanda provincial — CAGR base {CAGR_BASE*100:.1f}%/año')
ax.plot(anios, dem_boom, color=DARK_BLUE, lw=2.2, ls='--',
        label=f'Demanda provincial — CAGR boom {CAGR_BOOM*100:.2f}%/año (sup. modelo)')

# Marcar 2030 y 2036
for yr, label in [(2030, 'Josemaría\n+ Los Azules\nentra en prod.'),
                  (2036, 'El Pachón\n(estimado)')]:
    ax.axvline(yr, color=GREY, lw=0.8, ls=':')
    ax.text(yr + 0.2, ax.get_ylim()[0] + 20, label, fontsize=7.5, color=GREY,
            va='bottom')

# Etiquetas en 2030
v2030_base = dem_base[2030-2021]
v2030_boom = dem_boom[2030-2021]
ax.annotate(f'{v2030_base:.0f} MW', xy=(2030, v2030_base),
            xytext=(2031, v2030_base - 20), fontsize=9, color=MID_BLUE,
            arrowprops=dict(arrowstyle='->', color=MID_BLUE, lw=0.8))
ax.annotate(f'{v2030_boom:.0f} MW', xy=(2030, v2030_boom),
            xytext=(2031, v2030_boom + 15), fontsize=9, color=DARK_BLUE,
            arrowprops=dict(arrowstyle='->', color=DARK_BLUE, lw=0.8))

ax.set_title(
    'Proyección de demanda eléctrica PROVINCIAL 2021–2040\n'
    'Escenario base (CAGR 2%) vs. escenario boom (CAGR 3,75% — supuesto)',
    pad=10)
ax.set_xlabel('Año')
ax.set_ylabel('MW (demanda provincial)')
ax.set_xlim(2021, 2040)
ax.legend(fontsize=9, loc='upper left')
ax.text(0.0, -0.11,
        'Base: 551 MW (pico 2021, EPRE San Juan Anuario 2021). '
        'Esta proyección alimenta la brecha firme día/noche (secc. 6.5). '
        'No incluye demanda minera.',
        transform=ax.transAxes, fontsize=7.5, color=GREY, style='italic')
fig.tight_layout()
fig.savefig(f'{REPORTS}/08_01_proyeccion_cagr_alto.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Figura guardada: {REPORTS}/08_01_proyeccion_cagr_alto.png")
