"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 02: Limpieza y transformación del Excel CAMMESA 2005-2025
================================================================
Objetivo:
  - Cargar el Excel con la estructura correcta (header en fila 3)
  - Mostrar TODAS las variables disponibles para decidir qué usar
  - Limpiar: snake_case, forward-fill de categorías, tipos correctos
  - Transformar de formato ancho (años como columnas) a formato largo
  - Guardar dos CSVs limpios listos para el análisis:
      data/clean/matriz_nacional_long.csv  → todas las variables, formato largo
      data/clean/variables_referencia.csv  → catálogo de variables disponibles

Decisiones de limpieza documentadas en logs/02_log_limpieza.json
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

RUTA_EXCEL  = 'data/raw/estadisticas_2005_2025.xlsx'
LOG_PATH    = 'logs/02_log_limpieza.json'
CLEAN_LONG  = 'data/clean/matriz_nacional_long.csv'
CLEAN_REF   = 'data/clean/variables_referencia.csv'

log = {
    'proyecto': 'San Juan Energy Gap',
    'script': '02_limpieza.py',
    'fecha': datetime.now().isoformat(),
    'decisiones': []
}

def registrar(descripcion, detalle=None):
    """Agrega una decisión de limpieza al log."""
    entrada = {'descripcion': descripcion}
    if detalle:
        entrada['detalle'] = detalle
    log['decisiones'].append(entrada)
    print(f"  [LOG] {descripcion}")

print("=" * 60)
print("SCRIPT 02 — LIMPIEZA Y TRANSFORMACIÓN")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")

os.makedirs('data/clean', exist_ok=True)
os.makedirs('logs', exist_ok=True)


# ============================================================
# PASO 1: CARGA CON ESTRUCTURA CORRECTA
# El Excel tiene 3 filas de título antes de los datos reales.
# La fila de encabezados está en el índice 3 (0-based).
# ============================================================
print("--- PASO 1: CARGA ---\n")

df = pd.read_excel(RUTA_EXCEL, sheet_name='Evolucion Anual', header=3)

print(f"Shape cargado: {df.shape[0]} filas × {df.shape[1]} columnas")
print(f"Columnas detectadas:\n  {list(df.columns)}\n")

registrar(
    "Carga con header=3 (fila 3 del Excel es el encabezado real)",
    f"Shape resultante: {df.shape}"
)


# ============================================================
# PASO 2: RENOMBRAR COLUMNAS
# Las primeras 3 columnas son celdas combinadas en el Excel
# que pandas lee como "Unnamed: 0", "Unnamed: 1", "Unnamed: 2".
# Los años vienen como 2005.0, 2006.0 — los convertimos a string.
# ============================================================
print("--- PASO 2: RENOMBRAR COLUMNAS ---\n")

# Construir mapa de renombrado
rename_map = {}
for col in df.columns:
    col_str = str(col)
    if 'Unnamed: 0' in col_str:
        rename_map[col] = 'categoria'
    elif 'Unnamed: 1' in col_str:
        rename_map[col] = 'subcategoria'
    elif 'Unnamed: 2' in col_str:
        rename_map[col] = 'variable'
    elif col_str == 'Unidad':
        rename_map[col] = 'unidad'
    else:
        # Años: 2005.0 → '2005'
        try:
            anio = int(float(col_str))
            rename_map[col] = str(anio)
        except ValueError:
            rename_map[col] = col_str

df = df.rename(columns=rename_map)
print(f"Columnas renombradas:\n  {list(df.columns)}\n")
registrar("Columnas renombradas a snake_case y años a string entero")


# ============================================================
# PASO 3: FORWARD-FILL DE CATEGORÍAS
# El Excel usa celdas combinadas para categoria y subcategoria.
# Pandas lee solo el primer valor; los demás quedan como NaN.
# Forward-fill propaga el valor hacia abajo hasta el siguiente.
# ============================================================
print("--- PASO 3: FORWARD-FILL DE CATEGORÍAS ---\n")

df['categoria']    = df['categoria'].ffill()
df['subcategoria'] = df['subcategoria'].ffill()

registrar(
    "Forward-fill aplicado a 'categoria' y 'subcategoria'",
    "Necesario porque el Excel usa celdas combinadas (merged cells)"
)


# ============================================================
# PASO 4: ELIMINAR FILAS VACÍAS / TOTALES DUPLICADOS
# Algunas filas no tienen variable (subtotales o separadores).
# ============================================================
print("--- PASO 4: LIMPIEZA DE FILAS ---\n")

n_antes = len(df)
df = df.dropna(subset=['variable'])
n_despues = len(df)

print(f"Filas antes: {n_antes} → después: {n_despues} (eliminadas: {n_antes - n_despues})\n")
registrar(
    f"Eliminadas {n_antes - n_despues} filas sin nombre de variable",
    "Corresponden a filas vacías o separadores del Excel"
)


# ============================================================
# PASO 5: LIMPIAR STRINGS
# ============================================================
print("--- PASO 5: LIMPIEZA DE STRINGS ---\n")

for col in ['categoria', 'subcategoria', 'variable', 'unidad']:
    df[col] = df[col].astype(str).str.strip()

registrar("Strip aplicado a columnas de texto")


# ============================================================
# PASO 6: MOSTRAR CATÁLOGO COMPLETO DE VARIABLES
# Esto es fundamental — necesitamos ver QUÉ variables existen
# antes de decidir cuáles usar en el análisis.
# ============================================================
print("--- PASO 6: CATÁLOGO COMPLETO DE VARIABLES ---\n")

catalogo = df[['categoria', 'subcategoria', 'variable', 'unidad']].reset_index(drop=True)

print(f"{'#':<5} {'CATEGORÍA':<25} {'VARIABLE':<45} {'UNIDAD':<12}")
print("-" * 90)
for i, row in catalogo.iterrows():
    print(f"{i:<5} {row['categoria']:<25} {row['variable']:<45} {row['unidad']:<12}")


# ============================================================
# PASO 7: GUARDAR CSV DE REFERENCIA DE VARIABLES
# ============================================================
catalogo.to_csv(CLEAN_REF, index=False, encoding='utf-8')
print(f"\n✓ Catálogo guardado en: {CLEAN_REF}\n")
registrar(f"Catálogo de variables guardado en {CLEAN_REF}")


# ============================================================
# PASO 8: TRANSFORMAR A FORMATO LARGO (MELT)
# Pasamos de formato ancho (años como columnas)
# a formato largo (una fila por variable × año).
#
# ANTES:  variable | unidad | 2005  | 2006  | ... | 2025
# DESPUÉS: variable | unidad | anio  | valor
#
# ¿Por qué formato largo?
# - Es el estándar para análisis con pandas y visualizaciones
# - Facilita filtrar por año, por variable, o por categoría
# - Es compatible con seaborn/matplotlib sin reshaping adicional
# ============================================================
print("--- PASO 8: MELT A FORMATO LARGO ---\n")

# Columnas de año: todo lo que sea un string de 4 dígitos numéricos
anios = [col for col in df.columns if col.isdigit() and len(col) == 4]
id_vars = ['categoria', 'subcategoria', 'variable', 'unidad']

df_long = df.melt(
    id_vars=id_vars,
    value_vars=anios,
    var_name='anio',
    value_name='valor'
)

df_long['anio'] = df_long['anio'].astype(int)
df_long['valor'] = pd.to_numeric(df_long['valor'], errors='coerce')

# Ordenar
df_long = df_long.sort_values(['categoria', 'variable', 'anio']).reset_index(drop=True)

print(f"Shape formato largo: {df_long.shape[0]:,} filas × {df_long.shape[1]} columnas")
print(f"Años disponibles: {sorted(df_long['anio'].unique())}")
print(f"Nulos en 'valor': {df_long['valor'].isnull().sum()}")
print(f"\nPrimeras filas:")
print(df_long.head(10).to_string())

registrar(
    "Melt aplicado: formato ancho → largo",
    f"Shape final: {df_long.shape}, años: {sorted(df_long['anio'].unique())}"
)


# ============================================================
# PASO 9: GUARDAR CSV LIMPIO
# ============================================================
df_long.to_csv(CLEAN_LONG, index=False, encoding='utf-8')
print(f"\n✓ Dataset limpio guardado en: {CLEAN_LONG}")


# ============================================================
# PASO 10: GUARDAR LOG DE LIMPIEZA
# ============================================================
log['shape_final'] = {'filas': int(df_long.shape[0]), 'columnas': int(df_long.shape[1])}
log['anios'] = sorted([int(a) for a in df_long['anio'].unique()])
log['n_variables'] = int(df_long['variable'].nunique())
log['categorias'] = list(df_long['categoria'].unique())

with open(LOG_PATH, 'w', encoding='utf-8') as f:
    json.dump(log, f, ensure_ascii=False, indent=2)

print(f"✓ Log de limpieza guardado en: {LOG_PATH}")

print(f"""
{'=' * 60}
RESUMEN DEL 02_
{'=' * 60}
  Variables disponibles: {df_long['variable'].nunique()}
  Años cubiertos:        2005 – 2025
  Categorías:            {', '.join(df_long['categoria'].unique())}
  Dataset limpio:        {CLEAN_LONG}
  Catálogo variables:    {CLEAN_REF}
{'=' * 60}

PRÓXIMO PASO:
  Revisá el catálogo completo que imprimió arriba.
  Necesito que me confirmes qué variables ves en la sección
  de POTENCIA INSTALADA — especialmente si hay desglose
  por tecnología (solar, eólica, hidro, térmica, nuclear).
  Con eso arrancamos el 03_ EDA.
""")
