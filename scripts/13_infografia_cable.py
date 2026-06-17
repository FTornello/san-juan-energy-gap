#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 13 — Infografía vertical "El cable que falta" (formato LinkedIn, 1080x1920).

Fuente de contenido y números: reports/San_Juan_Energy_Gap_Relato_v2.md.
Una sola pieza vertical. Paleta del proyecto. Todos los números coinciden con el
relato v2. Regla Tier: El Pachón etiquetado como estimación (Tier 3).

Números canónicos usados (coinciden con el relato v2 y los scripts):
  - Josemaría 260 MW (ENRE Res. 79/2026); Los Azules 119 MW (NI 43-101, nov. 2025).
  - Demanda minera firme 2030 = 379 MW (= 260 + 119, output del script 09).
  - Transporte con plan aprobado = 260 MW (solo Josemaría).
  - Brecha = 119 MW (número central). Horizonte clúster = 1.500+ MW (Tier 2).
  - El Pachón ~600 MW (Tier 3). Chile 78% renovable minería 2024 (COCHILCO).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
REPORTS    = os.path.join(REPO_ROOT, 'reports')
os.makedirs(REPORTS, exist_ok=True)

# ── Números (coinciden con el relato v2) ────────────────────────────────────────
JOSEMARIA, LOS_AZULES = 260, 119
DEMANDA_FIRME = JOSEMARIA + LOS_AZULES          # 379
TRANSPORTE_APROBADO = 260
BRECHA = DEMANDA_FIRME - TRANSPORTE_APROBADO    # 119 (número central)
assert DEMANDA_FIRME == 379 and BRECHA == 119, "Números no coinciden con el relato v2"

# ── Paleta del proyecto ─────────────────────────────────────────────────────────
DARK   = "#1a3a5c"
MID    = "#2e6da4"
GOLD   = "#c8972a"
RED    = "#c0392b"
GREEN  = "#1e8449"
GREY   = "#7f8c8d"
LIGHT  = "#f2f4f7"
GHOST  = "#c7d2dd"
WHITE  = "#ffffff"

plt.rcParams.update({'font.family': 'DejaVu Sans'})

# Lienzo 1080x1920 px  (figsize 10.8x19.2 @ dpi 100). Coordenadas 0..100 x 0..178.
fig = plt.figure(figsize=(10.8, 19.2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 178)
ax.axis('off')
ax.set_facecolor(WHITE)
fig.patch.set_facecolor(WHITE)

def rbox(x, y, w, h, fc, ec='none', lw=0, r=1.2, alpha=1.0, z=2, hatch=None):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f'round,pad=0,rounding_size={r}',
                       facecolor=fc, edgecolor=ec, linewidth=lw, alpha=alpha,
                       zorder=z, hatch=hatch)
    ax.add_patch(p)
    return p

def txt(x, y, s, size, color=DARK, weight='normal', ha='center', va='center',
        z=5, style='normal', spacing=1.0):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            zorder=z, style=style, linespacing=spacing)

# ════════════════════════════════════════════════════════════════════════════════
# ENCABEZADO
# ════════════════════════════════════════════════════════════════════════════════
rbox(0, 160, 100, 18, DARK, r=0, z=1)
txt(50, 173.5, 'SAN JUAN  ·  COBRE  ·  ENERGÍA', 13, GHOST, 'bold')
txt(50, 168.2, 'EL CABLE QUE FALTA', 34, WHITE, 'bold')
txt(50, 162.6, 'Por qué el boom del cobre no es un problema de generación',
    13.5, GOLD, 'bold')

# ════════════════════════════════════════════════════════════════════════════════
# 1 · GANCHO
# ════════════════════════════════════════════════════════════════════════════════
txt(6, 154.5, '1', 17, GOLD, 'bold', ha='left')
txt(11, 154.6, 'EL PROBLEMA', 12.5, GREY, 'bold', ha='left')
txt(6, 150.0, 'No es generar energía.', 20, DARK, 'bold', ha='left')
txt(6, 145.6, 'Es transportarla hasta la cordillera.', 20, RED, 'bold', ha='left')
rbox(6, 134.5, 88, 8.6, LIGHT, r=1.4)
txt(50, 138.8,
    'San Juan tiene 861 MW instalados y al mediodía EXPORTA energía.',
    12.5, DARK, 'normal')
txt(50, 136.0,
    'Las minas están a 250–410 km y se conectan al SADI: el cuello de botella\n'
    'es una línea de 500 kV que hoy opera a 132 kV.',
    11, GREY, 'normal', spacing=1.3)

# ════════════════════════════════════════════════════════════════════════════════
# 2 · NÚMERO CENTRAL
# ════════════════════════════════════════════════════════════════════════════════
rbox(6, 108, 88, 23.5, DARK, r=1.6)
txt(11, 128.5, '2', 17, GOLD, 'bold', ha='left')
txt(17, 128.6, 'EL NÚMERO CENTRAL', 12.5, GHOST, 'bold', ha='left')
txt(50, 121.0, f'{BRECHA} MW', 64, WHITE, 'bold')
txt(50, 114.3, 'de demanda minera firme SIN cable aprobado en 2030', 13.5, GOLD, 'bold')
txt(50, 110.4,
    f'{DEMANDA_FIRME} MW de demanda firme (Josemaría {JOSEMARIA} + Los Azules {LOS_AZULES})'
    f'  −  {TRANSPORTE_APROBADO} MW único plan aprobado  =  {BRECHA} MW',
    10.5, GHOST, 'normal')

# ════════════════════════════════════════════════════════════════════════════════
# 3 · LOS TRES CAMINOS
# ════════════════════════════════════════════════════════════════════════════════
txt(6, 103.5, '3', 17, GOLD, 'bold', ha='left')
txt(11, 103.6, 'CADA MINA RESUELVE SU PROPIO CABLE', 12.5, GREY, 'bold', ha='left')

cards = [
    dict(x=4.5,  acc=MID,   name='Josemaría',  oper='Vicuña (BHP+Lundin)',
         mw='260 MW', tier='ENRE Res. 79/2026',
         route='Acceso a la línea\n500 kV (vía ENRE)',
         badge=GOLD, st='PRIORIDAD OTORGADA\nfallo PENDIENTE'),
    dict(x=36.0, acc=GREEN, name='Los Azules', oper='McEwen Copper',
         mw='119 MW', tier='NI 43-101 (nov. 2025)',
         route='Línea de AT PROPIA\nvía YPF Luz (al SADI)',
         badge=GREEN, st='SOLUCIÓN EN MARCHA\n(acuerdo bilateral)'),
    dict(x=67.5, acc=GREY,  name='El Pachón',  oper='Glencore',
         mw='~600 MW', tier='estimación (Tier 3)',
         route='Sin plan de\ntransporte definido',
         badge=RED,   st='SIN SOLUCIÓN\nde transporte'),
]
CW, CH, CY = 28, 36, 62
for c in cards:
    x = c['x']
    rbox(x, CY, CW, CH, WHITE, ec=c['acc'], lw=2.2, r=1.4, z=3)
    rbox(x, CY + CH - 6.2, CW, 6.2, c['acc'], r=1.4, z=4)
    xc = x + CW/2
    txt(xc, CY + CH - 3.0, c['name'], 14.5, WHITE, 'bold', z=5)
    txt(xc, CY + CH - 8.6, c['oper'], 9.0, GREY, 'normal', z=5)
    txt(xc, CY + CH - 14.0, c['mw'], 23, c['acc'], 'bold', z=5)
    txt(xc, CY + CH - 17.6, c['tier'], 8.3, GREY, style='italic', z=5)
    ax.plot([x+3, x+CW-3], [CY+CH-19.6, CY+CH-19.6], color=GHOST, lw=1, zorder=5)
    txt(xc, CY + CH - 23.3, 'RUTA', 8.2, DARK, 'bold', z=5)
    txt(xc, CY + CH - 26.6, c['route'], 9.6, '#2c3e50', 'normal', z=5, spacing=1.25)
    rbox(x+2.2, CY + 1.6, CW-4.4, 6.0, c['badge'], r=1.0, z=4, alpha=0.95)
    txt(xc, CY + 4.6, c['st'], 8.8, WHITE, 'bold', z=5, spacing=1.2)

# ════════════════════════════════════════════════════════════════════════════════
# 4 · HORIZONTE (secundario, "fantasma")
# ════════════════════════════════════════════════════════════════════════════════
rbox(6, 47, 88, 11.5, LIGHT, ec=GHOST, lw=1.5, r=1.4, hatch='//')
txt(11, 55.6, '4', 16, GREY, 'bold', ha='left')
txt(17, 55.6, 'Y ESTO RECIÉN EMPIEZA', 12, GREY, 'bold', ha='left')
txt(50, 51.6, '1.500+ MW  ·  horizonte del clúster hacia los 2030s', 17, GREY, 'bold')
txt(50, 48.6,
    'El Pachón + Filo del Sol + expansiones (CEO Glencore, mayo 2026 · Tier 2/3) — '
    'escala temporal, NO el número central',
    9.5, GREY, style='italic')

# ════════════════════════════════════════════════════════════════════════════════
# 5 · CIERRE: ENRE + CHILE
# ════════════════════════════════════════════════════════════════════════════════
txt(6, 43.0, '5', 17, GOLD, 'bold', ha='left')
txt(11, 43.0, 'QUIÉN DECIDE  ·  Y CÓMO SE RESUELVE', 12.5, GREY, 'bold', ha='left')

# Panel ENRE
rbox(4.5, 23.5, 43, 16.5, WHITE, ec=DARK, lw=2, r=1.4)
rbox(4.5, 35.5, 43, 4.5, DARK, r=1.4)
txt(26, 37.7, 'JURISDICCIÓN NACIONAL', 11.5, WHITE, 'bold')
txt(26, 31.8, 'Acceso abierto (Ley 24.065).', 10.5, DARK, 'bold')
txt(26, 27.3,
    'El ENRE debatió en la audiencia\ndel 3-jun-2026 quién usa el único\n'
    'cable. Fallo de fondo PENDIENTE.',
    9.3, '#2c3e50', 'normal', spacing=1.3)

# Panel Chile
rbox(52.5, 23.5, 43, 16.5, WHITE, ec=GREEN, lw=2, r=1.4)
rbox(52.5, 35.5, 43, 4.5, GREEN, r=1.4)
txt(74, 37.7, 'EL ESPEJO DE CHILE', 11.5, WHITE, 'bold')
txt(74, 32.0, '78%', 22, GREEN, 'bold')
txt(74, 27.6,
    'de la electricidad minera chilena\nfue renovable en 2024 — vía contratos\n'
    'de largo plazo (PPA), no plantas propias.',
    9.3, '#2c3e50', 'normal', spacing=1.3)
txt(74, 24.4, 'COCHILCO', 8.0, GREY, style='italic')

# ════════════════════════════════════════════════════════════════════════════════
# PIE
# ════════════════════════════════════════════════════════════════════════════════
rbox(0, 0, 100, 16, DARK, r=0, z=1)
txt(50, 11.5, 'El problema no es la energía. Es el cable.', 15, WHITE, 'bold')
txt(50, 7.4,
    'Fuente: San Juan Energy Gap — Relato v2 (jun. 2026).  '
    'El Pachón ~600 MW = estimación (Tier 3).',
    9.5, GHOST, 'normal')
txt(50, 4.2, 'github.com/FTornello/san-juan-energy-gap', 9.5, GOLD, 'bold')

ruta = os.path.join(REPORTS, 'infografia_cable_que_falta.png')
fig.savefig(ruta, dpi=100, facecolor=WHITE)
plt.close(fig)
print(f"Infografía guardada: {ruta}")
print(f"Brecha central: {BRECHA} MW  | Demanda firme: {DEMANDA_FIRME} MW  | Aprobado: {TRANSPORTE_APROBADO} MW")
