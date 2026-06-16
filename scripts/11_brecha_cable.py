#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 11 — Figura central del eje TRANSPORTE: "El cable que falta".

Compara, para 2030:
  - la demanda minera firme (Josemaría 260 MW + Los Azules 119 MW = 379 MW), y
  - la capacidad de transporte con plan APROBADO (260 MW, solo Josemaría — ENRE).

La brecha de 119 MW = demanda minera firme sin cable aprobado. Es el número central
del relato v2. El 1.500+ MW aparece sólo como horizonte temporal (Tier 2/3), nunca
como la cifra que prueba la tesis.

REGLA DE ORO: el total de demanda minera 2030 (379 MW) NO se calcula a mano aquí.
Se obtiene del output del script 09 (función minera(2030)), cargado como módulo.
Una aserción garantiza que la descomposición 260 + 119 coincide con ese output.

Números canónicos (entradas Tier 1, documentadas):
  - Josemaría 260 MW — ENRE Res. 79/2026.
  - Los Azules 119 MW — NI 43-101 (nov. 2025).
  - Clúster total 1.500+ MW — CEO Glencore Argentina (mayo 2026, Tier 2).
"""
import os
import importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
REPORTS    = os.path.join(REPO_ROOT, 'reports')
os.makedirs(REPORTS, exist_ok=True)

# ── Cargar el script 09 como módulo y tomar el 379 de SU output ─────────────────
_spec = importlib.util.spec_from_file_location(
    'script09', os.path.join(SCRIPT_DIR, '09_brecha_firme_dia_noche.py'))
script09 = importlib.util.module_from_spec(_spec)
print(">>> Ejecutando script 09 para obtener su output (demanda minera 2030)...\n")
_spec.loader.exec_module(script09)

DEMANDA_MINERA_2030 = script09.minera(2030)   # 379.0 — viene del script 09

# Descomposición (entradas Tier 1 documentadas); aserción de consistencia con script 09
JOSEMARIA = 260.0   # ENRE Res. 79/2026 (Fase 1)
LOS_AZULES = 119.0  # NI 43-101, nov. 2025
assert abs((JOSEMARIA + LOS_AZULES) - DEMANDA_MINERA_2030) < 1e-6, (
    f"Descomposición {JOSEMARIA}+{LOS_AZULES} != minera(2030)={DEMANDA_MINERA_2030} (script 09)")

TRANSPORTE_APROBADO = 260.0   # solo Josemaría (ENRE) — único plan con acceso otorgado
BRECHA = DEMANDA_MINERA_2030 - TRANSPORTE_APROBADO   # 119 MW (número central)
HORIZONTE = 1500.0            # clúster total 2030s — CEO Glencore (Tier 2), sólo horizonte

print("\n" + "=" * 70)
print("SCRIPT 11 — El cable que falta (figura central, 2030)")
print("=" * 70)
print(f"  Demanda minera firme 2030 (de script 09): {DEMANDA_MINERA_2030:.1f} MW")
print(f"    = Josemaría {JOSEMARIA:.0f} + Los Azules {LOS_AZULES:.0f}")
print(f"  Transporte con plan aprobado (solo Josemaría): {TRANSPORTE_APROBADO:.0f} MW")
print(f"  BRECHA (demanda sin cable aprobado): {BRECHA:.0f} MW  <-- número central")
print(f"  Horizonte clúster 2030s (Tier 2): {HORIZONTE:.0f}+ MW")
print("=" * 70 + "\n")

# ── Paleta (consistente con el repo + colorblind-safe) ──────────────────────────
DARK_BLUE = "#1a3a5c"
MID_BLUE  = "#2e6da4"
GOLD      = "#c8972a"
RED       = "#c0392b"
GREY      = "#7f8c8d"
GHOST     = "#c7d2dd"

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.titlecolor': DARK_BLUE,
    'figure.facecolor': 'white',
})

fig, ax = plt.subplots(figsize=(9.5, 6.2))

x_dem, x_cap, x_hor = 0.0, 1.1, 2.5
W = 0.62

# Barra 1: demanda minera firme 2030 (apilada Josemaría + Los Azules)
ax.bar(x_dem, JOSEMARIA, W, color=MID_BLUE, edgecolor='white',
       label='Josemaría — 260 MW (ENRE Res. 79/2026)')
ax.bar(x_dem, LOS_AZULES, W, bottom=JOSEMARIA, color=GOLD, edgecolor='white',
       label='Los Azules — 119 MW (NI 43-101, nov. 2025)')

# Barra 2: capacidad de transporte con plan aprobado (solo Josemaría)
ax.bar(x_cap, TRANSPORTE_APROBADO, W, color=DARK_BLUE, edgecolor='white',
       label='Transporte con plan aprobado — 260 MW (solo Josemaría)')

# Barra fantasma: horizonte 1.500+ MW (Tier 2/3)
ax.bar(x_hor, HORIZONTE, W, color=GHOST, edgecolor=GREY, linewidth=1.0,
       hatch='//', label='Horizonte clúster 2030s — 1.500+ MW (Tier 2/3)')

# ── Resaltar la brecha de 119 MW (el tramo dorado por encima del techo aprobado) ─
# Línea de "techo de transporte aprobado" (260 MW) cruzando ambas barras
ax.plot([x_dem - W/2 - 0.05, x_cap + W/2 + 0.05],
        [TRANSPORTE_APROBADO, TRANSPORTE_APROBADO],
        color=RED, lw=1.2, ls='--', alpha=0.8, zorder=5)
ax.text(x_cap + W/2 + 0.08, TRANSPORTE_APROBADO,
        'techo de transporte\naprobado (260 MW)',
        color=RED, fontsize=7.8, va='center', ha='left', style='italic')

# Flecha doble sobre el tramo dorado (260 → 379) = la brecha
brk_x = x_dem - W/2 - 0.16
ax.annotate('', xy=(brk_x, DEMANDA_MINERA_2030), xytext=(brk_x, TRANSPORTE_APROBADO),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=1.8))
# Callout ubicado en el espacio libre superior, con guía hacia el tramo dorado
ax.annotate(f'BRECHA = {BRECHA:.0f} MW\nde demanda firme\nSIN cable aprobado',
            xy=(x_dem, (DEMANDA_MINERA_2030 + TRANSPORTE_APROBADO) / 2),
            xytext=(x_dem + 0.30, 560),
            color=RED, fontsize=10.5, fontweight='bold', va='center', ha='left',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.4),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fdecea',
                      edgecolor=RED, alpha=0.95))

# Etiquetas de valor
ax.text(x_dem, DEMANDA_MINERA_2030 + 22, f'{DEMANDA_MINERA_2030:.0f} MW',
        ha='center', fontsize=11, fontweight='bold', color=DARK_BLUE)
ax.text(x_dem, JOSEMARIA/2, '260', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='white')
ax.text(x_dem, JOSEMARIA + LOS_AZULES/2, '119', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='white')
ax.text(x_cap, TRANSPORTE_APROBADO + 22, f'{TRANSPORTE_APROBADO:.0f} MW',
        ha='center', fontsize=11, fontweight='bold', color=DARK_BLUE)
ax.text(x_hor, HORIZONTE + 22, f'{HORIZONTE:.0f}+ MW', ha='center',
        fontsize=10.5, fontweight='bold', color=GREY)

# ── Ejes y textos ───────────────────────────────────────────────────────────────
ax.set_xticks([x_dem, x_cap, x_hor])
ax.set_xticklabels(['Demanda minera\nfirme 2030',
                    'Transporte con\nplan aprobado',
                    'Horizonte\n2030s'], fontsize=10)
ax.set_ylabel('MW', fontsize=11)
ax.set_ylim(0, HORIZONTE * 1.16)
ax.set_xlim(-0.6, 3.2)
ax.set_title('El cable que falta: demanda minera firme vs. transporte aprobado (2030)',
             pad=14)
ax.legend(fontsize=8.6, loc='upper left', framealpha=0.95, edgecolor='#D5DBDB')

ax.text(0.0, -0.135,
        'Demanda minera firme 2030 = 379 MW (output del script 09: Josemaría 260 + Los Azules 119). '
        'Plan de transporte aprobado: 260 MW (solo Josemaría, ENRE Res. 79/2026).\n'
        'Brecha = 119 MW (no depende del CAGR provincial). Horizonte 1.500+ MW: CEO Glencore (mayo 2026, '
        'Tier 2) + El Pachón (~600 MW, Tier 3) — sólo escala temporal, no número central.',
        transform=ax.transAxes, fontsize=7.6, color=GREY, style='italic')

fig.tight_layout()
ruta = os.path.join(REPORTS, '11_01_brecha_cable.png')
fig.savefig(ruta, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Figura guardada: {ruta}")
