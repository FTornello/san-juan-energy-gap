"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 00b: Mapa institucional — San Juan vs. Nación
=====================================================
Objetivo (capa accesible / Fase 0):
  Aclarar quién hace qué en el sistema eléctrico, separando
  el ámbito NACIONAL del PROVINCIAL. Responde la pregunta:
  ¿generación y distribución son compartidas o autónomas?

  Mensajes clave:
    - La generación está físicamente en San Juan pero VENDE
      al mercado nacional (MEM). No está reservada para la provincia.
    - La distribución SÍ es provincial: compra del MEM nacional
      y entrega localmente.
    - La regulación está partida: ENRE (nacional, transporte +
      mercado) vs. EPRE (provincial, distribución).
    - La minería se conecta DIRECTO a la transmisión nacional,
      salteando el nivel provincial.
    - Por eso el conflicto por la línea 500 kV lo define ENRE
      (jurisdicción nacional), no la provincia.

Genera: reports/00_02_mapa_institucional.png
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'figure.dpi':  150,
})

# Paleta
C_NACION   = '#34495E'   # ámbito nacional (slate)
C_PROV     = '#16A085'   # ámbito provincial (teal)
C_ENRE     = '#2C3E50'   # regulador nacional
C_CAMMESA  = '#566573'   # operador
C_GRID     = '#1F618D'   # SADI + MEM
C_EPSE     = '#2980B9'   # empresa estatal provincial
C_SOLAR    = '#F1C40F'   # generación solar
C_HIDRO    = '#4A90D9'   # generación hidro
C_DIST     = '#5D8AA8'   # distribuidoras
C_EPRE     = '#117A65'   # regulador provincial
C_USER     = '#95A5A6'   # consumo
C_MINA     = '#C0392B'   # minería / grandes usuarios

fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def caja(x, y, w, h, texto, color, fc_text='white', fontsize=9.5, weight='bold', alpha=0.92, z=4):
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle='round,pad=0.3,rounding_size=1',
        facecolor=color, edgecolor='white', linewidth=1.5, alpha=alpha, zorder=z
    )
    ax.add_patch(box)
    ax.text(x, y, texto, ha='center', va='center',
            fontsize=fontsize, fontweight=weight, color=fc_text, zorder=z+1)


def zona(x, y, w, h, color):
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle='round,pad=0.5,rounding_size=2',
        facecolor=color, edgecolor=color, linewidth=2, alpha=0.10, zorder=1
    )
    ax.add_patch(box)


def flecha(x1, y1, x2, y2, color, lw=2.4, ls='-', rad=0.0):
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='-|>', mutation_scale=22,
        color=color, lw=lw, linestyle=ls, zorder=3,
        shrinkA=3, shrinkB=3,
        connectionstyle=f'arc3,rad={rad}'
    )
    ax.add_patch(arr)


# ============================================================
# TÍTULO
# ============================================================
ax.text(50, 96.5, 'Quién hace qué: San Juan dentro del sistema nacional',
        ha='center', va='center', fontsize=17, fontweight='bold', color='#2C3E50')
ax.text(50, 92, 'La generación es de mercado nacional · la distribución es provincial · la minería se conecta directo a la red nacional',
        ha='center', va='center', fontsize=10, color='#7F8C8D', style='italic')


# ============================================================
# ZONA NACIONAL (banda superior)
# ============================================================
zona(50, 73, 92, 26, C_NACION)
ax.text(9, 84, 'ÁMBITO NACIONAL', ha='left', va='center',
        fontsize=12, fontweight='bold', color=C_NACION)

# SADI + MEM (centro, lo más grande)
caja(50, 73, 30, 13,
     'SADI  +  MEM\n\nRed nacional de transporte\n+ mercado mayorista\n(donde se vende y compra)',
     C_GRID, fontsize=9.5)

# CAMMESA (opera)
caja(82, 76, 20, 8, 'CAMMESA\nopera y despacha\nel sistema', C_CAMMESA, fontsize=9)

# ENRE (regula)
caja(82, 66, 20, 8, 'ENRE\nregulador nacional\n(transporte + mercado)', C_ENRE, fontsize=8.5)

# Vínculos internos nación
flecha(72, 75, 75, 76, C_CAMMESA, lw=1.6, rad=0.1)
flecha(72, 70, 75, 67, C_ENRE, lw=1.6, rad=-0.1)


# ============================================================
# ZONA PROVINCIAL (banda inferior)
# ============================================================
zona(50, 38, 92, 28, C_PROV)
ax.text(9, 50.5, 'ÁMBITO PROVINCIAL — SAN JUAN', ha='left', va='center',
        fontsize=12, fontweight='bold', color=C_PROV)

# --- Grupo 1: Generación en San Juan (izquierda) ---
ax.text(22, 47, 'Generación en San Juan', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='#2C3E50')
caja(15, 40, 13, 7, 'Parques\nsolares\n(privados)', C_SOLAR, fc_text='#2C3E50', fontsize=8.5)
caja(29, 40, 13, 7, 'EPSE\n(estatal):\nhidro + solar', C_EPSE, fontsize=8.5)
ax.text(22, 33.5, '861 MW instalados\n(70% solar · 27% hidro · 3% térmica)',
        ha='center', va='center', fontsize=7.5, color='#566573', style='italic')

# --- Grupo 2: Distribución (centro) ---
ax.text(52, 47, 'Distribución', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='#2C3E50')
caja(52, 40, 16, 8, 'Energía San Juan S.A.\n+ DECSA (Caucete)\n\ncompran del MEM\ny entregan local', C_DIST, fontsize=8)

# --- Grupo 3: Regulador provincial (derecha) ---
ax.text(80, 47, 'Regulador provincial', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='#2C3E50')
caja(80, 40, 16, 8, 'EPRE\nregula la\ndistribución\nprovincial', C_EPRE, fontsize=8.5)


# ============================================================
# FLUJOS ENTRE ÁMBITOS
# ============================================================
# Generación VENDE hacia arriba (al MEM nacional)
flecha(22, 43.5, 40, 67, C_PROV, lw=2.6, rad=0.15)
ax.text(26, 57, 'genera y VENDE\nal mercado nacional',
        ha='center', va='center', fontsize=8, color=C_PROV, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_PROV, alpha=0.85, boxstyle='round,pad=0.25', linewidth=0.8))

# Distribución COMPRA desde arriba (del MEM nacional)
flecha(56, 67, 54, 44, C_GRID, lw=2.6, rad=0.15)
ax.text(68, 57, 'COMPRA energía\ndel mercado nacional',
        ha='center', va='center', fontsize=8, color=C_GRID, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_GRID, alpha=0.85, boxstyle='round,pad=0.25', linewidth=0.8))


# ============================================================
# CONSUMO PROVINCIAL (debajo de la zona provincial)
# ============================================================
caja(52, 19, 30, 6, 'Consumo provincial:  hogares · comercios · industria',
     C_USER, fontsize=9)
flecha(52, 36, 52, 22.2, C_DIST, lw=2.4)
ax.text(60, 28.5, 'entrega local', ha='center', va='center',
        fontsize=7.5, color=C_DIST, style='italic')


# ============================================================
# MINERÍA — fuera de ambos ámbitos: conecta DIRECTO a la red nacional
# Un Gran Usuario no es generación ni distribución provincial:
# se conecta al transporte nacional. Por eso va por fuera de las zonas,
# al lado del consumo provincial pero claramente separado.
# ============================================================
caja(84, 18, 24, 9, 'Minería\n(Gran Usuario)', C_MINA, fontsize=9.5)
# Flecha que sube por el corredor vacío entre Distribución (x~52) y EPRE (x~80)
arr = FancyArrowPatch(
    (73, 22), (58, 66),
    arrowstyle='<|-|>', mutation_scale=20,
    color=C_MINA, lw=2.6, linestyle='--', zorder=3,
    shrinkA=6, shrinkB=6,
    connectionstyle='arc3,rad=-0.08'
)
ax.add_patch(arr)
ax.text(87, 30, 'se conecta DIRECTO\na la red nacional\n(saltea lo provincial)',
        ha='center', va='center', fontsize=7.5, color=C_MINA, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_MINA, alpha=0.9, boxstyle='round,pad=0.3', linewidth=0.8))


# ============================================================
# CALLOUT — la clave jurisdiccional (conecta con el caso 500 kV)
# ============================================================
ax.text(50, 7,
        '⚖  La transmisión de alta tensión es jurisdicción NACIONAL (ENRE). Por eso el conflicto por la línea 500 kV lo resuelve ENRE,\n'
        'no la provincia — aunque EPRE San Juan fue uno de los 8 actores que se opusieron. La provincia regula la distribución, no el transporte.',
        ha='center', va='center', fontsize=8.5, color='#2C3E50',
        bbox=dict(facecolor='#FEF9E7', edgecolor='#D4AC0D', alpha=0.95, boxstyle='round,pad=0.5', linewidth=1.5))


plt.tight_layout()
ruta = f'{REPORTS_DIR}/00_02_mapa_institucional.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()

print("=" * 60)
print("SCRIPT 00b — MAPA INSTITUCIONAL SAN JUAN vs. NACIÓN")
print("=" * 60)
print(f"\n✓ Guardado: {ruta}")
print("""
Segundo diagrama de la capa accesible (Fase 0).
Aclara la separación nacional/provincial:
  - Generación en SJ → vende al MEM nacional
  - Distribución provincial → compra del MEM
  - Regulación partida: ENRE (nación) vs. EPRE (provincia)
  - Minería → directo a transmisión nacional
  - Conecta con el caso 500 kV: lo define ENRE, no la provincia

Próximos diagramas de la Fase 0:
  - Matriz de generación de San Juan corregida (861 MW)
  - Curva de pato (por qué la solar no resuelve demanda 24/7)
""")
