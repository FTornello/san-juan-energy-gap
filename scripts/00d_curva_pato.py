"""
San Juan Energy Gap — Can the Grid Support the Mining Boom?
Script 00d: La curva de pato (esquema conceptual)
==================================================
Objetivo (capa accesible / Fase 0 — cierre):
  Explicar por qué la energía solar, aunque abundante, no resuelve
  una demanda minera constante. Muestra el fenómeno de la "curva de
  pato": cómo la demanda NETA (demanda total menos solar) se hunde
  al mediodía y se dispara al atardecer cuando el sol se va.

  Contraste central del proyecto:
    - La solar es una campana: cero de noche, pico al mediodía.
    - La demanda minera es PLANA: consume parejo las 24 horas.
    - Por eso una mina no puede apoyarse en solar — necesita
      generación firme o transmisión para importar energía cuando
      no hay sol.

  ⚠ HONESTIDAD DEL DATO:
  Este es un ESQUEMA CONCEPTUAL del fenómeno documentado, NO datos
  horarios medidos de San Juan (que no son públicos). La FORMA de
  las curvas corresponde al fenómeno real (CAISO, 2012); los valores
  están anclados a datos reales de San Juan (pico 551 MW, ~603 MW
  solares) pero el perfil hora a hora es ilustrativo.

Fuentes del concepto y los anclajes:
  - Curva de pato: California ISO (CAISO), 2012 — concepto estándar
  - Demanda pico San Juan: EPRE San Juan, Anuario 2021 (551 MW)
  - Capacidad solar San Juan: EPSE, feb. 2025 (~603 MW)
  - Perfil de carga minera (base, continuo): proceso de concentración
    domina el consumo (~55-58%) y opera 24/7 — COCHILCO (Chile)

Genera: reports/00_04_curva_pato.png
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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

# Colores
C_DEMANDA = '#2C3E50'   # demanda bruta
C_SOLAR   = '#F1C40F'   # generación solar
C_NETA    = '#C0392B'   # demanda neta (la "curva de pato")
C_MINA    = '#8E44AD'   # demanda minera (plana)
C_EXPORT  = '#27AE60'   # excedente exportable

# ------------------------------------------------------------
# CONSTRUCCIÓN DE LAS CURVAS (esquema conceptual)
# Anclajes reales: demanda pico ~551 MW · solar pico ~603 MW
# La FORMA es la del fenómeno documentado; el detalle horario es ilustrativo.
# ------------------------------------------------------------
h = np.linspace(0, 24, 500)

# Demanda bruta: base + bump matinal + pico vespertino (forma típica)
base     = 360
matinal  = 80  * np.exp(-((h - 10.0) / 3.0) ** 2)
vespert  = 191 * np.exp(-((h - 20.5) / 2.3) ** 2)   # pico ~551 al atardecer
demanda  = base + matinal + vespert

# Generación solar: campana diurna, pico ~603 al mediodía, cero de noche
solar = 603 * np.exp(-((h - 13.5) / 2.9) ** 2)
solar[(h < 6.5) | (h > 20.5)] = 0
solar = np.clip(solar, 0, None)

# Demanda neta = demanda - solar (la curva de pato)
neta = demanda - solar

# Demanda minera: plana, 24/7 (escala ilustrativa, ~1 proyecto grande)
mina = np.full_like(h, 550)

fig, ax = plt.subplots(figsize=(14, 7.5))

# --- Curvas ---
ax.plot(h, demanda, color=C_DEMANDA, lw=2.5, label='Demanda total (bruta)', zorder=4)
ax.fill_between(h, 0, solar, color=C_SOLAR, alpha=0.30, zorder=1)
ax.plot(h, solar, color='#D4AC0D', lw=2.2, label='Generación solar', zorder=3)
ax.plot(h, neta, color=C_NETA, lw=3, label='Demanda NETA (demanda − solar) = "curva de pato"', zorder=5)
ax.plot(h, mina, color=C_MINA, lw=2.5, linestyle='--', label='Demanda minera (plana, 24/7)', zorder=4)

# --- Línea de cero ---
ax.axhline(y=0, color='#7F8C8D', lw=1, zorder=2)

# --- Zona de excedente (demanda neta negativa → exporta) ---
ax.fill_between(h, neta, 0, where=(neta < 0), color=C_EXPORT, alpha=0.25, zorder=2)

# ============================================================
# ANOTACIONES
# ============================================================
# Vientre del pato (mediodía)
ax.annotate('el "vientre":\nde día sobra energía\n(la solar supera la demanda\n→ San Juan exporta)',
            xy=(13.5, neta[np.argmin(np.abs(h - 13.5))]),
            xytext=(8.5, -180),
            arrowprops=dict(arrowstyle='->', color=C_EXPORT, lw=1.6),
            fontsize=8.5, color='#1E8449', fontweight='bold', ha='center',
            bbox=dict(facecolor='#EAFAF1', edgecolor='#27AE60', alpha=0.92, boxstyle='round,pad=0.4', linewidth=1))

# Cuello del pato (atardecer)
idx_pico = np.argmin(np.abs(h - 20.5))
ax.annotate('el "cuello":\nal caer el sol, la demanda neta\nse dispara — hay que cubrirla\ncon generación firme o importada',
            xy=(20.5, neta[idx_pico]),
            xytext=(15.5, 600),
            arrowprops=dict(arrowstyle='->', color=C_NETA, lw=1.6),
            fontsize=8.5, color=C_NETA, fontweight='bold', ha='center',
            bbox=dict(facecolor='#FDEDEC', edgecolor=C_NETA, alpha=0.92, boxstyle='round,pad=0.4', linewidth=1))

# Demanda minera plana
ax.annotate('la mina consume PAREJO las 24 hs:\nnecesita energía también de noche,\ncuando la solar es cero',
            xy=(3, 550),
            xytext=(2.5, 290),
            arrowprops=dict(arrowstyle='->', color=C_MINA, lw=1.6),
            fontsize=8.5, color=C_MINA, fontweight='bold', ha='left',
            bbox=dict(facecolor='#F4ECF7', edgecolor=C_MINA, alpha=0.92, boxstyle='round,pad=0.4', linewidth=1))

# ============================================================
# FORMATO
# ============================================================
ax.set_title('La "curva de pato": por qué la solar abundante no resuelve una demanda constante',
             fontsize=13.5, fontweight='bold', pad=16)
ax.set_xlabel('Hora del día', fontsize=11)
ax.set_ylabel('MW', fontsize=11)
ax.set_xlim(0, 24)
ax.set_ylim(-260, 680)
ax.set_xticks(range(0, 25, 2))
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'{int(v):02d}h'))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'{v:,.0f}'))
ax.legend(loc='upper left', fontsize=9, framealpha=0.9, ncol=1)
ax.grid(axis='y', alpha=0.15)

# --- Disclaimer de honestidad del dato (importante) ---
fig.text(0.5, -0.02,
         'Esquema CONCEPTUAL del fenómeno documentado (curva de pato, CAISO 2012), NO datos horarios medidos de San Juan. '
         'La forma de las curvas es real;\nlos valores están anclados a datos reales (pico 551 MW — EPRE 2021; ~603 MW solares — EPSE 2025) '
         'pero el perfil hora a hora es ilustrativo. La demanda minera usa escala ilustrativa.',
         ha='center', va='top', fontsize=7.5, color='#95A5A6', style='italic')

plt.tight_layout(rect=[0, 0.04, 1, 1])
ruta = f'{REPORTS_DIR}/00_04_curva_pato.png'
plt.savefig(ruta, bbox_inches='tight', facecolor='white')
plt.close()

print("=" * 60)
print("SCRIPT 00d — CURVA DE PATO (ESQUEMA CONCEPTUAL)")
print("=" * 60)
print(f"""
✓ Guardado: {ruta}

  Cierra la capa accesible (Fase 0). Muestra el contraste central:
    - Solar: campana (cero de noche, pico al mediodía)
    - Demanda neta: vientre al mediodía, cuello al atardecer
    - Demanda minera: PLANA 24/7

  El gráfico está honestamente etiquetado como esquema conceptual:
  la forma es del fenómeno documentado (CAISO 2012), los valores
  anclados a datos reales de San Juan, el perfil horario ilustrativo.

  ── FASE 0 COMPLETA ──
  00_01  Flujo del sistema eléctrico
  00_02  Mapa institucional San Juan vs. Nación
  00_03  Matriz de generación de San Juan (861 MW)
  00_04  Curva de pato

  Próximo paso sugerido: integrar la Fase 0 al inicio del README
  (primero lo accesible, después lo técnico).
""")
