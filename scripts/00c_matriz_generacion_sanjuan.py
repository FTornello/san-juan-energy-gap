"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 00c: Matriz de generación de San Juan (corregida)
=========================================================
Objetivo (capa accesible / Fase 0):
  Corregir el dato flojo de generación provincial. En vez de los
  "~92 MW firme local" subestimados, mostrar los 861 MW reales y,
  sobre todo, distinguir capacidad FIRME (despachable 24/7) de
  capacidad VARIABLE (solar, solo con sol).

  Mensaje clave:
    San Juan tiene MÁS capacidad instalada (861 MW) que su demanda
    pico (551 MW). Pero el 70% es solar variable. De noche, solo la
    generación firme (~258 MW) está disponible, y NO alcanza para
    cubrir la demanda provincial — por eso importa de la red nacional.
    Esto prepara la "curva de pato" que viene después.

Fuente: EPSE San Juan (feb. 2025): 30 centrales, 860,96 MW,
        70% solar (21 parques), 27% hidro (7 centrales), 3% térmica (1).
        Demanda pico provincial: 551 MW (EPRE, Anuario 2021).

Genera: reports/00_03_matriz_generacion_sanjuan.png
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

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

# Paleta por tecnología (consistente con el resto del proyecto)
C_SOLAR   = '#F1C40F'
C_HIDRO   = '#4A90D9'
C_TERMICA = '#E67E22'
C_DEMANDA = '#C0392B'

# ------------------------------------------------------------
# DATOS (fuente EPSE feb. 2025)
# ------------------------------------------------------------
TOTAL_INSTALADO = 861          # MW
SOLAR   = round(TOTAL_INSTALADO * 0.70)   # 603 MW
HIDRO   = round(TOTAL_INSTALADO * 0.27)   # 232 MW
TERMICA = TOTAL_INSTALADO - SOLAR - HIDRO  # 26 MW

FIRME    = HIDRO + TERMICA     # 258 MW — despachable 24/7
VARIABLE = SOLAR               # 603 MW — solo con sol

DEMANDA_PICO = 551             # MW (EPRE 2021)

fig, (axA, axB) = plt.subplots(1, 2, figsize=(15, 6.5),
                               gridspec_kw={'width_ratios': [1, 1.15]})

fig.suptitle(
    'San Juan — Generación instalada: mucha capacidad, pero mayormente solar',
    fontsize=14, fontweight='bold', y=1.02
)


# ============================================================
# PANEL A — Composición de los 861 MW (donut)
# ============================================================
valores = [SOLAR, HIDRO, TERMICA]
etiquetas = ['Solar', 'Hidroeléctrica', 'Térmica']
colores = [C_SOLAR, C_HIDRO, C_TERMICA]

wedges, _, autotexts = axA.pie(
    valores,
    colors=colores,
    autopct=lambda p: f'{p:.0f}%\n({p/100*TOTAL_INSTALADO:,.0f} MW)',
    startangle=90,
    counterclock=False,
    wedgeprops={'width': 0.5, 'edgecolor': 'white', 'linewidth': 2},
    pctdistance=0.74,
)
for at in autotexts:
    at.set_fontsize(9.5)
    at.set_fontweight('bold')
# texto oscuro sobre el amarillo solar
autotexts[0].set_color('#2C3E50')
autotexts[1].set_color('white')
autotexts[2].set_color('white')

axA.text(0, 0, f'{TOTAL_INSTALADO}\nMW\ninstalados',
         ha='center', va='center', fontsize=13, fontweight='bold', color='#2C3E50')
axA.set_title('Composición de la generación', fontsize=12, pad=14)

# leyenda con número de centrales
leg_labels = ['Solar — 21 parques', 'Hidro — 7 centrales', 'Térmica — 1 central (gas)']
leg_handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colores]
axA.legend(leg_handles, leg_labels, loc='lower center',
           bbox_to_anchor=(0.5, -0.16), ncol=1, fontsize=8.5, framealpha=0.6)


# ============================================================
# PANEL B — Capacidad disponible: día vs. noche (vs. demanda pico)
# ============================================================
x = [0, 1]
ancho = 0.5

# Mediodía (sol pleno): toda la capacidad disponible
axB.bar(0, SOLAR,   ancho, bottom=HIDRO + TERMICA, color=C_SOLAR,   edgecolor='white', linewidth=1.5, label='Solar (variable)')
axB.bar(0, HIDRO,   ancho, bottom=TERMICA,         color=C_HIDRO,   edgecolor='white', linewidth=1.5, label='Hidro (firme)')
axB.bar(0, TERMICA, ancho, bottom=0,               color=C_TERMICA, edgecolor='white', linewidth=1.5, label='Térmica (firme)')

# Noche / pico sin sol: solo capacidad firme
axB.bar(1, HIDRO,   ancho, bottom=TERMICA, color=C_HIDRO,   edgecolor='white', linewidth=1.5, alpha=0.92)
axB.bar(1, TERMICA, ancho, bottom=0,       color=C_TERMICA, edgecolor='white', linewidth=1.5, alpha=0.92)

# Línea de demanda pico provincial
axB.axhline(y=DEMANDA_PICO, color=C_DEMANDA, lw=2, linestyle='--', zorder=5)
axB.text(1.64, DEMANDA_PICO, f'demanda pico\nprovincial\n{DEMANDA_PICO} MW',
         ha='left', va='center', fontsize=8.5, color=C_DEMANDA, fontweight='bold',
         bbox=dict(facecolor='white', edgecolor='none', alpha=0.9, boxstyle='round,pad=0.25'))

# Totales encima de cada barra
axB.text(0, TOTAL_INSTALADO + 18, f'{TOTAL_INSTALADO} MW\ndisponibles',
         ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2C3E50')
axB.text(1, FIRME + 18, f'{FIRME} MW\nfirmes',
         ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2C3E50')

# Zona de excedente (mediodía: por encima de la demanda)
axB.annotate(
    f'excedente\n→ exporta\n(+{TOTAL_INSTALADO - DEMANDA_PICO} MW)',
    xy=(0.27, (TOTAL_INSTALADO + DEMANDA_PICO) / 2),
    ha='left', va='center', fontsize=8, color='#1E8449', fontweight='bold',
    bbox=dict(facecolor='#EAFAF1', edgecolor='#27AE60', alpha=0.9, boxstyle='round,pad=0.3', linewidth=0.8)
)

# Zona de déficit (noche: por debajo de la demanda)
axB.annotate(
    f'déficit\n→ importa\n(−{DEMANDA_PICO - FIRME} MW)',
    xy=(1.27, (DEMANDA_PICO + FIRME) / 2),
    ha='left', va='center', fontsize=8, color=C_DEMANDA, fontweight='bold',
    bbox=dict(facecolor='#FDEDEC', edgecolor=C_DEMANDA, alpha=0.9, boxstyle='round,pad=0.3', linewidth=0.8)
)

axB.set_xticks(x)
axB.set_xticklabels(['Mediodía\n(sol pleno)', 'Noche / pico\n(sin sol)'], fontsize=10)
axB.set_ylabel('MW disponibles', fontsize=11)
axB.set_ylim(0, TOTAL_INSTALADO + 90)
axB.set_xlim(-0.5, 2.1)
axB.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'{v:,.0f}'))
axB.set_title('Capacidad disponible según la hora', fontsize=12, pad=14)
axB.legend(loc='upper right', fontsize=8, framealpha=0.7)

# Nota explicativa al pie
fig.text(0.5, -0.06,
         'San Juan tiene más capacidad instalada (861 MW) que su demanda pico (551 MW), pero el 70% es solar variable. '
         'De noche solo quedan ~258 MW firmes (hidro + térmica),\nque no alcanzan para la demanda provincial: por eso importa de la red nacional. '
         'Una demanda minera constante 24/7 no puede apoyarse en generación que desaparece al atardecer.',
         ha='center', va='top', fontsize=8.5, color='#566573', style='italic')

fig.text(0.5, -0.13,
         'Fuente: EPSE San Juan (feb. 2025) · demanda pico: EPRE San Juan, Anuario 2021',
         ha='center', va='top', fontsize=7.5, color='#95A5A6', style='italic')

plt.tight_layout(rect=[0, 0.02, 1, 1])
ruta = f'{REPORTS_DIR}/00_03_matriz_generacion_sanjuan.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()

print("=" * 60)
print("SCRIPT 00c — MATRIZ DE GENERACIÓN SAN JUAN (CORREGIDA)")
print("=" * 60)
print(f"""
✓ Guardado: {ruta}

  Datos (EPSE feb. 2025):
    Total instalado:  {TOTAL_INSTALADO} MW
    Solar:            {SOLAR} MW (70%, variable)
    Hidro:            {HIDRO} MW (27%, firme)
    Térmica:          {TERMICA} MW (3%, firme)
    ─────────────────────────────
    Capacidad firme:  {FIRME} MW (hidro + térmica)
    Demanda pico:     {DEMANDA_PICO} MW (EPRE 2021)
    Déficit nocturno: {DEMANDA_PICO - FIRME} MW que debe importar

  Este gráfico corrige el dato flojo de los "92 MW firme local"
  y deja servida la curva de pato (próximo y último de la Fase 0).
""")
