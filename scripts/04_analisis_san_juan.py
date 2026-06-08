"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 04: San Juan — datos reales + gap analysis
==================================================
Objetivo:
  - Explorar los datos del CSV de CAMMESA filtrados para San Juan / CUYO
  - Entender qué grandes usuarios industriales hay en San Juan según el MEM
  - Construir el gráfico central del proyecto: el gap analysis
    (infraestructura actual vs. demanda minera proyectada)

Fuentes de datos:
  - data/raw/potencia_instalada_raw.csv → región CUYO, plantas identificables
  - data/raw/demanda_raw.csv → provincia SAN JUAN (Grandes Usuarios)
  - Datos auditados de investigación (para proyecciones mineras):
      Josemaría:  260 MW (ENRE Res. 79/2026, BHP+Lundin/Vicuña)
      Los Azules: 119 MW (McEwen Copper FS nov. 2025)
      El Pachón:  ~600 MW estimado (benchmark 185 kt/día, factibilidad no publicada)
      Clúster total: >1.500 MW (CEO Glencore Argentina, mayo 2026)
      Capacidad línea ET Nueva SJ → Rodeo (132kV actual): ~90 MW
      Demanda provincial pico actual: ~551 MW (EPRE 2021)
      Generación provincial instalada: 861 MW (EPSE feb. 2025; 70% solar, ~258 MW firmes)

Nota sobre los CSV: cubren 2015-2020 y la región CUYO (no provincia).
Los datos de 2020-2026 y las proyecciones vienen de la auditoría de fuentes.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import os
from datetime import datetime

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':   'DejaVu Sans',
    'font.size':     11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.spines.top':    False,
    'axes.spines.right':  False,
    'figure.dpi':    150,
})

print("=" * 60)
print("SCRIPT 04 — ANÁLISIS SAN JUAN + GAP ANALYSIS")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")


# ============================================================
# PARTE A: LO QUE DICEN LOS DATOS DEL CSV SOBRE SAN JUAN
# ============================================================
print("=" * 60)
print("PARTE A — DATOS CSV: SAN JUAN / CUYO (2015–2020)")
print("=" * 60 + "\n")

# --- A1: Potencia instalada en CUYO ---
print("--- A1: Potencia instalada región CUYO ---\n")

df_pot_raw = pd.read_csv('data/raw/potencia_instalada_raw.csv')

# Filtrar CUYO
df_cuyo = df_pot_raw[df_pot_raw['region'] == 'CUYO'].copy()
print(f"Registros en CUYO: {len(df_cuyo):,}")
print(f"Años disponibles:  {sorted(df_cuyo['anio'].unique())}")
print(f"Tecnologías en CUYO:\n")

# Potencia total por tecnología en el último año disponible (2020)
df_cuyo_2020 = df_cuyo[df_cuyo['anio'] == 2020]
resumen_cuyo = (
    df_cuyo_2020
    .groupby('fuente_generacion')['potencia_instalada_mw']
    .sum()
    .sort_values(ascending=False)
)
for tec, mw in resumen_cuyo.items():
    print(f"  {tec:<20} {mw:>8,.1f} MW")
print(f"\n  TOTAL CUYO 2020: {resumen_cuyo.sum():,.1f} MW\n")

# Plantas identificables en San Juan (por nombre)
# Criterio: centrales conocidas de San Juan (Ullum, Villicum, Tocota, Guañizuil, etc.)
palabras_sj = ['ULLUM', 'VILLICUM', 'TOCOTA', 'GUAÑIZUIL', 'SOLARPACK', 'CALMAYO',
               'PISMANTA', 'CUESTA', 'VIENTO', 'SOLAR SJ', 'SOLARSJ', 'LOMA']
df_sj_aprox = df_cuyo[
    df_cuyo['central'].str.upper().str.contains('|'.join(palabras_sj), na=False) |
    df_cuyo['agente_descripcion'].str.upper().str.contains('SAN JUAN|SANJUAN', na=False)
]
if len(df_sj_aprox) > 0:
    print("Centrales probablemente sanjuaninas en el dataset:")
    print(df_sj_aprox[['central', 'agente_descripcion', 'tecnologia',
                        'potencia_instalada_mw', 'anio']]
          .drop_duplicates(subset=['central'])
          .sort_values('potencia_instalada_mw', ascending=False)
          .to_string(index=False))
else:
    print("  (No se identificaron centrales sanjuaninas por nombre en el subset disponible)")
print()

# --- A2: Grandes usuarios en San Juan ---
print("--- A2: Grandes usuarios industriales en San Juan (CSV) ---\n")

df_dem_raw = pd.read_csv('data/raw/demanda_raw.csv')

# Verificar valores únicos de provincia para encontrar San Juan
print(f"Valores únicos de 'provincia':")
print(f"  {sorted(df_dem_raw['provincia'].unique())}\n")

# Filtrar San Juan
df_sj_dem = df_dem_raw[df_dem_raw['provincia'] == 'SAN JUAN'].copy()

if len(df_sj_dem) > 0:
    print(f"Registros San Juan en demanda: {len(df_sj_dem):,}")
    print(f"Años:    {sorted(df_sj_dem['anio'].unique())}")
    print(f"Agentes: {df_sj_dem['agente_nemo'].nunique()} usuarios únicos\n")

    # Top usuarios por demanda anual total
    resumen_sj = (
        df_sj_dem
        .groupby(['agente_nemo', 'agente_descripcion'])['demanda_MWh']
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )
    print("Top 15 grandes usuarios (demanda total 2017–2020):")
    print(f"\n  {'Nemo':<12} {'Descripción':<45} {'MWh total':>12}")
    print("  " + "-" * 72)
    for _, row in resumen_sj.iterrows():
        print(f"  {row['agente_nemo']:<12} {row['agente_descripcion']:<45} {row['demanda_MWh']:>12,.0f}")

    # Demanda anual total de San Juan (GUM)
    dem_anual_sj = (
        df_sj_dem
        .groupby('anio')['demanda_MWh']
        .sum()
        .reset_index()
    )
    print(f"\nDemanda GUM San Juan por año:")
    for _, row in dem_anual_sj.iterrows():
        print(f"  {int(row['anio'])}: {row['demanda_MWh']/1000:,.1f} GWh")
else:
    print("  No se encontró 'SAN JUAN' — revisando variantes...")
    variantes = [p for p in df_dem_raw['provincia'].unique() if 'JUAN' in p.upper()]
    print(f"  Variantes encontradas: {variantes}")

print()


# ============================================================
# PARTE B: GAP ANALYSIS — EL GRÁFICO CENTRAL DEL PROYECTO
# ============================================================
print("=" * 60)
print("PARTE B — GAP ANALYSIS: INFRAESTRUCTURA vs. DEMANDA")
print("=" * 60 + "\n")

# ============================================================
# DATOS AUDITADOS — valores con fuente documentada
# ============================================================

# --- OFERTA / INFRAESTRUCTURA (contexto) ---
# El problema NO es falta de generación: San Juan tiene 861 MW instalados
# (EPSE feb. 2025) y es exportador neto al mediodía. El problema es doble:
#   (1) la mayoría es solar variable; solo ~258 MW son firmes (hidro + térmica), y
#   (2) la transmisión al norte minero (Iglesia/Calingasta) es de solo ~90 MW.
# Además, la generación provincial está en el centro/sur, lejos de las minas.
generacion_instalada = 861   # MW — EPSE feb. 2025 (70% solar · 27% hidro · 3% térmica)
capacidad_firme      = 258   # MW — hidro + térmica (despachable 24/7)
transmision_norte    = 90    # MW — línea 132kV ET Nueva San Juan → Rodeo (cuello de botella)

# --- DEMANDA: situación actual ---
# Fuente: EPRE San Juan — Anuario 2021 (última serie completa disponible)
# Potencia Operada máxima registrada en el sistema interconectado provincial:
#   San Juan SA (distribuidor): 507.50 MW
#   DECSA (Caucete):             21.15 MW
#   Grandes Usuarios MEM:        23.87 MW
#   TOTAL 2021:                 551.51 MW
# Nota: el dato anterior de 280 MW provenía de un artículo de prensa
# y estaba desactualizado. El dato corregido es de la fuente regulatoria oficial.
demanda_actual = 551  # MW — Potencia Operada máxima 2021, EPRE San Juan

# --- DEMANDA: proyecciones mineras ---
# (fuente y año de inicio de demanda documentados)
proyectos = [
    {
        'nombre':   'Josemaría\n(BHP + Lundin / Vicuña)',
        'mw':       260,
        'inicio':   '2027–2028',
        'fuente':   'ENRE Res. 79/2026',
        'color':    '#C0392B',
        'etapa':    'En construcción'
    },
    {
        'nombre':   'Los Azules\n(McEwen Copper)',
        'mw':       119,
        'inicio':   '2029–2030',
        'fuente':   'McEwen FS nov.2025',
        'color':    '#E67E22',
        'etapa':    'Factibilidad aprobada'
    },
    {
        'nombre':   'El Pachón\n(Glencore, est.)',
        'mw':       600,
        'inicio':   '2034+',
        'fuente':   'Benchmark: 185 kt/día a 3.600–4.200 msnm\n(factibilidad no publicada)',
        'color':    '#8E44AD',
        'etapa':    'Factibilidad en curso'
    },
]

total_minero = sum(p['mw'] for p in proyectos)
demanda_futura_benchmark = demanda_actual + total_minero  # base conservadora

# CEO Glencore Argentina confirmó >1.500 MW para el clúster completo (Expo Minera SJ, mayo 2026)
# Usado en el escenario final del gap analysis — fuente directa más confiable que el residual
total_minero_ceo = 1500
demanda_futura = demanda_actual + total_minero_ceo  # 2051 MW

print(f"  Demanda provincial actual (pico):   {demanda_actual:>6} MW")
print(f"  Generación provincial instalada:    {generacion_instalada:>6} MW (EPSE 2025, mayormente solar)")
print(f"  Capacidad firme (hidro + térmica):  {capacidad_firme:>6} MW")
print(f"  Transmisión al norte minero (132kV):{transmision_norte:>6} MW (cuello de botella)")
print(f"  Josemaría Fase 1:                   {proyectos[0]['mw']:>6} MW")
print(f"  Los Azules:                         {proyectos[1]['mw']:>6} MW")
print(f"  El Pachón (estimado benchmark):     {proyectos[2]['mw']:>6} MW")
print(f"  ─────────────────────────────────────────")
print(f"  Suma 3 proyectos nombrados (est.):  {total_minero:>6} MW")
print(f"  Clúster total (CEO Glencore):       >{total_minero_ceo:>5} MW  (incluye Filo del Sol + expansiones)")
print(f"  DEMANDA TOTAL FUTURA (prov.+clúster): {demanda_futura:>5} MW")
print(f"  BRECHA vs. línea 132kV actual:     {demanda_futura - 90:>6} MW\n")


# ============================================================
# GRÁFICO CENTRAL — gap analysis (v2, diseño reformulado)
# ============================================================
# Fusionado desde 04_fix_gap_chart.py.
# Decisión de diseño: comparar directamente DEMANDA del clúster vs.
# CAPACIDAD con plan — misma naturaleza, mismo eje.

print("--- Generando gráfico central (v2 — máxima claridad) ---")

# ---- Datos / aliases ----
josemaria          = proyectos[0]['mw']                              # 260 MW — DATO ENRE 79/2026
los_azules         = proyectos[1]['mw']                              # 119 MW — DATO McEwen NI 43-101
el_pachon          = proyectos[2]['mw']                              # 600 MW — ESTIMACIÓN benchmark
cluster_ceo        = total_minero_ceo                                # 1500 MW — CEO Glencore
filo_exp           = cluster_ceo - josemaria - los_azules - el_pachon   # 521 MW (residual)
capacidad_con_plan = josemaria                                       # 260 MW — ENRE Res. 214/2026
brecha_sin_plan    = cluster_ceo - capacidad_con_plan                # 1240 MW

plt.rcParams.update({'axes.spines.left': False})

segmentos = [
    ('Josemaría',                josemaria,  '#E67E22'),
    ('Los Azules',               los_azules, '#D35400'),
    ('El Pachón',                el_pachon,  '#A569BD'),
    ('Filo del Sol+expansiones', filo_exp,   '#BDC3C7'),
]

fig, ax = plt.subplots(figsize=(14, 7.8))
Y_DEM = 1.0
Y_CAP = 0.0
H = 0.46

# ---- Barra de DEMANDA del clúster (apilada) ----
x0 = 0
for nombre, val, color in segmentos:
    ax.barh(Y_DEM, val, left=x0, height=H, color=color, alpha=0.92,
            edgecolor='white', linewidth=1.6, zorder=3)
    txt_color = '#2C3E50' if color == '#BDC3C7' else color
    label = nombre + '\n' + f'{val:,.0f} MW'   # solo magnitud — el timing lo cuenta el 07
    ax.text(x0 + val/2, Y_DEM + H/2 + 0.05, label,
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=txt_color)
    x0 += val
ax.text(cluster_ceo + 22, Y_DEM, f'>{cluster_ceo:,.0f} MW',
        va='center', ha='left', fontsize=11.5, fontweight='bold', color='#2C3E50')

# ---- Barra de CAPACIDAD con plan ----
ax.barh(Y_CAP, capacidad_con_plan, height=H, color='#16A085', alpha=0.95,
        edgecolor='white', linewidth=1.6, zorder=3)
ax.text(capacidad_con_plan + 22, Y_CAP, f'{capacidad_con_plan:,.0f} MW',
        va='center', ha='left', fontsize=11.5, fontweight='bold', color='#0E6655')

# Etiquetas de categoría
ax.text(-22, Y_DEM, 'DEMANDA del' + '\n' + 'cluster minero',
        va='center', ha='right', fontsize=10.5, fontweight='bold', color='#2C3E50')
ax.text(-22, Y_CAP, 'CAPACIDAD con' + '\n' + 'plan (en disputa)',
        va='center', ha='right', fontsize=10.5, fontweight='bold', color='#0E6655')

# ---- Línea vertical en 260 ----
ax.plot([capacidad_con_plan, capacidad_con_plan],
        [Y_CAP - H/2 - 0.06, Y_DEM + H/2 + 0.06],
        color='#16A085', lw=2, linestyle='--', zorder=4)
linea_lbl = 'la capacidad con plan llega' + '\n' + 'exactamente hasta aca' + '\n' + '(cubre solo Josemaria)'
ax.text(capacidad_con_plan, Y_DEM + H/2 + 0.40, linea_lbl,
        ha='center', va='bottom', fontsize=8, color='#0E6655', fontweight='bold')

# ---- Flecha doble: brecha ----
ax.annotate('', xy=(capacidad_con_plan, 0.5), xytext=(cluster_ceo, 0.5),
            arrowprops=dict(arrowstyle='<->', color='#C0392B', lw=1.8))
brecha_lbl = (f'~{brecha_sin_plan:,.0f} MW del clúster SIN plan de transporte'
              + '\n' + '(Los Azules + El Pachón + Filo del Sol + expansiones)')
ax.text((capacidad_con_plan + cluster_ceo) / 2, 0.40, brecha_lbl,
        ha='center', va='top', fontsize=9.5, color='#C0392B', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#FDEDEC',
                  edgecolor='#C0392B', alpha=0.95, linewidth=1.2))

# ---- Nota de contexto ----
nota_ctx = ('Esta demanda minera se SUMA a los ~551 MW de pico provincial (EPRE 2021). '
            'La línea San Juan–Rodeo existe como 500 kV pero opera a 132 kV; '
            'energizarla a 500 kV es lo que se disputa en ENRE 79/2026.')
ax.text(0.5, -0.13, nota_ctx, transform=ax.transAxes, ha='center', va='top',
        fontsize=8.3, color='#566573', style='italic')

fuentes = ('Josemaría 260 MW — ENRE Res. 79/2026  |  '
           'Los Azules — McEwen Copper NI 43-101  |  '
           'El Pachón ~600 MW — estimación por benchmark  |  '
           'Clúster >1.500 MW — CEO Glencore Argentina, Expo Minera SJ, mayo 2026')
ax.text(0.5, -0.22, fuentes, transform=ax.transAxes, ha='center', va='top',
        fontsize=7.2, color='#7F8C8D', style='italic')

# Formato
ax.set_yticks([])
ax.set_xlabel('Megawatts (MW)', fontsize=11)
ax.set_xlim(-360, cluster_ceo + 240)
ax.set_ylim(-0.85, 2.05)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}' if x >= 0 else ''))
ax.set_title('San Juan — La capacidad con plan cubre solo el primer proyecto del cluster',
             fontsize=13, fontweight='bold', pad=16)
ax.tick_params(left=False)
plt.tight_layout(rect=[0, 0.06, 1, 1])

ruta = f'{REPORTS_DIR}/04_01_gap_analysis_san_juan.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()
print(f'  Guardado: {ruta}')


# ============================================================
# GRÁFICO 2 — Proporción: demanda minera vs. demanda provincial
# ============================================================
print("--- Generando gráfico de proporciones ---")

fig, ax = plt.subplots(figsize=(10, 5))

categorias = ['Demanda\nprovincial\nactual', 'Josemaría\nFase 1', 'Los Azules', 'El Pachón\n(~600 MW est.*)']
valores    = [demanda_actual, 260, 119, 600]
colores    = ['#3498DB', '#E74C3C', '#E67E22', '#8E44AD']

barras = ax.bar(categorias, valores, color=colores, width=0.55,
                edgecolor='white', linewidth=1.5, alpha=0.9)

for barra, val in zip(barras, valores):
    ratio = val / demanda_actual
    label = f'{val:,} MW'
    if val != demanda_actual:
        label += f'\n({ratio:.1f}× demanda\nprovincial actual)'
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height() + 20,
        label,
        ha='center', va='bottom',
        fontsize=9.5, fontweight='bold',
        color=colores[categorias.index(barra.get_label()) if barra.get_label() in categorias else 0]
    )

ax.set_ylabel('MW', fontsize=11)
ax.set_title(
    'San Juan — Demanda minera en perspectiva provincial',
    fontsize=13, fontweight='bold'
)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.set_ylim(0, 900)

# Línea de referencia: potencia provincial actual
ax.axhline(y=demanda_actual, color='#3498DB', lw=1.5,
           linestyle='--', alpha=0.6, label=f'Demanda provincial actual ({demanda_actual} MW)')
ax.legend(fontsize=9, loc='upper left')

# Nota al pie sobre El Pachón
ax.text(
    0.5, -0.13,
    '* El Pachón: estimado por benchmark de throughput (185 kt/día, 3.600–4.200 msnm). '
    'Factibilidad no publicada.\n'
    'CEO Glencore Argentina confirmó >1.500 MW totales para el clúster (Expo Minera SJ, mayo 2026).',
    transform=ax.transAxes, ha='center', va='top',
    fontsize=7.5, color='#7F8C8D', style='italic'
)

plt.tight_layout()
ruta2 = f'{REPORTS_DIR}/04_02_proporcion_minera_provincial.png'
plt.savefig(ruta2, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta2}\n")


print(f"""
{'=' * 60}
RESUMEN DEL 04_
{'=' * 60}
  Gráficos generados:
    04_01_gap_analysis_san_juan.png   ← el gráfico central
    04_02_proporcion_minera_provincial.png

  Hallazgos confirmados por datos:
    Demanda actual San Juan:  ~551 MW pico (EPRE 2021)
    Capacidad línea 132kV:    ~90 MW (cuello de botella)
    Solo Josemaría (260 MW) casi triplica la capacidad de la línea
    Clúster minero: >1.500 MW = 2.7× la demanda provincial
    La brecha sin resolver: >1.960 MW

  Próximo paso: 05_ — el caso de la línea 500kV como
  estudio de caso regulatorio que cierra el análisis.
{'=' * 60}
""")
