#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 12 — "Cada mina resuelve su propio cable" (hallazgo del eje TRANSPORTE).

Visualiza, para los tres proyectos del corredor, CÓMO resuelve cada uno su
transporte de alta tensión hasta la cordillera:
  - Josemaría (Vicuña): vía acceso a la línea 500 kV SADI–Rodeo — ENRE, fallo pendiente.
  - Los Azules (McEwen): línea de AT propia vía YPF Luz, conectada al SADI — bilateral.
  - El Pachón (Glencore): sin plan de transporte definido.

Es la prueba del eje: el cuello de botella es el TRANSPORTE, tan claro que cada
proyecto debe resolverlo por separado (no hay corredor coordinado).

Fuentes:
  - Josemaría 260 MW: ENRE Res. 79/2026; audiencia 3 jun 2026 sin fallo de fondo (Res. 219/2026).
  - Los Azules 119 MW: NI 43-101 (nov. 2025); MoU/acuerdo Los Azules–YPF Luz (oct. 2025 / 2026).
  - El Pachón ~600 MW: estimación benchmark (Tier 3); sin factibilidad publicada.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
REPORTS    = os.path.join(REPO_ROOT, 'reports')
os.makedirs(REPORTS, exist_ok=True)

DARK_BLUE = "#1a3a5c"
GREY      = "#7f8c8d"
GREEN     = "#1e8449"
AMBER     = "#c8972a"
RED       = "#c0392b"
LIGHT     = "#f2f4f7"

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'figure.facecolor': 'white',
})

# ── Datos de cada tarjeta ───────────────────────────────────────────────────────
cards = [
    {
        'mina':   'Josemaría',
        'oper':   'Vicuña (BHP + Lundin)',
        'mw':     '260 MW',
        'tier':   'Tier 1 — ENRE Res. 79/2026',
        'region': 'NORTE · Iglesia',
        'ruta':   'Acceso a la línea 500 kV\nNueva San Juan–Rodeo\n(energizar 132 → 500 kV)\n+ LEAT Rodeo–Chaparro\n+ ET Chaparro + LAT 220 kV',
        'estado': 'PRIORIDAD OTORGADA\nfallo de fondo PENDIENTE',
        'badge':  AMBER,
        'accent': DARK_BLUE,
    },
    {
        'mina':   'Los Azules',
        'oper':   'McEwen Copper',
        'mw':     '119 MW',
        'tier':   'Tier 1 — NI 43-101 (nov. 2025)',
        'region': 'SUR · Calingasta',
        'ruta':   'Línea de alta tensión\nPROPIA vía YPF Luz\n(diseña, construye y\nfinancia el generador),\nconectada al SADI · 100% renov.',
        'estado': 'SOLUCIÓN BILATERAL\nen marcha (MoU/acuerdo)',
        'badge':  GREEN,
        'accent': GREEN,
    },
    {
        'mina':   'El Pachón',
        'oper':   'Glencore',
        'mw':     '~600 MW',
        'tier':   'Tier 3 — estimación benchmark',
        'region': 'SUR · Calingasta',
        'ruta':   'Sin plan de transporte\ndefinido. Sin factibilidad\npublicada. Requeriría su\npropio corredor en el sur\n(~150 km de Josemaría)',
        'estado': 'SIN SOLUCIÓN\nde transporte',
        'badge':  RED,
        'accent': GREY,
    },
]

fig, ax = plt.subplots(figsize=(13.5, 7.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6, 9.55, 'Cada mina resuelve su propio cable',
        ha='center', va='center', fontsize=16, fontweight='bold', color=DARK_BLUE)
ax.text(6, 9.0,
        'El cuello de botella es el TRANSPORTE: no hay corredor coordinado, cada proyecto negocia su acceso a la alta tensión por separado',
        ha='center', va='center', fontsize=9.5, color=GREY, style='italic')

card_w, card_h = 3.6, 7.0
x_starts = [0.45, 4.2, 7.95]
y_bottom = 1.05

for card, x0 in zip(cards, x_starts):
    # Marco de la tarjeta
    box = mpatches.FancyBboxPatch(
        (x0, y_bottom), card_w, card_h,
        boxstyle='round,pad=0.06,rounding_size=0.18',
        facecolor='white', edgecolor=card['accent'], linewidth=2.2, zorder=2)
    ax.add_patch(box)

    xc = x0 + card_w / 2
    # Franja superior con el nombre
    header = mpatches.FancyBboxPatch(
        (x0, y_bottom + card_h - 1.15), card_w, 1.15,
        boxstyle='round,pad=0.06,rounding_size=0.18',
        facecolor=card['accent'], edgecolor=card['accent'], zorder=3)
    ax.add_patch(header)
    ax.text(xc, y_bottom + card_h - 0.45, card['mina'],
            ha='center', va='center', fontsize=13.5, fontweight='bold', color='white', zorder=4)
    ax.text(xc, y_bottom + card_h - 0.88, card['oper'],
            ha='center', va='center', fontsize=8.5, color='white', zorder=4)

    # Región
    ax.text(xc, y_bottom + card_h - 1.45, card['region'],
            ha='center', va='center', fontsize=8, fontweight='bold', color=GREY)

    # Demanda MW
    ax.text(xc, y_bottom + card_h - 2.15, card['mw'],
            ha='center', va='center', fontsize=20, fontweight='bold', color=card['accent'])
    ax.text(xc, y_bottom + card_h - 2.62, card['tier'],
            ha='center', va='center', fontsize=7.3, color=GREY, style='italic')

    # Separador
    ax.plot([x0 + 0.3, x0 + card_w - 0.3],
            [y_bottom + card_h - 2.95, y_bottom + card_h - 2.95],
            color='#D5DBDB', lw=1)

    # Ruta de transporte
    ax.text(xc, y_bottom + card_h - 3.25, 'RUTA DE TRANSPORTE',
            ha='center', va='center', fontsize=7.6, fontweight='bold', color=DARK_BLUE)
    ax.text(xc, y_bottom + card_h - 4.25, card['ruta'],
            ha='center', va='center', fontsize=8.4, color='#2c3e50', linespacing=1.45)

    # Badge de estado
    badge = mpatches.FancyBboxPatch(
        (x0 + 0.35, y_bottom + 0.35), card_w - 0.7, 0.95,
        boxstyle='round,pad=0.04,rounding_size=0.12',
        facecolor=card['badge'], edgecolor='white', alpha=0.95, zorder=3)
    ax.add_patch(badge)
    ax.text(xc, y_bottom + 0.825, card['estado'],
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='white',
            zorder=4, linespacing=1.3)

# Nota al pie
ax.text(6, 0.35,
        'Fuentes: ENRE Res. 79 y 219/2026; NI 43-101 Los Azules (nov. 2025); acuerdo Los Azules–YPF Luz (oct. 2025 / 2026); '
        'El Pachón ~600 MW (Tier 3, benchmark). Estado al 16 jun 2026.',
        ha='center', va='center', fontsize=7.4, color=GREY, style='italic')

fig.tight_layout()
ruta = os.path.join(REPORTS, '12_01_solucion_por_mina.png')
fig.savefig(ruta, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Figura guardada: {ruta}")
