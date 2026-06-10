#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 09 — Brecha de generación firme día vs. noche.

Supuestos explícitos:
  - Demanda provincial nocturna = pico de demanda provincial proyectado (supuesto conservador).
    No hay dato desagregado día/noche en EPRE. Si hubiera un perfil horario real, la
    demanda nocturna sería ~85-90% del pico. Usamos el pico como cota superior (Tier 3
    en este supuesto).
  - Base provincial: 551 MW en 2021 (EPRE Anuario 2021), CAGR 2%/año (script 08).
  - Capacidad firme nocturna: 258 MW (hidro + térmica, EPSE feb. 2025 — Tier 1).
  - Demanda minera: Josemaría 260 MW + Los Azules 119 MW desde 2030 (Tier 1),
    El Pachón ~600 MW desde 2036 (Tier 3).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

REPORTS = "/sessions/sweet-nifty-hopper/mnt/reports"
DARK_BLUE  = "#1a3a5c"
MID_BLUE   = "#2e6da4"
LIGHT_GREY = "#f2f4f7"
GOLD       = "#c8972a"
RED        = "#c0392b"
GREEN      = "#27ae60"
GREY       = "#7f8c8d"

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
BASE_YEAR  = 2021
BASE_MW    = 551.0
CAGR       = 0.020        # escenario base (Tier 1-base); ver script 08 para boom
FIRME_NOC  = 258.0        # MW firmes de noche (EPSE feb. 2025 — Tier 1)
CAP_DIA    = 861.0        # MW instalados con solar (EPSE feb. 2025 — Tier 1)

def prov(yr):
    """Demanda provincial proyectada (pico = cota sup. nocturna — supuesto)."""
    return BASE_MW * (1 + CAGR) ** (yr - BASE_YEAR)

def minera(yr):
    """Demanda minera según cronograma."""
    d = 0.0
    if yr >= 2030: d += 260.0   # Josemaría (Tier 1)
    if yr >= 2030: d += 119.0   # Los Azules (Tier 1)
    if yr >= 2036: d += 600.0   # El Pachón (Tier 3 — estimación)
    return d

# ── Años clave ────────────────────────────────────────────────────────────────
KEY_YEARS = [2025, 2030, 2036]
LABELS = {
    2025: 'Hoy\n(2025)',
    2030: '2030\n(Josemaría\n+ Los Azules)',
    2036: '2036\n(+ El Pachón\nest. Tier 3)',
}

# ── Output textual ────────────────────────────────────────────────────────────
print("=" * 70)
print("SCRIPT 09 — Brecha de generación firme día vs. noche")
print(f"Base provincial: {BASE_MW} MW en {BASE_YEAR}, CAGR {CAGR*100:.1f}%/año")
print(f"Firmes noche: {FIRME_NOC} MW | Instalado día: {CAP_DIA} MW")
print("=" * 70)
print(f"{'Año':>6}  {'Prov. (MW)':>11}  {'Minera (MW)':>12}  "
      f"{'Total noche (MW)':>17}  {'Déficit noche (MW)':>18}")
print("-" * 72)
results = {}
for yr in KEY_YEARS:
    p = prov(yr)
    m = minera(yr)
    tot = p + m
    deficit = tot - FIRME_NOC
    results[yr] = dict(prov=p, minera=m, total=tot, deficit=deficit)
    print(f"{yr:>6}  {p:>11.1f}  {m:>12.1f}  {tot:>17.1f}  {deficit:>18.1f}")

print()
print("Valores clave para documento (v3.1):")
for yr, r in results.items():
    print(f"  {yr}: demanda total nocturna = {r['total']:.1f} MW  |  "
          f"déficit nocturno = {r['deficit']:.1f} MW")
print()
print("SUPUESTO: demanda nocturna = pico provincial (no hay desagregación día/noche")
print("  en EPRE). Factor 90% solo sobre componente PROVINCIAL (la demanda minera es")
print("  24/7 constante — no se descuenta).")
# Corrección: el 90% aplica solo a la componente provincial, NO a la minera
prov_2030   = results[2030]['prov']
minera_2030 = results[2030]['minera']
deficit_90  = prov_2030 * 0.90 + minera_2030 - FIRME_NOC
print(f"  Factor 90% correcto → déficit 2030 = "
      f"{prov_2030:.1f} × 0,90 + {minera_2030:.1f} − {FIRME_NOC:.1f} = {deficit_90:.1f} MW.")
print(f"  (Error en v3: se aplicaba 90% al total incluyendo demanda minera → "
      f"{results[2030]['total']*0.90 - FIRME_NOC:.1f} MW — incorrecto)")
print("=" * 70)

# ── Figura ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.8))

x = np.arange(len(KEY_YEARS))
width = 0.25

# Barras: capacidad día, capacidad firme noche, demanda total noche
cap_dia_vals  = [CAP_DIA] * len(KEY_YEARS)
cap_noc_vals  = [FIRME_NOC] * len(KEY_YEARS)
total_vals    = [results[yr]['total'] for yr in KEY_YEARS]
deficit_vals  = [results[yr]['deficit'] for yr in KEY_YEARS]

bars1 = ax.bar(x - width, cap_dia_vals, width, color=MID_BLUE,
               alpha=0.85, label='Capacidad instalada total (con solar)', edgecolor='white')
bars2 = ax.bar(x,         cap_noc_vals, width, color=DARK_BLUE,
               alpha=0.85, label='Capacidad firme nocturna (hidro+térmica)', edgecolor='white')
bars3 = ax.bar(x + width, total_vals,   width, color=RED,
               alpha=0.78, label='Demanda total nocturna proyectada', edgecolor='white')

# Etiquetas de valor
for bar, v in zip(bars1, cap_dia_vals):
    ax.text(bar.get_x()+bar.get_width()/2, v+12, f'{v:.0f}',
            ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=MID_BLUE)
for bar in bars2:
    ax.text(bar.get_x()+bar.get_width()/2, FIRME_NOC+12, f'{FIRME_NOC:.0f}',
            ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=DARK_BLUE)
for bar, v, yr in zip(bars3, total_vals, KEY_YEARS):
    ax.text(bar.get_x()+bar.get_width()/2, v+12, f'{v:.0f}',
            ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=RED)
    # Anotación de déficit
    ax.annotate(f'Déficit\n{results[yr]["deficit"]:.0f} MW',
                xy=(bar.get_x()+bar.get_width()/2, FIRME_NOC),
                xytext=(bar.get_x()+bar.get_width()/2 + 0.12, FIRME_NOC + (v - FIRME_NOC)/2),
                fontsize=7.5, color=RED, ha='left',
                arrowprops=dict(arrowstyle='->', color=RED, lw=0.7))

# Línea firme 258 MW
ax.axhline(FIRME_NOC, color=DARK_BLUE, lw=1.2, ls='--', alpha=0.5, zorder=0)
ax.text(2.5, FIRME_NOC + 10, f'{FIRME_NOC:.0f} MW (firme nocturno)',
        fontsize=8, color=DARK_BLUE, ha='right', va='bottom')

ax.set_title('San Juan: capacidad firme disponible vs. demanda total proyectada de noche\n'
             '(2025, 2030, 2036 — escenario base CAGR 2%)', pad=10)
ax.set_xticks(x)
ax.set_xticklabels([LABELS[yr] for yr in KEY_YEARS], fontsize=9)
ax.set_ylabel('MW')
ax.set_ylim(0, max(total_vals) * 1.22)
ax.legend(fontsize=8.5, loc='upper left')
ax.text(0.0, -0.13,
        'Demanda provincial: 551 MW en 2021 (EPRE), CAGR 2%/año (Tier 1-base). '
        'Firmes noche: EPSE feb. 2025 (Tier 1). '
        'El Pachón 2036: ~600 MW (Tier 3 — estimación). '
        'Supuesto: demanda nocturna = pico provincial (Tier 3).',
        transform=ax.transAxes, fontsize=7.5, color=GREY, style='italic')
fig.tight_layout()
fig.savefig(f'{REPORTS}/09_01_brecha_dia_noche.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Figura guardada: {REPORTS}/09_01_brecha_dia_noche.png")
