"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 05: Caso de estudio — La línea 500kV y el modelo de infraestructura
==========================================================================
Objetivo:
  - Construir la línea de tiempo regulatoria del conflicto por la línea 500kV
  - Visualizar el modelo fragmentado vs. coordinado de infraestructura
  - Mostrar qué cubre y qué NO cubre la propuesta de Vicuña
  - Conectar el caso regulatorio con el gap analysis del script 04_

Este script no usa nuevas fuentes de datos — trabaja con los datos
auditados en la investigación y los conecta con los gráficos anteriores.

Fuentes documentadas:
  - ENRE Res. 79/2026 (18 feb 2026): prioridad Vicuña 90%/25 años
  - ENRE Res. 165/2026 y 214/2026 (abr 2026): corrección, excluye Filo del Sol
  - Tiempo de San Juan, Econojournal, Diario de Cuyo — mar/abr/may 2026
  - Declaraciones CEO Glencore Argentina, Expo Minera SJ, mayo 2026
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import os
from datetime import datetime

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':   'DejaVu Sans',
    'font.size':     10.5,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.spines.top':    False,
    'axes.spines.right':  False,
    'figure.dpi':    150,
})

print("=" * 60)
print("SCRIPT 05 — CASO DE ESTUDIO: LÍNEA 500kV")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")


# ============================================================
# GRÁFICO 1 — LÍNEA DE TIEMPO REGULATORIA
# ============================================================
print("--- Gráfico 1: Línea de tiempo regulatoria ---")

eventos = [
    {
        'fecha':  'Ago 2024',
        'x':      0,
        'titulo': 'MOU\nLos Azules–YPF Luz',
        'desc':   'Los Azules firma acuerdo\nde suministro renovable\nexclusivo con YPF Luz',
        'actor':  'Los Azules',
        'color':  '#E67E22',
        'y':      1,
    },
    {
        'fecha':  'Feb 2026',
        'x':      2,
        'titulo': 'ENRE Res.\n79/2026',
        'desc':   'ENRE otorga a Vicuña 90%\nde la capacidad NUEVA que\ndesbloquea energizar a 500 kV\nla línea SJ–Rodeo (25 años)',
        'actor':  'Vicuña (BHP+Lundin)',
        'color':  '#C0392B',
        'y':      -1,
    },
    {
        'fecha':  'Mar 2026',
        'x':      3,
        'titulo': 'Oposiciones\nformales',
        'desc':   '8 actores presentan\nobjeciones: EPRE SJ,\nLos Azules, Municipios,\nLa Rioja, otros',
        'actor':  'Múltiples actores',
        'color':  '#8E44AD',
        'y':      1,
    },
    {
        'fecha':  'Abr 2026',
        'x':      4.5,
        'titulo': 'ENRE Res.\n214/2026',
        'desc':   'Corrección: excluye\nFilo del Sol. Solo\ncubre Josemaría\nFase 1 (260 MW)',
        'actor':  'ENRE',
        'color':  '#D35400',
        'y':      -1,
    },
    {
        'fecha':  'May 2026',
        'x':      6,
        'titulo': 'CEO Glencore\nExpo Minera SJ',
        'desc':   'Pérez de Solay critica\nel modelo de infra\npropia: "pierden\nel foco"',
        'actor':  'Glencore',
        'color':  '#27AE60',
        'y':      1,
    },
    {
        'fecha':  '3 jun 2026',
        'x':      8.8,
        'titulo': 'Audiencia\npública',
        'desc':   'Se realiza la audiencia\npública por el acceso\ny las condiciones de\nuso de la línea',
        'actor':  'ENRE / actores',
        'color':  '#7F8C8D',
        'y':      -1,
    },
]

fig, ax = plt.subplots(figsize=(18, 7))

# Línea de tiempo horizontal
ax.axhline(y=0, color='#BDC3C7', lw=2.5, zorder=1)

# Corregir x de cada evento para mayor espaciado
x_posiciones = [0, 2.2, 3.8, 5.4, 7.0, 8.8]
for ev, xp in zip(eventos, x_posiciones):
    ev['x'] = xp

for ev in eventos:
    x, y, color = ev['x'], ev['y'], ev['color']

    # Punto en la línea
    ax.plot(x, 0, 'o', color=color, markersize=14, zorder=3, markeredgecolor='white', markeredgewidth=1.5)

    # Línea vertical al texto
    ax.plot([x, x], [0, y * 0.55], color=color, lw=1.5, linestyle='--', alpha=0.7, zorder=2)

    # Caja de texto
    ax.text(x, y * 0.75,
            f"{ev['fecha']}\n\n{ev['titulo']}",
            ha='center', va='center',
            fontsize=8.8, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=color, linewidth=1.5, alpha=0.95))

    # Descripción debajo/arriba del recuadro — offset mayor para no pisarse
    offset = 0.48 if y > 0 else -0.48
    ax.text(x, y * 0.75 + offset,
            ev['desc'],
            ha='center', va='center',
            fontsize=7.5, color='#5D6D7E', style='italic')

ax.set_xlim(-0.8, 9.8)
ax.set_ylim(-2.1, 2.1)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_title(
    'Línea de tiempo: el conflicto por la infraestructura eléctrica del norte de San Juan',
    fontsize=13, fontweight='bold', pad=15
)
ax.text(0.5, -0.08,
        'Fuentes: ENRE (resoluciones 79, 165 y 214/2026), Tiempo de San Juan, Econojournal, Diario de Cuyo — feb/jun 2026',
        transform=ax.transAxes, ha='center', fontsize=7.5, color='#95A5A6', style='italic')

plt.tight_layout()
ruta1 = f'{REPORTS_DIR}/05_01_timeline_regulatorio.png'
plt.savefig(ruta1, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta1}")


# ============================================================
# GRÁFICO 2 — LÍNEAS SEPARADAS vs. TRONCOS REGIONALES
# La geografía importa: los proyectos están en DOS regiones
# (Norte/Iglesia y Sur/Calingasta), separadas ~150 km. No existe
# un único corredor posible para los cuatro; la coordinación es
# REGIONAL. El tronco norte (San Juan–Rodeo, 500 kV) YA EXISTE.
# ============================================================
print("--- Gráfico 2: Líneas separadas vs. troncos regionales ---")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# ---- Paleta ----
C_VICUNA = '#C0392B'   # Josemaría + Filo del Sol (Vicuña, norte)
C_LOSAZ  = '#E67E22'   # Los Azules (sur)
C_PACHON = '#8E44AD'   # El Pachón (sur)
C_GRID   = '#2980B9'
C_GRAY   = '#BDC3C7'
C_GREEN  = '#27AE60'

def caja_mina(ax, x, y, nombre, mw, color):
    rect = mpatches.FancyBboxPatch(
        (x - 0.42, y - 0.24), 0.84, 0.48,
        boxstyle='round,pad=0.04', facecolor=color, edgecolor='white',
        linewidth=2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(x, y, f'{nombre}\n{mw}', ha='center', va='center',
            fontsize=7.2, fontweight='bold', color='white')

def nodo_sadi(ax, x, y):
    circ = plt.Circle((x, y), 0.30, color=C_GRID, zorder=4)
    ax.add_patch(circ)
    ax.text(x, y, 'SADI\n(valle)', ha='center', va='center',
            fontsize=7.3, fontweight='bold', color='white', zorder=5)

# Posiciones de las minas (idénticas en ambos paneles)
MINAS = [
    (0.60, 4.05, 'Josemaría',    '260 MW',       C_VICUNA),
    (1.45, 4.05, 'Filo del Sol', 'expansión',    C_VICUNA),
    (2.70, 4.05, 'Los Azules',   '119 MW',       C_LOSAZ),
    (3.55, 4.05, 'El Pachón',    '~600 MW est.', C_PACHON),
]

def base_panel(ax, titulo, color_t):
    ax.set_xlim(0, 4.15); ax.set_ylim(-0.75, 5.05)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(titulo, fontsize=11, fontweight='bold', color=color_t, pad=8)
    for (x, y, n, mw, c) in MINAS:
        caja_mina(ax, x, y, n, mw, c)
    nodo_sadi(ax, 2.0, 0.5)
    ax.text(1.02, 4.62, 'NORTE · Iglesia', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#34495E')
    ax.text(3.12, 4.62, 'SUR · Calingasta', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#34495E')

# =========================================
# PANEL IZQUIERDO: LÍNEAS SEPARADAS (actual)
# =========================================
axL = axes[0]
base_panel(axL, 'Modelo actual: una línea por operador', '#E74C3C')

# Norte (Vicuña): Josemaría + Filo comparten una línea (mismo operador)
jx = 1.02
axL.plot([0.60, jx], [3.81, 2.55], color=C_VICUNA, lw=1.6, alpha=0.75)
axL.plot([1.45, jx], [3.81, 2.55], color=C_VICUNA, lw=1.6, alpha=0.75)
axL.annotate('', xy=(1.80, 0.72), xytext=(jx, 2.55),
             arrowprops=dict(arrowstyle='->', color=C_VICUNA, lw=2.3,
                             connectionstyle='arc3,rad=0.12'))
axL.text(0.78, 1.55, 'línea Vicuña\n(norte)', ha='center', va='center',
         fontsize=6.8, color=C_VICUNA, fontweight='bold')

# Sur: Los Azules y El Pachón, cada uno su línea (paralelas)
axL.annotate('', xy=(2.18, 0.72), xytext=(2.70, 3.81),
             arrowprops=dict(arrowstyle='->', color=C_LOSAZ, lw=2.3,
                             connectionstyle='arc3,rad=-0.10'))
axL.annotate('', xy=(2.36, 0.62), xytext=(3.55, 3.81),
             arrowprops=dict(arrowstyle='->', color=C_PACHON, lw=2.3,
                             connectionstyle='arc3,rad=-0.22'))
axL.text(3.55, 1.55, 'dos líneas\nseparadas\n(sur)', ha='center', va='center',
         fontsize=6.8, color='#7F8C8D', fontweight='bold', style='italic')

axL.text(2.0, -0.45,
         'Los Azules y El Pachón (sur) construyen líneas separadas y paralelas.\n'
         'Según el CEO de Glencore Argentina, este modelo genera "los costos más altos del mundo".',
         ha='center', va='center', fontsize=7,
         color='#E74C3C', fontweight='bold',
         bbox=dict(facecolor='#FDEDEC', edgecolor='#E74C3C', alpha=0.9,
                   boxstyle='round,pad=0.3'))

# =========================================
# PANEL DERECHO: TRONCOS REGIONALES (alternativa)
# =========================================
axR = axes[1]
base_panel(axR, 'Alternativa: troncos regionales compartidos', '#27AE60')

# Tronco NORTE (ya existe)
axR.plot([0.32, 1.72], [2.4, 2.4], color=C_GREEN, lw=6,
         solid_capstyle='round', alpha=0.85, zorder=3)
axR.plot([0.60, 0.40], [3.81, 2.42], color=C_GRAY, lw=1.6, linestyle='--', alpha=0.7)
axR.plot([1.45, 1.64], [3.81, 2.42], color=C_GRAY, lw=1.6, linestyle='--', alpha=0.7)
axR.text(1.02, 2.52, 'TRONCO NORTE (vía Rodeo)\nYA EXISTE · 500 kV',
         ha='center', va='bottom', fontsize=6.4, color=C_GREEN, fontweight='bold')
axR.annotate('', xy=(1.82, 0.72), xytext=(1.02, 2.35),
             arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2.6,
                             connectionstyle='arc3,rad=0.12'))

# Tronco SUR (a construir)
axR.plot([2.32, 3.82], [2.4, 2.4], color=C_GREEN, lw=6,
         solid_capstyle='round', alpha=0.85, zorder=3)
axR.plot([2.70, 2.50], [3.81, 2.42], color=C_GRAY, lw=1.6, linestyle='--', alpha=0.7)
axR.plot([3.55, 3.74], [3.81, 2.42], color=C_GRAY, lw=1.6, linestyle='--', alpha=0.7)
axR.text(3.07, 2.52, 'TRONCO SUR (vía Calingasta)\na construir · compartido',
         ha='center', va='bottom', fontsize=6.4, color=C_GREEN, fontweight='bold')
axR.annotate('', xy=(2.18, 0.72), xytext=(3.07, 2.35),
             arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2.6,
                             connectionstyle='arc3,rad=-0.12'))

axR.text(2.0, -0.45,
         'Coordinación REGIONAL: el norte ya tiene su tronco (existe); en el sur,\n'
         'Los Azules y El Pachón compartirían un corredor en vez de dos líneas paralelas.\n'
         'La geografía (~150 km entre regiones) impide un único corredor para los cuatro.',
         ha='center', va='center', fontsize=6.5,
         color=C_GREEN, fontweight='bold',
         bbox=dict(facecolor='#EAFAF1', edgecolor=C_GREEN, alpha=0.9,
                   boxstyle='round,pad=0.3'))

# Separador vertical entre paneles
fig.add_artist(plt.Line2D([0.5, 0.5], [0.06, 0.92],
                           transform=fig.transFigure,
                           color='#BDC3C7', lw=1.5, linestyle='--'))

fig.suptitle(
    '¿Líneas separadas o troncos regionales compartidos?\n'
    'Los proyectos están en dos regiones (Norte/Iglesia y Sur/Calingasta), separadas ~150 km',
    fontsize=12.5, fontweight='bold', y=1.02)

plt.tight_layout()
ruta2 = f'{REPORTS_DIR}/05_02_modelo_fragmentado_vs_coordinado.png'
plt.savefig(ruta2, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta2}")


# ============================================================
# GRÁFICO 3 — LA CADENA DE INFRAESTRUCTURA PARA UN SOLO PROYECTO
# (reformulado: de "cobertura acumulada" a fragmentación concreta)
# Muestra TODA la infraestructura que requiere abastecer solo a
# Josemaría (260 MW), el primero y más chico de los proyectos.
# Fuentes: ENRE Res. 79/2026, Transener, EPRE, Minería y Desarrollo (dic 2024).
# ============================================================
print("--- Gráfico 3: Cadena de infraestructura (fragmentación) ---")

fig, ax = plt.subplots(figsize=(16, 7.5))
ax.set_xlim(0, 11.6)
ax.set_ylim(-1.7, 2.5)
ax.axis('off')

C_EXIST   = '#5D8AA8'   # infraestructura existente
C_UPGRADE = '#E67E22'   # existente, requiere re-energización a 500 kV
C_NUEVO   = '#C0392B'   # infraestructura NUEVA requerida
C_MINA2   = '#8E44AD'   # la mina

def estacion(ax, x, y, titulo, sub, color, etiqueta):
    box = mpatches.FancyBboxPatch(
        (x - 0.64, y - 0.42), 1.28, 0.84,
        boxstyle='round,pad=0.04', facecolor=color, edgecolor='white',
        linewidth=2, alpha=0.93, zorder=4)
    ax.add_patch(box)
    ax.text(x, y + 0.12, titulo, ha='center', va='center', fontsize=8.6,
            fontweight='bold', color='white', zorder=5)
    ax.text(x, y - 0.20, sub, ha='center', va='center', fontsize=6.8,
            color='white', zorder=5)
    ecolor = {'existente': '#7F8C8D', 'NUEVA': C_NUEVO}.get(etiqueta, C_UPGRADE)
    ax.text(x, y + 0.55, etiqueta, ha='center', va='bottom', fontsize=7.4,
            fontweight='bold', color=ecolor)

def tramo(ax, x1, x2, y, texto, color, nuevo):
    ax.plot([x1, x2], [y, y], color=color, lw=8 if nuevo else 6,
            solid_capstyle='round', zorder=2, alpha=0.92)
    ax.text((x1 + x2) / 2, y - 0.52, texto, ha='center', va='top', fontsize=7.2,
            color=color, fontweight='bold')

Y = 1.05
# --- Estaciones (cadena de izquierda a derecha) ---
estacion(ax, 1.15, Y, 'ET Nueva\nSan Juan', 'conecta al SADI\nadecuar a 500 kV', C_EXIST, 'existente')
estacion(ax, 4.05, Y, 'ET Rodeo', 'nueva playa\n500 kV',                         C_EXIST, 'existente')
estacion(ax, 6.95, Y, 'ET Chaparro', '500/220 kV · GIS\n~3.000 msnm',            C_NUEVO, 'NUEVA')
estacion(ax, 9.20, Y, 'ET Josemaría', 'en la mina',                              C_NUEVO, 'NUEVA')
# Mina
circ = plt.Circle((10.75, Y), 0.44, color=C_MINA2, zorder=4, ec='white', lw=2)
ax.add_patch(circ)
ax.text(10.75, Y, 'Mina\n260 MW', ha='center', va='center', fontsize=7.6,
        fontweight='bold', color='white', zorder=5)

# --- Tramos de línea ---
tramo(ax, 1.79, 3.41, Y, 'línea EXISTENTE · 161 km\nre-energizar 132 → 500 kV', C_UPGRADE, nuevo=False)
tramo(ax, 4.69, 6.31, Y, 'NUEVA línea 500 kV\n~167 km',                          C_NUEVO,   nuevo=True)
tramo(ax, 7.59, 8.56, Y, 'NUEVA 220 kV\ndoble terna · ~93 km',                   C_NUEVO,   nuevo=True)
ax.plot([9.84, 10.31], [Y, Y], color=C_MINA2, lw=6, solid_capstyle='round', zorder=2)

# SADI a la izquierda
ax.annotate('', xy=(0.51, Y), xytext=(0.05, Y),
            arrowprops=dict(arrowstyle='->', color='#34495E', lw=2))
ax.text(0.05, Y + 0.30, 'SADI', ha='left', va='center', fontsize=8.5, color='#34495E', fontweight='bold')

# --- Leyenda de colores ---
leg = [
    mpatches.Patch(facecolor=C_EXIST, edgecolor='white', label='Infraestructura existente'),
    mpatches.Patch(facecolor=C_UPGRADE, edgecolor='white', label='Existente — requiere re-energización a 500 kV'),
    mpatches.Patch(facecolor=C_NUEVO, edgecolor='white', label='Infraestructura NUEVA requerida'),
]
ax.legend(handles=leg, loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, framealpha=0.9, edgecolor='#D5DBDB')

# --- Título ---
ax.set_title('Lo que requiere UN SOLO proyecto: la cadena de infraestructura para Josemaría (260 MW)',
             fontsize=13, fontweight='bold', pad=16)

# --- Cajas resumen ---
ax.text(5.8, -0.62,
        'Para abastecer SOLO a Josemaría —el primero y más chico del clúster (260 MW)— hace falta:\n'
        're-energizar a 500 kV la línea existente  +  2 líneas nuevas (~260 km)  +  1 estación transformadora nueva (Chaparro).',
        ha='center', va='center', fontsize=8.8, color='#2C3E50',
        bbox=dict(facecolor='#FBFCFC', edgecolor='#AEB6BF', alpha=0.92, boxstyle='round,pad=0.5', linewidth=1))

ax.text(5.8, -1.35,
        'Los Azules, El Pachón y Filo del Sol requieren CADA UNO su propia cadena de infraestructura. No hay un plan de corredor compartido.',
        ha='center', va='center', fontsize=9, color='#C0392B', fontweight='bold',
        bbox=dict(facecolor='#FDEDEC', edgecolor='#C0392B', alpha=0.95, boxstyle='round,pad=0.4', linewidth=1.2))

# Fuentes
ax.text(0.5, -0.02,
        'Fuentes: ENRE Res. 79/2026; Transener; EPRE San Juan; Minería y Desarrollo (dic. 2024) — obras del PIEAT Rodeo–Josemaría (LEAT+LAT ~260 km)',
        transform=ax.transAxes, ha='center', va='top', fontsize=7.2, color='#95A5A6', style='italic')

plt.tight_layout()
ruta3 = f'{REPORTS_DIR}/05_03_fragmentacion_infraestructura.png'
plt.savefig(ruta3, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta3}")
print("  ⚠ Nota: el gráfico 05_03 se renombró (cadena de infraestructura).")
print("    Podés borrar el viejo reports/05_03_cobertura_propuestas.png")


# ============================================================
# RESUMEN EN CONSOLA
# ============================================================
print(f"""
{'=' * 60}
RESUMEN DEL 05_
{'=' * 60}
  Gráficos generados:
    05_01_timeline_regulatorio.png
    05_02_modelo_fragmentado_vs_coordinado.png
    05_03_fragmentacion_infraestructura.png

  Conclusión del caso de estudio:
    La conexión al norte ya existe como línea de 500 kV pero opera
    a 132 kV. Energizarla a 500 kV (ENRE Res. 79/2026) desbloquea
    capacidad nueva, 90% asignada a Josemaría (260 MW). Pero abastecer
    solo a Josemaría requiere, además, 2 líneas nuevas (~260 km) y la
    nueva ET Chaparro. Los Azules, El Pachón y Filo del Sol necesitan
    cada uno su propia cadena: el modelo es un patchwork descoordinado.

    El CEO de Glencore Argentina lo dijo en mayo 2026: las mineras que
    construyen infraestructura propia "pierden el foco" y generan los
    costos más altos del mundo.

{'=' * 60}

PRÓXIMO PASO: 06_ — README en inglés + project_log final.
""")
