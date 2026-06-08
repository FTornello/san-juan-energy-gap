"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 00: Diagrama de flujo del sistema eléctrico argentino
============================================================
Objetivo (capa accesible / Fase 0):
  Explicar visualmente cómo funciona el sistema eléctrico antes de
  entrar al análisis técnico. Muestra:
    - El flujo físico: generación → transporte → distribución → consumo
    - Dónde se ubica el MEM (mercado mayorista)
    - El rol de CAMMESA (operador que equilibra gen = demanda 24/7)
    - Dónde se conectan los grandes usuarios (como las minas)

Este script no usa datos — es un diagrama conceptual.
Genera: reports/00_01_flujo_sistema_electrico.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':   'DejaVu Sans',
    'figure.dpi':    150,
})

# Paleta (coherente con el resto del proyecto)
C_TERMICA = '#E67E22'
C_HIDRO   = '#4A90D9'
C_NUCLEAR = '#9B59B6'
C_SOLAR   = '#F1C40F'
C_EOLICA  = '#27AE60'
C_RED     = '#2C3E50'   # transporte
C_DIST    = '#5D8AA8'   # distribución
C_USER    = '#95A5A6'   # consumo
C_MEM     = '#D4AC0D'   # mercado
C_CAMMESA = '#34495E'   # operador
C_MINA    = '#C0392B'   # grandes usuarios / minería

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


# ============================================================
# UTILIDADES
# ============================================================
def caja(x, y, w, h, texto, color, fc_text='white', fontsize=10, weight='bold', alpha=0.92):
    """Dibuja una caja redondeada con texto centrado."""
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle='round,pad=0.4,rounding_size=1.2',
        facecolor=color, edgecolor='white', linewidth=1.5,
        alpha=alpha, zorder=3
    )
    ax.add_patch(box)
    ax.text(x, y, texto, ha='center', va='center',
            fontsize=fontsize, fontweight=weight, color=fc_text, zorder=4)


def flecha(x1, y1, x2, y2, color='#7F8C8D', lw=2.2):
    """Dibuja una flecha de flujo."""
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='-|>', mutation_scale=20,
        color=color, lw=lw, zorder=2,
        shrinkA=2, shrinkB=2
    )
    ax.add_patch(arr)


# ============================================================
# TÍTULO
# ============================================================
ax.text(50, 96, 'Cómo funciona el sistema eléctrico argentino',
        ha='center', va='center', fontsize=17, fontweight='bold', color='#2C3E50')
ax.text(50, 91, 'De dónde viene la electricidad y cómo llega hasta el consumo',
        ha='center', va='center', fontsize=11, color='#7F8C8D', style='italic')


# ============================================================
# ENCABEZADOS DE LAS 4 ETAPAS
# ============================================================
etapas = [
    (13, '1. GENERACIÓN',   'Producen energía'),
    (38, '2. TRANSPORTE',   'La mueven a larga distancia'),
    (63, '3. DISTRIBUCIÓN', 'La entregan localmente'),
    (87, '4. CONSUMO',      'La usan'),
]
for x, titulo, sub in etapas:
    ax.text(x, 83, titulo, ha='center', va='center',
            fontsize=11.5, fontweight='bold', color='#2C3E50')
    ax.text(x, 79.5, sub, ha='center', va='center',
            fontsize=8.5, color='#95A5A6', style='italic')


# ============================================================
# ETAPA 1 — GENERACIÓN (5 fuentes apiladas)
# ============================================================
fuentes = [
    (74, 'Térmica\n(gas, carbón)', C_TERMICA),
    (66, 'Hidroeléctrica',         C_HIDRO),
    (58, 'Nuclear',                C_NUCLEAR),
    (50, 'Solar',                  C_SOLAR),
    (42, 'Eólica',                 C_EOLICA),
]
for y, nombre, color in fuentes:
    fc = '#2C3E50' if color == C_SOLAR else 'white'
    caja(13, y, 18, 6, nombre, color, fc_text=fc, fontsize=9)
    # Flecha de cada fuente hacia el transporte
    flecha(22.5, y, 29, 60)


# ============================================================
# ETAPA 2 — TRANSPORTE (la red de alta tensión / SADI)
# ============================================================
caja(38, 60, 18, 30,
     'RED DE\nTRANSPORTE\n\n500 / 220 / 132 kV\n\nSADI\n(Sistema Argentino\nde Interconexión)',
     C_RED, fontsize=10)

# Flecha transporte → distribución
flecha(47.5, 60, 54, 60)


# ============================================================
# ETAPA 3 — DISTRIBUCIÓN
# ============================================================
caja(63, 60, 17, 14,
     'Distribuidoras\nprovinciales\n\n(media y baja\ntensión)',
     C_DIST, fontsize=9)

# Flechas distribución → consumo (hogares/comercios)
flecha(71.5, 62, 78, 70)
flecha(71.5, 60, 78, 60)


# ============================================================
# ETAPA 4 — CONSUMO
# ============================================================
consumos = [
    (70, 'Hogares',   C_USER),
    (60, 'Comercios', C_USER),
    (50, 'Industria', C_USER),
]
for y, nombre, color in consumos:
    caja(87, y, 15, 6, nombre, color, fontsize=9)

# --- Grandes Usuarios: conexión DIRECTA al transporte (las minas) ---
caja(87, 36, 16, 9,
     'Grandes Usuarios\n(minería, industria\npesada)',
     C_MINA, fontsize=8.5)
# Línea directa desde el transporte (saltea la distribución)
arr = FancyArrowPatch(
    (38, 45), (79, 36),
    arrowstyle='-|>', mutation_scale=20,
    color=C_MINA, lw=2.5, linestyle='--', zorder=2,
    connectionstyle='arc3,rad=-0.15', shrinkA=4, shrinkB=4
)
ax.add_patch(arr)
ax.text(58, 38, 'Los grandes usuarios se conectan\nDIRECTO a la red de alta tensión\n(no pasan por la distribuidora)',
        ha='center', va='center', fontsize=7.5, color=C_MINA, style='italic',
        bbox=dict(facecolor='white', edgecolor=C_MINA, alpha=0.85,
                  boxstyle='round,pad=0.3', linewidth=0.8))


# ============================================================
# BANDA MEM — el mercado mayorista
# ============================================================
mem_box = FancyBboxPatch(
    (5, 22), 90, 7,
    boxstyle='round,pad=0.3,rounding_size=1',
    facecolor=C_MEM, edgecolor='white', linewidth=1.5, alpha=0.25, zorder=1
)
ax.add_patch(mem_box)
ax.text(8, 25.5, 'MEM', ha='left', va='center',
        fontsize=12, fontweight='bold', color='#9A7D0A')
ax.text(50, 25.5,
        'Mercado Eléctrico Mayorista:  los generadores VENDEN  ·  distribuidoras y grandes usuarios COMPRAN',
        ha='center', va='center', fontsize=9.5, color='#7D6608', fontweight='bold')


# ============================================================
# BANDA CAMMESA — el operador
# ============================================================
cammesa_box = FancyBboxPatch(
    (5, 11), 90, 7,
    boxstyle='round,pad=0.3,rounding_size=1',
    facecolor=C_CAMMESA, edgecolor='white', linewidth=1.5, alpha=0.92, zorder=1
)
ax.add_patch(cammesa_box)
ax.text(8, 14.5, 'CAMMESA', ha='left', va='center',
        fontsize=12, fontweight='bold', color='white')
ax.text(52, 14.5,
        'Opera y despacha todo el sistema  ·  equilibra generación = demanda en cada instante, las 24 hs',
        ha='center', va='center', fontsize=9.5, color='white', fontweight='bold')


# ============================================================
# CALLOUT — el concepto clave
# ============================================================
ax.text(50, 4.5,
        '⚡ Concepto clave: la electricidad NO se almacena en la red. Lo que se genera se consume en el mismo instante.\n'
        'Por eso CAMMESA ajusta la generación segundo a segundo para seguir a la demanda.',
        ha='center', va='center', fontsize=9, color='#2C3E50',
        bbox=dict(facecolor='#FEF9E7', edgecolor='#D4AC0D', alpha=0.95,
                  boxstyle='round,pad=0.5', linewidth=1.5))


plt.tight_layout()
ruta = f'{REPORTS_DIR}/00_01_flujo_sistema_electrico.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()

print("=" * 60)
print("SCRIPT 00 — DIAGRAMA DE FLUJO DEL SISTEMA")
print("=" * 60)
print(f"\n✓ Guardado: {ruta}")
print("""
Este es el primer diagrama de la capa accesible (Fase 0).
Muestra el flujo completo: generación → transporte →
distribución → consumo, con el MEM y CAMMESA, y dónde
se conectan los grandes usuarios como las minas.

Próximos diagramas de la Fase 0:
  - Mapa institucional San Juan vs. Nación
  - Matriz de generación de San Juan corregida (861 MW)
  - Curva de pato (por qué la solar no resuelve demanda 24/7)
""")
