"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 01: Descarga y exploración inicial de datos CAMMESA
=============================================================
Objetivo:
  - Descargar los datasets de CAMMESA desde el portal de datos abiertos
  - Guardar los archivos originales sin modificar (nunca tocar data/raw/)
  - Explorar la estructura de cada dataset: filas, columnas, tipos, nulos, rangos
  - Generar un reporte de calidad en JSON (logs/01_reporte_calidad.json)

Lo que NO hace este script:
  - No limpia nada. No cambia nombres de columnas. No imputa nulos.
  - Eso es trabajo del script 02_.

Fuente: CAMMESA Open Data — datos.energia.gob.ar
Licencia: Creative Commons Attribution
Actualización: mensual (último update: mayo 2026)
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

# ============================================================
# CONFIGURACIÓN
# ============================================================

# URLs directas de descarga — CAMMESA Open Data
URLS = {
    'potencia_instalada': (
        'http://datos.energia.gob.ar/dataset/'
        '2b4dfee6-6fca-4e4d-9611-a12d65cd4aa8/resource/'
        'b05fbb16-7278-463f-8895-087e2495bfee/download/potencia-instalada.csv'
    ),
    'demanda': (
        'http://datos.energia.gob.ar/dataset/'
        '2b4dfee6-6fca-4e4d-9611-a12d65cd4aa8/resource/'
        'ae008cdf-ed5d-4a85-90ee-5f4c53704e79/download/demanda-ltimos-aos.csv'
    ),
    'balance': (
        'http://datos.energia.gob.ar/dataset/'
        '2b4dfee6-6fca-4e4d-9611-a12d65cd4aa8/resource/'
        '863d7b10-4df9-4dad-8418-5e8a6cc730da/download/balance.csv'
    ),
}

# Estructura de carpetas del proyecto
CARPETAS = ['data/raw', 'data/clean', 'scripts', 'logs', 'reports']


# ============================================================
# UTILIDADES
# ============================================================

def crear_estructura():
    """Crea las carpetas del proyecto si no existen."""
    for carpeta in CARPETAS:
        os.makedirs(carpeta, exist_ok=True)
    print("✓ Estructura de carpetas lista\n")


def cargar_csv(nombre, url):
    """
    Descarga un CSV desde la URL dada.
    Intenta UTF-8 primero, cae a latin-1 si falla.
    Los archivos del Estado argentino a veces tienen encoding mixto.
    """
    print(f"→ Descargando '{nombre}'...")
    try:
        df = pd.read_csv(url, encoding='utf-8')
    except UnicodeDecodeError:
        print(f"  (UTF-8 falló, intentando latin-1...)")
        df = pd.read_csv(url, encoding='latin-1')
    except Exception as e:
        print(f"  ERROR al cargar {nombre}: {e}")
        return None
    print(f"  ✓ {df.shape[0]:,} filas × {df.shape[1]} columnas")
    return df


# ============================================================
# PASO 1: CREAR ESTRUCTURA Y DESCARGAR
# ============================================================

print("=" * 60)
print("SCRIPT 01 — DESCARGA Y EXPLORACIÓN")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")

crear_estructura()

# Descarga
print("--- DESCARGA ---")
datasets = {}
for nombre, url in URLS.items():
    df = cargar_csv(nombre, url)
    if df is not None:
        datasets[nombre] = df

print(f"\n✓ {len(datasets)}/{len(URLS)} datasets cargados correctamente\n")


# ============================================================
# PASO 2: GUARDAR ORIGINALES
# Regla de oro: data/raw/ no se toca nunca después de este paso.
# ============================================================

print("--- GUARDANDO ORIGINALES ---")
for nombre, df in datasets.items():
    ruta = f'data/raw/{nombre}_raw.csv'
    df.to_csv(ruta, index=False, encoding='utf-8')
    print(f"  Guardado: {ruta}")
print()


# ============================================================
# PASO 3: EXPLORACIÓN
# Para cada dataset, respondemos las preguntas del Workflow Genérico:
#   - ¿Cuántas filas y columnas?
#   - ¿Qué tipo de dato es cada columna?
#   - ¿Hay duplicados?
#   - ¿Cuántos nulos hay y qué porcentaje representan?
#   - ¿Los rangos de valores tienen sentido?
# ============================================================

def explorar(nombre, df):
    """
    Genera un resumen de calidad del dataset.
    Imprime en pantalla y devuelve un dict para el JSON log.
    """
    separador = "=" * 60
    print(f"\n{separador}")
    print(f"DATASET: {nombre.upper()}")
    print(separador)

    # --- Shape ---
    print(f"\nShape: {df.shape[0]:,} filas × {df.shape[1]} columnas")

    # --- Duplicados ---
    n_duplicados = df.duplicated().sum()
    print(f"Duplicados: {n_duplicados:,}")

    # --- Columnas ---
    print(f"\n{'Columna':<40} {'Tipo':<12} {'Nulos':>8} {'%Nulos':>8} {'Únicos':>8}  Muestra")
    print("-" * 100)
    columnas_info = []
    for col in df.columns:
        dtype   = str(df[col].dtype)
        nulos   = int(df[col].isnull().sum())
        pct     = round(nulos / len(df) * 100, 1)
        unicos  = int(df[col].nunique())
        muestra = str(df[col].dropna().iloc[0]) if len(df[col].dropna()) > 0 else 'N/A'
        print(f"  {col:<38} {dtype:<12} {nulos:>8,} {pct:>7.1f}% {unicos:>8,}  {muestra[:40]}")
        columnas_info.append({
            'nombre': col,
            'tipo': dtype,
            'nulos': nulos,
            'pct_nulos': pct,
            'unicos': unicos,
            'muestra': muestra[:80]
        })

    # --- Estadísticas numéricas ---
    numericas = df.select_dtypes(include=[np.number])
    if not numericas.empty:
        print(f"\nEstadísticas columnas numéricas:")
        print(numericas.describe().round(2).to_string())

    # --- Primeras filas ---
    print(f"\nPrimeras 3 filas:")
    print(df.head(3).to_string())

    # --- Últimas filas (para ver cobertura temporal) ---
    print(f"\nÚltimas 3 filas:")
    print(df.tail(3).to_string())

    return {
        'nombre': nombre,
        'filas': int(df.shape[0]),
        'columnas': int(df.shape[1]),
        'duplicados': int(n_duplicados),
        'columnas_detalle': columnas_info
    }


print("\n--- EXPLORACIÓN ---")
reporte = {}
for nombre, df in datasets.items():
    reporte[nombre] = explorar(nombre, df)


# ============================================================
# PASO 4: GUARDAR REPORTE DE CALIDAD
# Este JSON es el punto de partida para diseñar el script 02_.
# ============================================================

reporte['_metadata'] = {
    'proyecto': 'San Juan Energy Gap — Can the Grid Support the Mining Boom?',
    'script': '01_descarga_exploracion.py',
    'fecha_ejecucion': datetime.now().isoformat(),
    'fuente': 'CAMMESA Open Data — datos.energia.gob.ar',
    'licencia': 'Creative Commons Attribution',
    'datasets_cargados': list(datasets.keys()),
}

ruta_reporte = 'logs/01_reporte_calidad.json'
with open(ruta_reporte, 'w', encoding='utf-8') as f:
    json.dump(reporte, f, ensure_ascii=False, indent=2)

print(f"\n{'=' * 60}")
print(f"✓ Reporte de calidad guardado en: {ruta_reporte}")
print(f"{'=' * 60}")
print("""
PRÓXIMO PASO:
  Compartí el output de este script (lo que imprimió en consola)
  y el archivo logs/01_reporte_calidad.json.
  Con eso diseñamos el script 02_limpieza.py.

  Lo que tenés que mirar antes de eso:
    1. ¿Los nombres de columnas son descriptivos o crípticos?
    2. ¿Hay alguna columna de región/provincia? ¿Cómo se llama San Juan?
    3. ¿Hay columnas de fecha? ¿En qué formato?
    4. ¿Qué porcentaje de nulos tiene cada columna importante?
""")
