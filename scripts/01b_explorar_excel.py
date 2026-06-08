"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 01b: Exploración del Excel de estadísticas anuales CAMMESA 2005-2025
============================================================================
Objetivo:
  - Listar todas las hojas del Excel y sus dimensiones
  - Mostrar las primeras filas de cada hoja para entender la estructura
  - Identificar qué hojas son relevantes para el proyecto
  - Documentar el hallazgo en logs/01b_reporte_excel.json

Por qué este script existe:
  Los CSVs del portal de datos abiertos solo llegaban a 2020.
  Este Excel tiene la serie completa 2005–2025, que es lo que necesitamos
  para mostrar la evolución de la matriz eléctrica argentina y el crecimiento
  renovable hasta la actualidad.

Fuente: CAMMESA — Resumen Anual 2025 / Estadísticas anuales 2005–2025
"""

import pandas as pd
import json
import os
from datetime import datetime

RUTA_EXCEL = 'data/raw/estadisticas_2005_2025.xlsx'

# ============================================================
# VERIFICACIÓN
# ============================================================
print("=" * 60)
print("SCRIPT 01b — EXPLORACIÓN DEL EXCEL CAMMESA")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60 + "\n")

if not os.path.exists(RUTA_EXCEL):
    print(f"ERROR: No encontré el archivo en {RUTA_EXCEL}")
    print("Verificá que lo hayas guardado con ese nombre exacto en data/raw/")
    exit(1)

print(f"✓ Archivo encontrado: {RUTA_EXCEL}")
tamaño_mb = os.path.getsize(RUTA_EXCEL) / (1024 * 1024)
print(f"  Tamaño: {tamaño_mb:.2f} MB\n")


# ============================================================
# PASO 1: LISTAR HOJAS
# ============================================================
print("--- HOJAS DEL ARCHIVO ---\n")

xl = pd.ExcelFile(RUTA_EXCEL)
hojas = xl.sheet_names

print(f"Total de hojas: {len(hojas)}")
for i, hoja in enumerate(hojas):
    print(f"  [{i}] {hoja}")

print()


# ============================================================
# PASO 2: EXPLORAR CADA HOJA
# ============================================================
print("--- EXPLORACIÓN POR HOJA ---")

reporte_hojas = {}

for hoja in hojas:
    print(f"\n{'=' * 60}")
    print(f"HOJA: '{hoja}'")
    print("=" * 60)

    # Intentamos leer sin asumir nada sobre el header
    try:
        # header=None para ver los datos crudos antes de asumir estructura
        df_raw = pd.read_excel(RUTA_EXCEL, sheet_name=hoja, header=None, nrows=10)
        print(f"Dimensiones (primeras 10 filas): {df_raw.shape}")
        print(f"\nPrimeras 10 filas (sin procesar):")
        print(df_raw.to_string())

        # También intentamos leer con header=0 para ver si tiene sentido
        df_h0 = pd.read_excel(RUTA_EXCEL, sheet_name=hoja, header=0, nrows=5)
        print(f"\nSi la fila 1 es header — columnas detectadas:")
        print(f"  {list(df_h0.columns)}")

        reporte_hojas[hoja] = {
            'filas_totales': None,  # completar a mano después
            'columnas': list(df_h0.columns),
            'primeras_filas_raw': df_raw.head(5).to_dict()
        }

    except Exception as e:
        print(f"  Error al leer la hoja: {e}")
        reporte_hojas[hoja] = {'error': str(e)}


# ============================================================
# PASO 3: LEER HOJA COMPLETA PARA LAS CANDIDATAS
# Después de ver la estructura, intentamos leer cada hoja completa
# y mostramos shape + columnas
# ============================================================
print(f"\n\n{'=' * 60}")
print("RESUMEN DE DIMENSIONES COMPLETAS")
print("=" * 60)
print("(esto puede demorar un momento si el archivo es grande)\n")

for hoja in hojas:
    try:
        df_full = pd.read_excel(RUTA_EXCEL, sheet_name=hoja)
        print(f"  '{hoja}': {df_full.shape[0]:,} filas × {df_full.shape[1]} columnas")
        reporte_hojas[hoja]['filas_totales'] = int(df_full.shape[0])
        reporte_hojas[hoja]['columnas_totales'] = int(df_full.shape[1])
    except Exception as e:
        print(f"  '{hoja}': ERROR — {e}")


# ============================================================
# PASO 4: GUARDAR REPORTE
# ============================================================
reporte = {
    '_metadata': {
        'proyecto': 'San Juan Energy Gap',
        'script': '01b_explorar_excel.py',
        'fecha_ejecucion': datetime.now().isoformat(),
        'archivo': RUTA_EXCEL,
        'total_hojas': len(hojas),
        'nombres_hojas': hojas
    },
    'hojas': reporte_hojas
}

os.makedirs('logs', exist_ok=True)
ruta_reporte = 'logs/01b_reporte_excel.json'
with open(ruta_reporte, 'w', encoding='utf-8') as f:
    json.dump(reporte, f, ensure_ascii=False, indent=2, default=str)

print(f"\n{'=' * 60}")
print(f"✓ Reporte guardado en: {ruta_reporte}")
print(f"{'=' * 60}")
print("""
PRÓXIMO PASO:
  Compartí el output de este script.
  Lo que necesito ver:
    1. Los nombres exactos de las hojas
    2. Las primeras filas de cada hoja (para entender si el header
       está en la fila 1 o más abajo — CAMMESA a veces tiene
       encabezados de 2-3 filas con títulos y subtítulos)
    3. Cuáles hojas tienen potencia instalada, generación y demanda
""")
