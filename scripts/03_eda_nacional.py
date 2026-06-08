"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 03: EDA — Matriz eléctrica nacional Argentina 2005–2025
==============================================================
Objetivo:
  - Cargar el dataset limpio y filtrar las variables relevantes
  - Crear las visualizaciones clave de la matriz nacional:
      1. Evolución de potencia instalada por tecnología [MW]
      2. Composición porcentual de la matriz en 2005 vs 2025
      3. Curva de crecimiento renovable (Solar + Eólica)
      4. Demanda local total vs potencia máxima

  - Guardar los gráficos en reports/
  - Identificar los hallazgos para el análisis

Por qué este EDA importa al proyecto:
  Antes de mostrar el gap en San Juan, necesitamos establecer el
  contexto nacional — qué pasó con la matriz argentina en 20 años.
  La explosión renovable (especialmente solar en la región Cuyo)
  es el telón de fondo de toda la historia.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os
from datetime import datetime

# ============================================================
# CONFIGURACIÓN
# ============================================================

CLEAN_LONG  = 'data/clean/matriz_nacional_long.csv'
REPORTS_DIR = 'reports'

os.makedirs(REPORTS_DIR, exist_ok=True)

# Paleta de colores por tecnología — coherente en todos los gráficos
COLORES = {
    'Térmica':                    '#E07B39',  # naranja
    'Hidráulica Renovable HI > 50 MW (*****)': '#4A90D9',  # azul
    'Nuclear':                    '#9B59B6',  # violeta
    'Eólica':                     '#27AE60',  # verde
    'Solar':                      '#F1C40F',  # amarillo
    'Renovable Ley 26190':        '#2ECC71',  # verde claro
    'Hidráulica Renovable HI <= 50 MW': '#5DADE2',  # azul claro
    'Biomasa':                    '#795548',  # marrón
    'Biogas':                     '#A5D6A7',  # verde pálido
    'POTENCIA INSTALADA TOTAL':   '#2C3E50',  # gris oscuro
}

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
print("SCRIPT 03 — EDA MATRIZ NACIONAL")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")


# ============================================================
# PASO 1: CARGA Y LIMPIEZA FINAL
# ============================================================
print("--- PASO 1: CARGA ---\n")

df = pd.read_csv(CLEAN_LONG, encoding='utf-8')

# Limpiar saltos de línea residuales en categoría
df['categoria']    = df['categoria'].str.replace(r'\n', ' ', regex=True).str.strip()
df['subcategoria'] = df['subcategoria'].str.replace(r'\n', ' ', regex=True).str.strip()

print(f"Shape: {df.shape}")
print(f"Categorías disponibles: {df['categoria'].unique()}\n")


# ============================================================
# PASO 2: FILTROS — POTENCIA INSTALADA EN MW
# ============================================================
print("--- PASO 2: FILTROS ---\n")

# Categoría potencia instalada (limpiada)
cat_potencia = [c for c in df['categoria'].unique() if 'POTENCIA' in c][0]
cat_oferta   = [c for c in df['categoria'].unique() if 'OFERTA' in c][0]
cat_demanda  = 'DEMANDA'

print(f"  Categoría potencia: '{cat_potencia}'")
print(f"  Categoría oferta:   '{cat_oferta}'")
print(f"  Categoría demanda:  '{cat_demanda}'\n")

# Potencia instalada en MW (no en %)
mask_potencia_mw = (
    (df['categoria'] == cat_potencia) &
    (df['unidad'] == '[MW]') &
    (df['variable'] != 'POTENCIA INSTALADA TOTAL')  # total lo graficamos aparte
)
df_pot = df[mask_potencia_mw].copy()

# Total instalado
# Nota: el Excel tiene dos filas con el mismo nombre para esta variable,
# lo que genera un zigzag al graficar. groupby + max colapsa a una fila por año.
df_total = (
    df[
        (df['categoria'] == cat_potencia) &
        (df['variable'] == 'POTENCIA INSTALADA TOTAL') &
        (df['unidad'] == '[MW]')
    ]
    .groupby('anio', as_index=False)['valor']
    .max()
)

# Oferta: % cobertura renovable / demanda
df_cob_renov = df[
    (df['categoria'] == cat_oferta) &
    (df['variable'].str.contains('Cobertura Renovable', na=False))
].copy()

# Demanda local GWh
df_demanda = df[
    (df['categoria'] == cat_demanda) &
    (df['variable'] == 'DEMANDA LOCAL') &
    (df['unidad'] == '[GWh]')
].copy()

# Potencia máxima MW
df_pot_max = df[
    (df['categoria'] == cat_demanda) &
    (df['variable'] == 'POTENCIA MÁX') &
    (df['unidad'] == '[MW]')
].copy()

print(f"  Tecnologías en potencia instalada: {sorted(df_pot['variable'].unique())}")
print(f"  Años disponibles: {sorted(df['anio'].unique())}\n")


# ============================================================
# PASO 3: ESTADÍSTICAS DESCRIPTIVAS CLAVE
# ============================================================
print("--- PASO 3: HALLAZGOS PRINCIPALES ---\n")

# Potencia total 2005 vs 2025
total_2005 = df_total[df_total['anio'] == 2005]['valor'].values[0]
total_2025 = df_total[df_total['anio'] == 2025]['valor'].values[0]
print(f"  Potencia total instalada 2005:  {total_2005:,.0f} MW")
print(f"  Potencia total instalada 2025:  {total_2025:,.0f} MW")
print(f"  Crecimiento 20 años:            +{total_2025 - total_2005:,.0f} MW (+{(total_2025/total_2005 - 1)*100:.0f}%)\n")

# Solar y eólica 2005 vs 2025
for tec in ['Solar', 'Eólica']:
    v2005 = df_pot[(df_pot['variable'] == tec) & (df_pot['anio'] == 2005)]['valor'].values
    v2025 = df_pot[(df_pot['variable'] == tec) & (df_pot['anio'] == 2025)]['valor'].values
    if len(v2005) and len(v2025):
        print(f"  {tec} 2005: {v2005[0]:,.0f} MW  →  2025: {v2025[0]:,.0f} MW")

# Renovable Ley 26190
v_r2025 = df_pot[(df_pot['variable'] == 'Renovable Ley 26190') & (df_pot['anio'] == 2025)]['valor'].values
if len(v_r2025):
    print(f"  Total Renovable (Ley 26190) 2025: {v_r2025[0]:,.0f} MW  ({v_r2025[0]/total_2025*100:.1f}% del total)\n")

# Cobertura renovable
cob_2025 = df_cob_renov[df_cob_renov['anio'] == 2025]['valor'].values
if len(cob_2025):
    print(f"  % Cobertura Renovable / Demanda 2025: {cob_2025[0]:.1f}%\n")

# Demanda
dem_2005 = df_demanda[df_demanda['anio'] == 2005]['valor'].values[0]
dem_2025 = df_demanda[df_demanda['anio'] == 2025]['valor'].values[0]
print(f"  Demanda local 2005: {dem_2005/1000:.1f} TWh")
print(f"  Demanda local 2025: {dem_2025/1000:.1f} TWh")
print(f"  Crecimiento demanda 20 años: +{(dem_2025/dem_2005 - 1)*100:.0f}%\n")


# ============================================================
# PASO 4: GRÁFICO 1 — EVOLUCIÓN POTENCIA INSTALADA POR TECNOLOGÍA
# Apilado, 2005–2025. Muestra cómo creció cada fuente.
# ============================================================
print("--- GRÁFICO 1: Evolución potencia instalada ---")

# Tecnologías a graficar (las más relevantes para la historia)
tecs_grafico = [
    'Térmica',
    'Hidráulica Renovable HI > 50 MW (*****)',
    'Nuclear',
    'Eólica',
    'Solar',
    'Hidráulica Renovable HI <= 50 MW',
    'Biomasa',
]
tecs_presentes = [t for t in tecs_grafico if t in df_pot['variable'].unique()]

# Pivotear para el gráfico apilado
df_pivot = df_pot[df_pot['variable'].isin(tecs_presentes)].pivot_table(
    index='anio', columns='variable', values='valor', aggfunc='sum'
)
df_pivot = df_pivot.reindex(columns=tecs_presentes)
df_pivot = df_pivot.fillna(0)

anios = df_pivot.index.tolist()
colores_lista = [COLORES.get(t, '#AAAAAA') for t in tecs_presentes]

fig, ax = plt.subplots(figsize=(13, 6))
bottom = np.zeros(len(anios))
for tec, color in zip(tecs_presentes, colores_lista):
    valores = df_pivot[tec].values
    ax.bar(anios, valores, bottom=bottom, label=tec, color=color, width=0.75, alpha=0.92)
    bottom += valores

# Línea de total instalado
df_total_sorted = df_total.sort_values('anio')
ax.plot(
    df_total_sorted['anio'], df_total_sorted['valor'],
    color='#2C3E50', lw=2, marker='o', markersize=4,
    label='Total instalado', zorder=5
)

ax.set_title('Argentina — Potencia instalada por tecnología (2005–2025)')
ax.set_xlabel('Año')
ax.set_ylabel('MW')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.legend(loc='upper left', fontsize=9, framealpha=0.7)
ax.set_xlim(2004.5, 2025.5)
ax.set_xticks(anios)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
ruta = f'{REPORTS_DIR}/03_01_potencia_instalada_evolucion.png'
plt.savefig(ruta, bbox_inches='tight')
plt.close()
print(f"  ✓ Guardado: {ruta}")


# ============================================================
# PASO 5: GRÁFICO 2 — COMPOSICIÓN 2005 vs 2025 (DONUT)
# ============================================================
print("--- GRÁFICO 2: Composición 2005 vs 2025 ---")

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

for ax, anio in zip(axes, [2005, 2025]):
    datos = df_pot[
        (df_pot['variable'].isin(tecs_presentes)) &
        (df_pot['anio'] == anio)
    ].groupby('variable')['valor'].sum()
    datos = datos.reindex(tecs_presentes).fillna(0)
    datos = datos[datos > 0]

    colores_donut = [COLORES.get(t, '#AAAAAA') for t in datos.index]

    wedges, texts, autotexts = ax.pie(
        datos.values,
        labels=None,
        colors=colores_donut,
        autopct=lambda p: f'{p:.0f}%' if p > 3 else '',
        startangle=90,
        wedgeprops={'width': 0.55},
        pctdistance=0.75
    )
    for at in autotexts:
        at.set_fontsize(9)

    total = datos.sum()
    ax.text(0, 0, f'{total:,.0f}\nMW', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#2C3E50')
    ax.set_title(f'{anio}', fontsize=14, fontweight='bold', pad=15)

# Leyenda compartida
legend_handles = [
    plt.Rectangle((0, 0), 1, 1, color=COLORES.get(t, '#AAAAAA'), label=t)
    for t in tecs_presentes
]
fig.legend(handles=legend_handles, loc='lower center', ncol=4, fontsize=9,
           framealpha=0.7, bbox_to_anchor=(0.5, -0.02))
fig.suptitle('Composición de la matriz eléctrica argentina', fontsize=14,
             fontweight='bold', y=1.01)

plt.tight_layout()
ruta = f'{REPORTS_DIR}/03_02_composicion_2005_vs_2025.png'
plt.savefig(ruta, bbox_inches='tight')
plt.close()
print(f"  ✓ Guardado: {ruta}")


# ============================================================
# PASO 6: GRÁFICO 3 — CRECIMIENTO RENOVABLE (SOLAR + EÓLICA)
# ============================================================
print("--- GRÁFICO 3: Crecimiento renovable ---")

fig, ax = plt.subplots(figsize=(12, 5))

for tec, color, ls in [
    ('Eólica', COLORES['Eólica'], '-'),
    ('Solar',  COLORES['Solar'],  '-'),
    ('Renovable Ley 26190', COLORES['Renovable Ley 26190'], '--'),
]:
    serie = df_pot[(df_pot['variable'] == tec)].sort_values('anio')
    if not serie.empty:
        ax.plot(serie['anio'], serie['valor'],
                label=tec, color=color, lw=2.5, linestyle=ls,
                marker='o', markersize=5)

# Anotación Solar 2025
solar_2025 = df_pot[(df_pot['variable'] == 'Solar') & (df_pot['anio'] == 2025)]['valor'].values
if len(solar_2025):
    ax.annotate(
        f'Solar 2025:\n{solar_2025[0]:,.0f} MW',
        xy=(2025, solar_2025[0]),
        xytext=(2022, solar_2025[0] + 1000),
        arrowprops=dict(arrowstyle='->', color='gray'),
        fontsize=9, color=COLORES['Solar']
    )

ax.set_title('Argentina — Crecimiento de energías renovables (2005–2025)')
ax.set_xlabel('Año')
ax.set_ylabel('MW instalados')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.legend(fontsize=10)
ax.set_xlim(2004.5, 2026)
ax.set_xticks(sorted(df_pot['anio'].unique()))
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
ruta = f'{REPORTS_DIR}/03_03_crecimiento_renovable.png'
plt.savefig(ruta, bbox_inches='tight')
plt.close()
print(f"  ✓ Guardado: {ruta}")


# ============================================================
# PASO 7: GRÁFICO 4 — DEMANDA LOCAL vs POTENCIA MÁX
# ============================================================
print("--- GRÁFICO 4: Demanda vs Potencia máxima ---")

fig, ax1 = plt.subplots(figsize=(12, 5))
ax2 = ax1.twinx()

dem = df_demanda.sort_values('anio')
pmax = df_pot_max.sort_values('anio')

ax1.fill_between(dem['anio'], dem['valor'] / 1000, alpha=0.3,
                 color='#3498DB', label='Demanda local [TWh]')
ax1.plot(dem['anio'], dem['valor'] / 1000,
         color='#3498DB', lw=2.5, marker='o', markersize=5)

ax2.plot(pmax['anio'], pmax['valor'],
         color='#E74C3C', lw=2.5, linestyle='--',
         marker='s', markersize=5, label='Potencia máxima [MW]')

ax1.set_xlabel('Año')
ax1.set_ylabel('Demanda local [TWh]', color='#3498DB')
ax2.set_ylabel('Potencia máxima [MW]', color='#E74C3C')
ax1.tick_params(axis='y', labelcolor='#3498DB')
ax2.tick_params(axis='y', labelcolor='#E74C3C')
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}'))
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper left')

ax1.set_title('Argentina — Demanda eléctrica y potencia máxima (2005–2025)')
ax1.set_xticks(sorted(dem['anio'].unique()))
ax1.tick_params(axis='x', rotation=45)
plt.tight_layout()
ruta = f'{REPORTS_DIR}/03_04_demanda_potencia_max.png'
plt.savefig(ruta, bbox_inches='tight')
plt.close()
print(f"  ✓ Guardado: {ruta}")


# ============================================================
# RESUMEN FINAL
# ============================================================
print(f"""
{'=' * 60}
RESUMEN DEL 03_
{'=' * 60}
  Gráficos generados en reports/:
    03_01_potencia_instalada_evolucion.png
    03_02_composicion_2005_vs_2025.png
    03_03_crecimiento_renovable.png
    03_04_demanda_potencia_max.png

  Hallazgos para documentar:
    - Potencia total 2005→2025: {total_2005:,.0f} → {total_2025:,.0f} MW
    - Crecimiento demanda 20 años: +{(dem_2025/dem_2005 - 1)*100:.0f}%
{'=' * 60}

PRÓXIMO PASO:
  Compartí los 4 gráficos (screenshots o los archivos).
  Los revisamos juntos y documentamos los hallazgos antes
  de arrancar el script 04_ sobre San Juan específicamente.
""")
