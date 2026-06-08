"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 00e: Mapa geográfico — el problema es también espacial
=============================================================
Objetivo (capa accesible / Fase 0 — geografía):
  Hacer VISIBLE el argumento central que hasta ahora estaba solo en
  texto: la generación y el consumo están en el valle central/este de
  San Juan, mientras los proyectos mineros están en la cordillera
  occidental (250–410 km al oeste, pegados al límite con Chile),
  conectados por una línea de transmisión insuficiente.

  Esto explica por qué tener 861 MW instalados NO resuelve el problema:
  esa generación está en el lugar equivocado respecto de las minas.

⚠ HONESTIDAD DEL DATO:
  - Los Azules: coordenadas de ficha técnica pública (31°06'27"S, 70°13'10"O).
  - Josemaría, Filo del Sol, El Pachón: posicionados según descripciones
    públicas (departamento, distancia a capital, distancia a Chile, altitud).
  - Centrales hidro, parques solares y trazas de líneas: posición REFERENCIAL.
  - Mapa esquemático georreferenciado, NO a escala topográfica exacta.

Fuentes de ubicación: fichas técnicas y notas públicas (sisanjuan.gob.ar,
  nuevamineria.com, McEwen Copper, Revista Nueva Minería, aceroyroca.com).

Genera: reports/00_05_mapa_geografico.png
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import os

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':   'DejaVu Sans',
    'font.size':     10,
    'figure.dpi':    150,
})

# Paleta (consistente con el proyecto)
C_MINA   = '#C0392B'   # proyectos mineros
C_HIDRO  = '#4A90D9'   # centrales hidro
C_SOLAR  = '#F1C40F'   # parques solares
C_DEM    = '#2C3E50'   # demanda (Gran San Juan)
C_TOWN   = '#95A5A6'   # localidades de referencia
C_LINEA  = '#34495E'   # línea de transmisión existente
C_FALTA  = '#C0392B'   # tramos insuficientes
C_CORD   = '#D7CCC8'   # cordillera (oeste)
C_VALLE  = '#E8F6F3'   # valle central (este)

# ------------------------------------------------------------
# DATOS GEOGRÁFICOS (lon, lat) — ubicaciones aproximadas
# ------------------------------------------------------------
# Proyectos mineros (cordillera occidental)
minas = [
    ('Josemaría',    -69.83, -29.78, '410 km de la capital · 10 km de Chile'),
    ('Filo del Sol', -69.98, -29.62, 'parte del Proyecto Vicuña'),
    ('Los Azules',   -70.22, -31.11, '250 km al O · 3 km de Chile · 31°06\u2032S'),
    ('El Pachón',    -70.42, -31.76, '363 km de la capital · límite con Chile'),
]

# Centrales hidroeléctricas (sobre el Río San Juan, valle central)
hidros = [
    ('Embalse Ullum', -68.67, -31.45),
    ('Los Caracoles', -69.05, -31.57),
    ('Punta Negra',   -68.98, -31.73),
    ('El Tambolar',   -69.18, -31.47),
]

# Parques solares (valle central y sur — posición referencial)
solares = [
    ('Cañada Honda', -68.50, -31.98),
    ('Ullum solar',  -68.72, -31.40),
    ('Caucete',      -68.25, -31.65),
]

# Demanda concentrada
gran_sj = ('Gran San Juan', -68.54, -31.54)

# Localidades de referencia
towns = [
    ('Capital',    -68.54, -31.54),
    ('Calingasta', -69.42, -31.34),
    ('Barreal',    -69.47, -31.63),
    ('Rodeo',      -69.14, -30.21),
    ('Jáchal',     -68.75, -30.24),
]

fig, ax = plt.subplots(figsize=(12, 13))

# ------------------------------------------------------------
# ZONAS (contexto geográfico, esquemático)
# ------------------------------------------------------------
# Cordillera occidental (donde están las minas)
ax.axvspan(-70.7, -69.55, color=C_CORD, alpha=0.55, zorder=0)
ax.text(-70.62, -28.74, 'CORDILLERA DE LOS ANDES\n(límite con Chile · donde están las minas)',
        ha='left', va='top', fontsize=9, color='#6D4C41', fontweight='bold', style='italic')

# Valle central / este (donde están generación y consumo)
ax.axvspan(-69.0, -67.9, color=C_VALLE, alpha=0.7, zorder=0)
ax.text(-68.05, -28.74, 'VALLE CENTRAL / ESTE\n(generación + consumo)',
        ha='right', va='top', fontsize=9, color='#117A65', fontweight='bold', style='italic')

# ------------------------------------------------------------
# LÍNEAS DE TRANSMISIÓN (trazas referenciales)
# ------------------------------------------------------------
# Existente: Gran San Juan → Jáchal → Rodeo (línea 500 kV operando a 132 kV)
ax.plot([-68.54, -68.75, -69.14], [-31.54, -30.24, -30.21],
        color=C_LINEA, lw=2.5, zorder=3, solid_capstyle='round')
# Existente: Gran San Juan → Calingasta
ax.plot([-68.54, -69.42], [-31.54, -31.34],
        color=C_LINEA, lw=2.5, zorder=3, solid_capstyle='round')

# Tramos INSUFICIENTES hacia las minas (dashed rojo)
ax.plot([-69.14, -69.83], [-30.21, -29.78], color=C_FALTA, lw=2, ls=(0, (5, 3)), zorder=3)  # Rodeo→Josemaría
ax.plot([-69.42, -70.22], [-31.34, -31.11], color=C_FALTA, lw=2, ls=(0, (5, 3)), zorder=3)  # Calingasta→Los Azules
ax.plot([-70.22, -70.42], [-31.11, -31.76], color=C_FALTA, lw=2, ls=(0, (5, 3)), zorder=3)  # Los Azules→El Pachón

ax.text(-69.5, -30.0, 'línea SJ–Rodeo\n500 kV (opera a 132 kV)',
        ha='left', va='center', fontsize=8, color=C_LINEA, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_LINEA, alpha=0.85, boxstyle='round,pad=0.25', linewidth=0.8))
ax.text(-69.88, -30.90, 'tramos sin capacidad\nsuficiente para\nla demanda minera',
        ha='center', va='center', fontsize=8, color=C_FALTA, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_FALTA, alpha=0.9, boxstyle='round,pad=0.3', linewidth=0.8))

# ------------------------------------------------------------
# MARCADORES
# ------------------------------------------------------------
# Localidades de referencia (gris, debajo de todo)
for nombre, lon, lat in towns:
    if nombre == 'Capital':
        continue  # Capital se muestra como Gran San Juan
    ax.scatter(lon, lat, s=35, c=C_TOWN, marker='o', zorder=4, edgecolors='white', linewidths=0.8)
    ax.text(lon, lat - 0.07, nombre, ha='center', va='top', fontsize=8, color='#7F8C8D')

# Parques solares (amarillo)
for nombre, lon, lat in solares:
    ax.scatter(lon, lat, s=110, c=C_SOLAR, marker='o', zorder=5, edgecolors='#B7950B', linewidths=1.2)

# Centrales hidro (azul, triángulo)
for nombre, lon, lat in hidros:
    ax.scatter(lon, lat, s=130, c=C_HIDRO, marker='^', zorder=5, edgecolors='white', linewidths=1.2)

# Gran San Juan — demanda (estrella oscura, grande)
ax.scatter(gran_sj[1], gran_sj[2], s=480, c=C_DEM, marker='*', zorder=7, edgecolors='white', linewidths=1.5)
ax.text(gran_sj[1] + 0.06, gran_sj[2], 'GRAN SAN JUAN\n(demanda: ~551 MW pico)',
        ha='left', va='center', fontsize=9.5, color=C_DEM, fontweight='bold')

# Proyectos mineros (rojo, diamante) + etiquetas con distancia
# Layout por mina para evitar solapamientos: name=(dx,dy,ha), nota=(dx,dy,ha)
lay_minas = {
    'Josemaría':    ((0.06,  0.02, 'left'),   (0.0,  -0.13, 'center')),
    'Filo del Sol': ((0.0,   0.13, 'center'), (-0.06, 0.02, 'right')),
    'Los Azules':   ((-0.07, 0.04, 'right'),  (0.0,  -0.13, 'center')),
    'El Pachón':    ((0.0,   0.13, 'center'), (0.0,  -0.13, 'center')),
}
for nombre, lon, lat, nota in minas:
    ax.scatter(lon, lat, s=200, c=C_MINA, marker='D', zorder=6, edgecolors='white', linewidths=1.3)
    (ndx, ndy, nha), (tdx, tdy, tha) = lay_minas[nombre]
    ax.text(lon + ndx, lat + ndy, nombre, ha=nha, va='center', fontsize=9.5, color=C_MINA, fontweight='bold')
    ax.text(lon + tdx, lat + tdy, nota, ha=tha, va='center', fontsize=6.8, color='#A93226', style='italic')

# ------------------------------------------------------------
# FLECHA DE SEPARACIÓN (el mensaje central)
# ------------------------------------------------------------
ax.annotate('', xy=(-70.0, -32.25), xytext=(-68.5, -32.25),
            arrowprops=dict(arrowstyle='<->', color='#566573', lw=1.8))
ax.text(-69.25, -32.33, '≈ 250–410 km de separación',
        ha='center', va='top', fontsize=9, color='#566573', fontweight='bold')

# ------------------------------------------------------------
# FORMATO
# ------------------------------------------------------------
ax.set_xlim(-70.7, -67.9)
ax.set_ylim(-32.5, -28.55)
ax.set_xlabel('Longitud Oeste  ←  (oeste a la izquierda)', fontsize=10)
ax.set_ylabel('Latitud Sur', fontsize=10)
ax.set_aspect(1.15)  # corrección aproximada lat/lon a esta latitud
ax.grid(alpha=0.15, zorder=0)

ax.set_title('San Juan — la brecha también es geográfica',
             fontsize=15, fontweight='bold', pad=22)
ax.text(0.5, 1.04,
        'La generación (861 MW) y el consumo están en el valle central/este · las minas están en la cordillera occidental, '
        '250–410 km al oeste',
        transform=ax.transAxes, ha='center', va='bottom', fontsize=9.5, color='#566573', style='italic')

# Leyenda
leg = [
    Line2D([0], [0], marker='D', color='w', markerfacecolor=C_MINA, markersize=11, label='Proyecto minero (demanda futura)'),
    Line2D([0], [0], marker='*', color='w', markerfacecolor=C_DEM, markersize=16, label='Gran San Juan (demanda actual)'),
    Line2D([0], [0], marker='^', color='w', markerfacecolor=C_HIDRO, markersize=11, label='Central hidroeléctrica'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=C_SOLAR, markersize=11, label='Parque solar (referencial)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=C_TOWN, markersize=8, label='Localidad de referencia'),
    Line2D([0], [0], color=C_LINEA, lw=2.5, label='Transmisión existente'),
    Line2D([0], [0], color=C_FALTA, lw=2, ls='--', label='Tramo insuficiente para minería'),
]
ax.legend(handles=leg, loc='lower right', fontsize=8, framealpha=0.92, edgecolor='#D5DBDB')

# Disclaimer de honestidad
fig.text(0.5, 0.055,
         'Ubicaciones APROXIMADAS. Los Azules: coordenadas de ficha técnica (31°06\u203227\u2033S, 70°13\u203210\u2033O). '
         'Josemaría, Filo del Sol y El Pachón: posicionados según descripciones públicas\n(departamento, distancia a capital y a Chile, altitud). '
         'Centrales hidro, parques solares y trazas de líneas: posición referencial. Mapa esquemático georreferenciado, no a escala topográfica.',
         ha='center', va='top', fontsize=7, color='#95A5A6', style='italic')

plt.tight_layout(rect=[0, 0.07, 1, 1])
ruta = f'{REPORTS_DIR}/00_05_mapa_geografico.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()

print("=" * 60)
print("SCRIPT 00e — MAPA GEOGRÁFICO SAN JUAN")
print("=" * 60)
print(f"""
✓ Guardado: {ruta}

  Hace visible el argumento espacial central:
    - Generación + demanda: valle central/este (lon ~-68.5)
    - Minas: cordillera occidental (lon -69.8 a -70.4), 250-410 km
    - Conectadas por la línea SJ–Rodeo (500 kV diseñada, opera a 132 kV)

  Por qué importa: explica por qué 861 MW instalados NO resuelven
  el problema — esa generación está en el lugar equivocado respecto
  de las minas. Substancia lo que antes era solo afirmación de texto.

  Honestamente etiquetado: Los Azules con coordenadas de ficha técnica;
  resto posicionado por descripciones públicas; trazas referenciales.
""")
