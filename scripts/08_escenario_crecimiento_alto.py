#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
San Juan Energy Gap — Script 08
Proyección provincial: CAGR base 2% vs. boom 3,75%
====================================================
Objetivo:
  Comparar la proyección de demanda eléctrica provincial de San Juan
  bajo dos escenarios de crecimiento, para cuantificar el rango de
  la brecha de generación firme nocturna (ver script 09).

  El CAGR provincial NO afecta la brecha de transporte minero de 2030
  (esa brecha es fija: Josemaría + Los Azules - plan aprobado = 119 MW).
  Lo que sí varía con el CAGR es la demanda nocturna total.

Fórmula:
  demanda(año) = BASE_MW × (1 + CAGR) ^ (año − BASE_AÑO)

=== DATOS vs. SUPUESTOS ===

  DATO: BASE_MW = 551 MW
    Demanda pico provincial 2021 (EPRE San Juan, Anuario 2021). Sin CSV en repo.

  SUPUESTO: CAGR_BASE = 2,0%/año
    Piso conservador; refleja crecimiento histórico de San Juan sin minería.
    No hay serie horaria EPRE disponible para derivarlo del CSV.

  SUPUESTO: CAGR_BOOM = 3,75%/año
    Escenario boom; captura efecto indirecto de 25.000–35.000 empleos directos
    + 3–5x empleos indirectos sobre la demanda no-minera. Parámetro del modelo.

  DATO: BASE_AÑO = 2021
    Año del dato EPRE (fuente de BASE_MW).
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
REPORTS_DIR = os.path.join(REPO_ROOT, 'reports')
os.makedirs(REPORTS_DIR, exist_ok=True)

# ── Estilo (consistente con script 07) ───────────────────────────────────────
plt.rcParams.update({
    'font.family':       'DejaVu Sans',
    'font.size':         11,
    'axes.titlesize':    13,
    'axes.titleweight':  'bold',
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'figure.dpi':        150,
})

print("=" * 70)
print("SCRIPT 08 — PROYECCIÓN PROVINCIAL: CAGR 2% vs. 3,75%")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 70)

# ── Parámetros ────────────────────────────────────────────────────────────────
BASE_AÑO = 2021
BASE_MW  = 551.0    # DATO: demanda pico provincial 2021 (EPRE San Juan, Anuario 2021)
CAGR_BASE = 0.020   # SUPUESTO: piso conservador (crecimiento histórico sin minería)
CAGR_BOOM = 0.0375  # SUPUESTO: escenario boom (efecto indirecto del boom minero)

AÑOS_TABLA = [2025, 2028, 2030, 2032, 2035, 2036, 2040]
AÑOS_PLOT  = np.arange(2021, 2041)

# ── Función de proyección ─────────────────────────────────────────────────────
def proyeccion(años, base_mw, base_año, cagr):
    """
    Proyecta demanda con crecimiento compuesto anual.
    Fórmula: base × (1 + cagr)^(año - base_año)
    """
    return np.array([base_mw * (1 + cagr) ** (a - base_año) for a in años])

# ── Calcular series ───────────────────────────────────────────────────────────
valores_tabla_2  = proyeccion(AÑOS_TABLA, BASE_MW, BASE_AÑO, CAGR_BASE)
valores_tabla_375 = proyeccion(AÑOS_TABLA, BASE_MW, BASE_AÑO, CAGR_BOOM)
serie_2          = proyeccion(AÑOS_PLOT, BASE_MW, BASE_AÑO, CAGR_BASE)
serie_375        = proyeccion(AÑOS_PLOT, BASE_MW, BASE_AÑO, CAGR_BOOM)

# ── Output textual ────────────────────────────────────────────────────────────
print()
print("ADVERTENCIA DE CALIDAD DE DATOS")
print("-" * 70)
print(f"  DATO     : BASE_MW = {BASE_MW:.0f} MW — EPRE San Juan, Anuario 2021. Sin CSV en repo.")
print(f"  SUPUESTO : CAGR_BASE = {CAGR_BASE*100:.1f}%/año — piso conservador (histórico sin minería)")
print(f"  SUPUESTO : CAGR_BOOM = {CAGR_BOOM*100:.2f}%/año — escenario boom (efecto indirecto)")
print(f"  DATO     : BASE_AÑO = {BASE_AÑO} — año del dato EPRE")
print("-" * 70)
print()

print(f"Fórmula: {BASE_MW} × (1 + CAGR) ^ (año − {BASE_AÑO})")
print()
print(f"{'Año':>6}  {'CAGR 2% (MW)':>14}  {'CAGR 3,75% (MW)':>16}")
print("-" * 42)
for yr, v2, v375 in zip(AÑOS_TABLA, valores_tabla_2, valores_tabla_375):
    print(f"{yr:>6}  {v2:>14.1f}  {v375:>16.1f}")

print()
print("Valores clave para el documento (v3.1):")
key_check = {2030: None, 2036: None, 2040: None}
for yr, v2, v375 in zip(AÑOS_TABLA, valores_tabla_2, valores_tabla_375):
    if yr in key_check:
        print(f"  {yr}: CAGR 2% = {v2:.1f} MW  |  CAGR 3,75% = {v375:.1f} MW")
print()

# ── Gráfico ───────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6.5))

ax.plot(AÑOS_PLOT, serie_2,
        color='#2980B9', lw=2.5, linestyle='-',
        label=f'CAGR 2%/año — escenario base (piso conservador, SUPUESTO)')
ax.plot(AÑOS_PLOT, serie_375,
        color='#C0392B', lw=2.5, linestyle='--',
        label=f'CAGR 3,75%/año — escenario boom (efecto indirecto, SUPUESTO)')

# Banda de incertidumbre
ax.fill_between(AÑOS_PLOT, serie_2, serie_375,
                alpha=0.12, color='#8E44AD',
                label='Rango entre escenarios')

# Punto de partida
ax.scatter([BASE_AÑO], [BASE_MW],
           color='#27AE60', s=80, zorder=5,
           label=f'Base: {BASE_MW:.0f} MW en {BASE_AÑO} (DATO — EPRE Anuario 2021)')

# Anotaciones en años clave
for yr, v2, v375 in zip(AÑOS_TABLA, valores_tabla_2, valores_tabla_375):
    if yr in [2030, 2036, 2040]:
        ax.annotate(f'{v2:.1f}', xy=(yr, v2), xytext=(yr - 0.3, v2 + 15),
                    fontsize=8, color='#2980B9', ha='right', fontweight='bold')
        ax.annotate(f'{v375:.1f}', xy=(yr, v375), xytext=(yr + 0.2, v375 + 15),
                    fontsize=8, color='#C0392B', ha='left', fontweight='bold')

# Línea vertical en 2030
ax.axvline(x=2030, color='#7F8C8D', lw=1, linestyle=':', alpha=0.7)
ax.text(2030.15, BASE_MW + 30, '2030\n(entrada minas)', fontsize=8,
        color='#7F8C8D', va='bottom')

ax.set_xlim(2020.5, 2040.5)
ax.set_ylim(500, max(serie_375) * 1.12)
ax.set_xlabel('Año', fontsize=11)
ax.set_ylabel('Demanda provincial proyectada (MW)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))

ax.set_title(
    f'San Juan — Proyección provincial de demanda eléctrica 2021–2040\n'
    f'Base: {BASE_MW:.0f} MW ({BASE_AÑO}, DATO EPRE) | CAGR base 2% vs. boom 3,75% (SUPUESTOS)',
    fontsize=12, fontweight='bold', pad=14
)

nota = (
    f'DATO: {BASE_MW:.0f} MW en {BASE_AÑO} — EPRE San Juan, Anuario 2021 (Potencia Operada máxima). Sin CSV en repo. '
    f'Ambas tasas CAGR son supuestos del modelo. '
    f'Esta proyección NO afecta la brecha de transporte minero de 2030 (119 MW — fija). '
    f'Sí afecta la brecha de generación firme nocturna (script 09).'
)
ax.text(0.5, -0.10, nota,
        transform=ax.transAxes, ha='center', va='top',
        fontsize=7.5, color='#566573', style='italic',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#FDFEFE',
                  edgecolor='#BDC3C7', alpha=0.9))

ax.legend(loc='upper left', fontsize=9, framealpha=0.92, edgecolor='#BDC3C7')

plt.tight_layout(rect=[0, 0.10, 1, 1])
ruta_png = os.path.join(REPORTS_DIR, '08_01_proyeccion_cagr_alto.png')
plt.savefig(ruta_png, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Figura guardada: {ruta_png}")
print("=" * 70)
