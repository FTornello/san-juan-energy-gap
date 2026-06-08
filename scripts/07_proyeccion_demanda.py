"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 07: Proyección de demanda eléctrica minera 2025–2040
==============================================================
Objetivo:
  Proyectar la demanda eléctrica del clúster minero del norte sanjuanino
  sobre el cronograma público de entrada de cada proyecto, con análisis
  de sensibilidad sobre El Pachón (la variable más incierta).

Nota sobre el horizonte temporal:
  El pedido original era 2025–2034. Se extendió a 2025–2040 porque El Pachón
  tiene producción proyectada para "finales de los 2030s" (Glencore, RIGI
  submission 2025/2026). Un horizonte de 2034 hubiera dejado el proyecto más
  grande fuera del rango, vaciando el análisis de sensibilidad.

=== DATOS vs. SUPUESTOS DEL MODELO ===

  DATOS (fuente primaria documentada):
  ─────────────────────────────────────
  Demanda provincial pico actual: 551 MW
    Fuente: EPRE San Juan, Anuario 2021 (Potencia Operada máxima)
  Josemaría — demanda eléctrica Fase 1: 260 MW
    Fuente: ENRE Resolución 79/2026 (filing de Vicuña Corp, BHP+Lundin)
  Los Azules — demanda eléctrica: 119 MW
    Fuente: McEwen Copper NI 43-101, nov. 2025 (estudio de factibilidad)
  El Pachón — demanda: NO publicada (sin fuente primaria)
    → Se modela como estimación por benchmark (ver sección ESTIMACIONES)
  Clúster total confirmado: >1.500 MW
    Fuente: CEO Glencore Argentina, Expo Minera San Juan, mayo 2026

  ESTIMACIONES (sin fuente primaria para demanda de El Pachón):
  ──────────────────────────────────────────────────────────────
  El Pachón — benchmark de demanda:
    Base: ~600 MW (throughput declarado 185 kt/día, alta altitud 3.600–4.200 msnm,
          comparado con QB2 y Quellaveco; factibilidad no publicada)
    Rango ilustrativo: 400 MW (bajo) / 600 MW (base) / 800 MW (alto)
    → 260 + 119 + 800 = 1.179 MW < >1.500 MW (el residual corresponde a Filo del Sol
      y otras expansiones no modeladas aquí)

  SUPUESTOS DEL MODELO (parámetros sin fuente directa):
  ──────────────────────────────────────────────────────
  1. Crecimiento demanda provincial: +2,0% anual (2022–2040)
       Justificación: CAGR histórico conservador para Argentina (~1,8–2,5%).
       Supuesto, no dato. La demanda real 2022–2026 no fue medida en este análisis.

  2. Cronograma Josemaría — rampa 2028–2030, plena operación 2030:
       Fuente del cronograma: BHP/Lundin Vicuña Corp, technical report H1 2026,
       objetivo de producción 2030. El objetivo anterior (2026–2027) fue desplazado.
       La ENRE Res. 79/2026 es sobre acceso a la línea, no sobre fecha de producción.
       → SUPUESTO del modelo, consistente con declaraciones públicas de Vicuña Corp.

  3. Cronograma Los Azules — rampa 2029–2030, plena operación 2030:
       Fuente del cronograma: McEwen Copper, producción esperada "fines 2029/principios
       2030" (post-FS nov. 2025, construcción estimada 2027+).
       → SUPUESTO del modelo, consistente con declaraciones públicas de McEwen Copper.

  4. Cronograma El Pachón — rampa variable según escenario:
       Fuente del cronograma: Glencore RIGI submission (2025/2026): producción en
       "finales de los 2030s". Sin fecha precisa.
       → Escenario alto: rampa 2034–2036, pleno 2036
       → Escenario base: rampa 2036–2038, pleno 2038
       → Escenario bajo: rampa 2037–2039, pleno 2039
       SUPUESTO DEL MODELO / ILUSTRATIVO. No existe fecha oficial publicada.

  5. Rampa de entrada: lineal en 2 años (0 % → 100 % de demanda)
       Estándar operativo para proyectos mineros de esta escala. Supuesto del modelo.

  REFERENCIA — plan de infraestructura actual:
  ─────────────────────────────────────────────
  Línea 500 kV propuesta (Vicuña Corp / Josemaría):
    Cobertura: 260 MW (solo Fase 1 de Josemaría — ENRE Res. 214/2026)
    No existe un plan coordinado de infraestructura para el clúster completo.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import os
from datetime import datetime

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':      'DejaVu Sans',
    'font.size':        11,
    'axes.titlesize':   13,
    'axes.titleweight': 'bold',
    'axes.spines.top':  False,
    'axes.spines.right': False,
    'figure.dpi':       150,
})

print("=" * 70)
print("SCRIPT 07 — PROYECCIÓN DE DEMANDA ELÉCTRICA MINERA 2025–2040")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 70 + "\n")

print("ADVERTENCIA DE CALIDAD DE DATOS")
print("-" * 70)
print("  ✓  Demanda provincial (551 MW): DATO — EPRE San Juan, Anuario 2021")
print("  ✓  Josemaría (260 MW):          DATO — ENRE Res. 79/2026")
print("  ✓  Los Azules (119 MW):         DATO — McEwen Copper NI 43-101, nov. 2025")
print("  ⚠  El Pachón (400/600/800 MW):  ESTIMACIÓN — benchmark; factibilidad no publicada")
print("  ⚠  Cronogramas de entrada:      SUPUESTO DEL MODELO — ver docstring")
print("  ⚠  Crecimiento provincial +2%:  SUPUESTO DEL MODELO — CAGR histórico aprox.")
print("-" * 70 + "\n")


# ============================================================
# PARÁMETROS DEL MODELO
# ============================================================

AÑOS = np.arange(2025, 2041)         # 2025–2040 inclusive
BASE_AÑO   = 2021                     # año del dato EPRE
DEMANDA_BASE = 551                    # MW — EPRE San Juan, Anuario 2021 (DATO)
CREC_PROV  = 0.02                     # +2% anual — SUPUESTO DEL MODELO

# Proyectos — demanda plena (MW) — DATO o ESTIMACIÓN según docstring
JOSEMARIA_MW  = 260   # DATO — ENRE Res. 79/2026
LOS_AZULES_MW = 119   # DATO — McEwen Copper NI 43-101, nov. 2025

# El Pachón — 3 escenarios — ESTIMACIÓN / ILUSTRATIVO
PACHON_ESCENARIOS = {
    'bajo': {
        'mw':          400,
        'ramp_inicio': 2037,
        'ramp_fin':    2039,
        'color':       '#B39DDB',   # violeta claro
        'label':       'Escenario bajo (400 MW, 2037–2039)',
    },
    'base': {
        'mw':          600,
        'ramp_inicio': 2036,
        'ramp_fin':    2038,
        'color':       '#7B1FA2',   # violeta medio
        'label':       'Escenario base (600 MW, 2036–2038)',
    },
    'alto': {
        'mw':          800,
        'ramp_inicio': 2034,
        'ramp_fin':    2036,
        'color':       '#4A148C',   # violeta oscuro
        'label':       'Escenario alto (800 MW, 2034–2036)',
    },
}

# Cronogramas — SUPUESTO DEL MODELO (ver docstring para fuentes)
JOSEMARIA_RAMP  = (2028, 2030)   # consistente con Vicuña Corp 2030 target
LOS_AZULES_RAMP = (2029, 2030)   # consistente con McEwen "fines 2029/principios 2030"

# Plan de infraestructura actual (línea 500 kV propuesta Vicuña)
PLAN_MW = 260   # cobertura real aprobada — ENRE Res. 214/2026 (solo Josemaría Fase 1)


# ============================================================
# FUNCIONES DEL MODELO
# ============================================================

def demanda_provincial(años, base_mw, base_año, crec):
    """Proyección de demanda provincial con crecimiento anual constante.
    SUPUESTO DEL MODELO: crecimiento uniforme al 2% anual desde el dato 2021."""
    return np.array([base_mw * (1 + crec) ** (a - base_año) for a in años])


def rampa_lineal(años, demanda_plena_mw, año_inicio, año_fin):
    """Curva de rampa lineal: 0 MW en año_inicio → demanda_plena en año_fin.
    SUPUESTO DEL MODELO: rampa lineal de 2 años es estándar operativo."""
    demanda = np.zeros(len(años))
    for i, a in enumerate(años):
        if a < año_inicio:
            demanda[i] = 0.0
        elif a >= año_fin:
            demanda[i] = demanda_plena_mw
        else:
            progreso = (a - año_inicio) / (año_fin - año_inicio)
            demanda[i] = demanda_plena_mw * progreso
    return demanda


# ============================================================
# CÁLCULO DE SERIES TEMPORALES
# ============================================================

dem_prov      = demanda_provincial(AÑOS, DEMANDA_BASE, BASE_AÑO, CREC_PROV)
dem_josemaria = rampa_lineal(AÑOS, JOSEMARIA_MW,  *JOSEMARIA_RAMP)
dem_losazules = rampa_lineal(AÑOS, LOS_AZULES_MW, *LOS_AZULES_RAMP)

series_pachon = {}
for escen, cfg in PACHON_ESCENARIOS.items():
    series_pachon[escen] = rampa_lineal(AÑOS, cfg['mw'], cfg['ramp_inicio'], cfg['ramp_fin'])

# Demanda total por escenario
dem_total = {}
for escen in PACHON_ESCENARIOS:
    dem_total[escen] = dem_prov + dem_josemaria + dem_losazules + series_pachon[escen]


# ============================================================
# IMPRESIÓN DE TABLA DE VERIFICACIÓN
# ============================================================

print("TABLA RESUMEN — demanda total por escenario (MW, años clave)\n")
print(f"  {'Año':>6}  {'Prov':>6}  {'Josemarí':>8}  {'LosAzul':>8}  "
      f"{'Pachón base':>12}  {'Total base':>11}  {'Total alto':>11}  {'Total bajo':>11}")
print("  " + "-" * 82)
for i, a in enumerate(AÑOS):
    if a in [2025, 2027, 2029, 2030, 2031, 2034, 2036, 2038, 2040]:
        print(f"  {a:>6}  {dem_prov[i]:>6.0f}  {dem_josemaria[i]:>8.0f}  "
              f"{dem_losazules[i]:>8.0f}  {series_pachon['base'][i]:>12.0f}  "
              f"{dem_total['base'][i]:>11.0f}  {dem_total['alto'][i]:>11.0f}  "
              f"{dem_total['bajo'][i]:>11.0f}")

print()
print(f"  [!] Josemaría y Los Azules llegan a plena operación en 2030 SIMULTÁNEAMENTE")
print(f"      → concentración de demanda nueva: +{JOSEMARIA_MW + LOS_AZULES_MW} MW")
print(f"         en aprox. 2 años (2029–2030)\n")


# ============================================================
# GRÁFICO 1 — TRAYECTORIA DE DEMANDA (escenario base con banda)
# ============================================================
print("--- Generando Gráfico 1: Trayectoria de demanda ---")

fig, ax = plt.subplots(figsize=(14, 8))

# ── Área apilada: solo componentes con fuente primaria ────────
# El Pachón NO va en el stack (sin fuente de demanda publicada).
# Se muestra por separado como banda de incertidumbre.
ax.stackplot(
    AÑOS,
    dem_prov,
    dem_josemaria,
    dem_losazules,
    labels=[
        f'Demanda provincial (dato 2021: {DEMANDA_BASE} MW; +2%/año supuesto)',
        f'Josemaría — {JOSEMARIA_MW} MW (DATO: ENRE Res. 79/2026)',
        f'Los Azules: {LOS_AZULES_MW} MW (DATO: McEwen NI 43-101, nov. 2025)',
    ],
    colors=['#2980B9', '#C0392B', '#E67E22'],
    alpha=0.82
)

# ── Banda El Pachón: 400–800 MW (sin área sólida) ────────────
base_conocida = dem_prov + dem_josemaria + dem_losazules
ax.fill_between(
    AÑOS,
    base_conocida + series_pachon['bajo'],
    base_conocida + series_pachon['alto'],
    alpha=0.35, color='#9B59B6',
    label='El Pachón: rango 400–800 MW\n(ESTIMACIÓN ilustrativa — factibilidad no publicada)'
)
# Línea del escenario base dentro de la banda
ax.plot(
    AÑOS, base_conocida + series_pachon['base'],
    color='#7B1FA2', lw=1.5, linestyle=':',
    label='El Pachón escenario base ~600 MW'
)

# ── Línea del plan actual ─────────────────────────────────────
# = demanda provincial proyectada + 260 MW de Josemaría (ENRE Res. 214/2026)
# No es una línea plana: crece con la demanda provincial base.
plan_total = dem_prov + PLAN_MW
ax.plot(
    AÑOS, plan_total,
    color='#27AE60', lw=2.5, linestyle='--', zorder=5,
    label=f'Plan actual: dem. provincial + {PLAN_MW} MW Josemaría\n(línea 500 kV Vicuña — ENRE Res. 214/2026)'
)

# ── Anotación: convergencia Josemaría + Los Azules ──────────
idx_2030 = np.where(AÑOS == 2030)[0][0]
ax.annotate(
    'Josemaría + Los Azules\nalcanzan plena operación\nen 2030 (simultáneamente)',
    xy=(2030, base_conocida[idx_2030]),
    xytext=(2031.5, base_conocida[idx_2030] + 120),
    arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.5),
    fontsize=9, color='#555', ha='left', style='italic',
    bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='#E67E22', alpha=0.85)
)

# ── Anotación: brecha plan vs. total base (2040) ─────────────
# Posicionada en zona alta libre (sobre la banda púrpura), con fondo blanco
idx_2040 = np.where(AÑOS == 2040)[0][0]
gap_2040 = (base_conocida[idx_2040] + series_pachon['base'][idx_2040]) - plan_total[idx_2040]
ax.annotate(
    f'Brecha plan vs. escenario base en 2040:\n≈{gap_2040:,.0f} MW sin cubrir',
    xy=(2040, plan_total[idx_2040] + gap_2040 / 2),
    xytext=(2034.5, base_conocida[idx_2040] + series_pachon['alto'][idx_2040] * 0.85),
    arrowprops=dict(arrowstyle='->', color='#6A1B9A', lw=1.5),
    fontsize=9, color='#4A148C', ha='center', style='italic',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#9B59B6', alpha=0.95)
)

# ── Líneas verticales: hitos de entrada ──────────────────────
hitos = {
    2029: ('2029–2030\nJosemaría &\nLos Azules\n(supuesto)', '#E67E22'),
    2036: ('2036–2038\nEl Pachón base\n(supuesto/ilustr.)', '#8E44AD'),
}
for año, (etiqueta, color) in hitos.items():
    ax.axvline(x=año, color=color, lw=1, linestyle=':', alpha=0.6, zorder=2)
    ax.text(año + 0.15, 100, etiqueta, fontsize=8, color=color, va='bottom', alpha=0.85)

# ── Decoración ───────────────────────────────────────────────
ax.set_xlim(2024.5, 2040.5)
ax.set_ylim(0, max(dem_total['alto']) * 1.12)
ax.set_xlabel('Año', fontsize=11)
ax.set_ylabel('Demanda eléctrica (MW)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))

ax.set_title(
    'San Juan — Proyección de demanda eléctrica minera 2025–2040\n'
    'Escenario base con banda de incertidumbre para El Pachón',
    fontsize=13, fontweight='bold', pad=16
)

reconciliacion = (
    'Proyección incluye los tres proyectos con cronograma conocido (Josemaría, Los Azules, El Pachón). '
    'Excluye Filo del Sol + expansiones (~521 MW, sin fecha pública): por eso el total modelado queda '
    'por debajo del clúster >1.500 MW confirmado por CEO Glencore Argentina (Expo Minera SJ, mayo 2026).'
)
ax.text(
    0.5, -0.10, reconciliacion,
    transform=ax.transAxes, ha='center', va='top',
    fontsize=7.8, color='#2C3E50', style='italic',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FDFEFE', edgecolor='#BDC3C7', alpha=0.9)
)

nota = (
    'Supuestos del modelo: crecimiento provincial +2%/año (CAGR histórico conservador). '
    'Cronogramas: Josemaría 2030 (Vicuña Corp / BHP+Lundin), Los Azules 2030 (McEwen Copper), '
    'El Pachón "finales de 2030s" (Glencore RIGI). El Pachón: sin fuente de demanda publicada — '
    'estimación por benchmark ilustrativa. Plan actual: línea 500 kV Vicuña Corp cubre solo '
    'Josemaría Fase 1 (ENRE Res. 214/2026).'
)
ax.text(
    0.5, -0.19, nota,
    transform=ax.transAxes, ha='center', va='top',
    fontsize=7.2, color='#7F8C8D', style='italic'
)

ax.legend(
    loc='upper left', fontsize=8.5,
    framealpha=0.92, edgecolor='#BDC3C7',
    bbox_to_anchor=(0.01, 0.99)
)

plt.tight_layout(rect=[0, 0.14, 1, 1])
ruta1 = f'{REPORTS_DIR}/07_01_proyeccion_demanda_base.png'
plt.savefig(ruta1, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta1}")


# ============================================================
# GRÁFICO 2 — ANÁLISIS DE SENSIBILIDAD: 3 ESCENARIOS EL PACHÓN
# ============================================================
print("--- Generando Gráfico 2: Sensibilidad El Pachón ---")

fig, ax = plt.subplots(figsize=(13, 7))

# Demanda sin El Pachón (base conocida: prov + Josem + LosAzul)
dem_sin_pachon = dem_prov + dem_josemaria + dem_losazules

# ── Base conocida (área) ──────────────────────────────────────
ax.fill_between(
    AÑOS, 0, dem_sin_pachon,
    color='#2C3E50', alpha=0.15,
    label=f'Base conocida: provincial + Josemaría + Los Azules (datos con fuente primaria)'
)
ax.plot(AÑOS, dem_sin_pachon, color='#2C3E50', lw=2, linestyle='-')

# ── 3 escenarios El Pachón ────────────────────────────────────
for escen, cfg in PACHON_ESCENARIOS.items():
    dem_tot = dem_sin_pachon + series_pachon[escen]
    ax.plot(
        AÑOS, dem_tot,
        color=cfg['color'], lw=2.2,
        linestyle={'bajo': ':', 'base': '-', 'alto': '--'}[escen],
        label=f"Total — {cfg['label']}  ⚠ estimación ilustrativa"
    )

# ── Banda de incertidumbre sombreada ─────────────────────────
ax.fill_between(
    AÑOS,
    dem_sin_pachon + series_pachon['bajo'],
    dem_sin_pachon + series_pachon['alto'],
    color='#9B59B6', alpha=0.12,
    label='Rango de incertidumbre El Pachón'
)

# ── Línea del plan actual ─────────────────────────────────────
ax.plot(
    AÑOS, plan_total,
    color='#27AE60', lw=2.5, linestyle='--', zorder=5,
    label=f'Plan actual: dem. provincial + {PLAN_MW} MW Josemaría\n(línea 500 kV Vicuña — ENRE Res. 214/2026)'
)

# ── Anotación: gap en 2030 (sin Pachón) ──────────────────────
idx_2030 = np.where(AÑOS == 2030)[0][0]
gap_2030 = dem_sin_pachon[idx_2030] - plan_total[idx_2030]
ax.annotate(
    f'Gap 2030 (sin Pachón):\n≈{gap_2030:,.0f} MW sin cubrir',
    xy=(2030, (dem_sin_pachon[idx_2030] + plan_total[idx_2030]) / 2),
    xytext=(2027, dem_sin_pachon[idx_2030] + 100),
    arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.4),
    fontsize=9, color='#2C3E50', ha='center', style='italic'
)

# ── Decoración ───────────────────────────────────────────────
ax.set_xlim(2024.5, 2040.5)
ax.set_ylim(0, max(dem_total['alto']) * 1.12)
ax.set_xlabel('Año', fontsize=11)
ax.set_ylabel('Demanda eléctrica total (MW)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))

ax.set_title(
    'Análisis de sensibilidad — El Pachón (400 / 600 / 800 MW)\n'
    'Impacto sobre la demanda total del clúster 2025–2040',
    fontsize=13, fontweight='bold', pad=16
)

reconciliacion2 = (
    'Proyección incluye los tres proyectos con cronograma conocido (Josemaría, Los Azules, El Pachón). '
    'Excluye Filo del Sol + expansiones (~521 MW, sin fecha pública): por eso el total modelado queda '
    'por debajo del clúster >1.500 MW confirmado por CEO Glencore Argentina (Expo Minera SJ, mayo 2026).'
)
ax.text(
    0.5, -0.09, reconciliacion2,
    transform=ax.transAxes, ha='center', va='top',
    fontsize=7.8, color='#2C3E50', style='italic',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FDFEFE', edgecolor='#BDC3C7', alpha=0.9)
)

nota2 = (
    '⚠ El Pachón: demanda sin publicar. Rango 400–800 MW = estimación ilustrativa por benchmark '
    '(throughput 185 kt/día a 3.600–4.200 msnm). '
    'Cronograma "finales de 2030s": Glencore RIGI submission 2025/2026. '
    'Cronogramas son supuestos del modelo, no compromisos contractuales.'
)
ax.text(
    0.5, -0.17, nota2,
    transform=ax.transAxes, ha='center', va='top',
    fontsize=7.2, color='#7F8C8D', style='italic'
)

ax.legend(
    loc='upper left', fontsize=8.5,
    framealpha=0.92, edgecolor='#BDC3C7',
    bbox_to_anchor=(0.01, 0.99)
)

plt.tight_layout(rect=[0, 0.12, 1, 1])
ruta2 = f'{REPORTS_DIR}/07_02_sensibilidad_pachon.png'
plt.savefig(ruta2, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {ruta2}")


# ============================================================
# RESUMEN IMPRESO
# ============================================================
print(f"""
{'=' * 70}
RESUMEN SCRIPT 07
{'=' * 70}

  Gráficos generados:
    07_01_proyeccion_demanda_base.png   ← trayectoria base con banda
    07_02_sensibilidad_pachon.png       ← análisis de sensibilidad 3 escenarios

  Hallazgos del modelo:
    Josemaría + Los Azules plena operación: 2030 (simultáneos)
    → Demanda nueva concentrada: +{JOSEMARIA_MW + LOS_AZULES_MW} MW en 2 años (2029–2030)
    → Gap vs. plan (línea Vicuña 260 MW) en 2030: ≈{gap_2030:,.0f} MW sin cubrir
       incluso antes de que El Pachón entre al cuadro

    El Pachón (estimación, "finales de 2030s"):
    → Escenario base (+600 MW): demanda total ~{dem_total['base'][idx_2040]:,.0f} MW en 2040
    → Escenario alto (+800 MW): demanda total ~{dem_total['alto'][idx_2040]:,.0f} MW en 2040
    → Escenario bajo (+400 MW): demanda total ~{dem_total['bajo'][idx_2040]:,.0f} MW en 2040

  Calidad de los datos de este script:
    ✓ Variables con fuente primaria: provincia (551 MW), Josemaría (260 MW),
      Los Azules (119 MW), clúster total (>1.500 MW)
    ⚠ Estimaciones: El Pachón (400/600/800 MW — benchmark, ilustrativo)
    ⚠ Supuestos del modelo: crecimiento +2%/año, cronogramas de entrada,
      rampa lineal 2 años

  Próximo paso:
    Correr 06_readme_log.py de nuevo para registrar script 07 y gráficos 07_01/02.
{'=' * 70}
""")
