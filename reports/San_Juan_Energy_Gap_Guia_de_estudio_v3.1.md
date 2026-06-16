# SAN JUAN ENERGY GAP
## Guía de estudio profunda — v3.1
### Infraestructura eléctrica para el boom minero de San Juan, Argentina

> **Idea fuerza:** San Juan no tiene un problema de generar energía — tiene un problema de transportarla hasta sus minas.

**Junio 2026 — Versión 3.1**

---

## Índice

- [0. Conceptos que tenés que entender sí o sí](#0-conceptos)
- [1. Resumen ejecutivo](#1-resumen)
- [2. El contexto: por qué este proyecto importa](#2-contexto)
- [3. La pregunta central y la tesis](#3-pregunta)
- [4. Los datos y la jerarquía de evidencia](#4-datos)
- [5. El proceso técnico: cómo se construyó el análisis](#5-proceso)
- [6. El modelo: la proyección de demanda 2025–2040](#6-modelo)
- [7. El conflicto regulatorio](#7-regulatorio)
- [8. Cómo lo resuelve Chile: el modelo SEN + PPA](#8-chile)
- [9. Qué está en juego: la apuesta de Argentina](#9-juego)
- [10. Qué NO prueba este análisis](#10-limitaciones)
- [11. Escenarios: qué puede pasar](#11-escenarios)
- [12. Tabla resumen: todos los números clave](#12-tabla)
- [13. Tarjetas de memoria](#13-tarjetas)
- [14. Pitch STAR para entrevistas](#14-pitch)
- [15. La historia del proyecto](#15-historia)
- [16. Qué habilidades demuestra](#16-habilidades)
- [17. Qué monitorear](#17-monitorear)
- [18. Glosario](#18-glosario)
- [19. Fuentes](#19-fuentes)
- [20. Apéndice: estructura del repositorio](#20-apendice)

---

## 0. Conceptos que tenés que entender sí o sí

### 0.1 MW vs. MWh: la diferencia que más confunde

El **MW (megavatio)** es una unidad de *potencia*: la capacidad de producir energía en un instante dado. El **MWh (megavatio-hora)** es una unidad de *energía*: potencia × tiempo.

**Ejemplo concreto:**
- Una planta de **100 MW** que trabaja **10 horas** produce **1.000 MWh**.
- Una mina que consume **260 MW** continuos consume en un año: 260 MW × 8.760 hs = **2.277.600 MWh** (aproximadamente 2,3 TWh/año).
- Por eso cuando decimos "Josemaría necesita 260 MW", queremos decir que en cada instante necesita esa capacidad disponible.

### 0.2 Por qué se usa alta tensión: kV y pérdidas en la línea

La fórmula clave es: **P_pérdida = I² × R**. A mayor tensión, menor corriente para la misma potencia, y las pérdidas caen al cuadrado.

**Pérdidas por nivel de tensión:**
- **500 kV:** aproximadamente 1% de pérdidas cada 100 km.
- **132 kV:** aproximadamente 3–5% de pérdidas cada 100 km.
- Las minas de San Juan están a 250–410 km del nodo San Juan. En 132 kV llegaría entre un 10% y un 20% menos de energía. En 500 kV esa pérdida baja a 2–4%.

### 0.3 Generación firme vs. generación intermitente

Una fuente es **firme** si puede producir a voluntad 24/7 (hidro con embalse, gas). Es **intermitente** si solo produce cuando hay recurso natural (solar de día, eólico cuando hay viento). Las minas necesitan suministro **firme** garantizado.

- Factor de capacidad solar real San Juan: **26,0%** (1.372.040 MWh ÷ 603 MW ÷ 8.760 h — EPSE/CAMMESA dic. 2024, pipeline propio).
- Factor de capacidad hidro con embalse: ~40–60%.
- Factor de capacidad gas/vapor: >80% cuando se lo despacha.

### 0.4 Frecuencia, equilibrio y apagones

La red argentina opera a **50 Hz**. Si la demanda supera a la oferta, la frecuencia cae. Por debajo de 49 Hz los generadores se desconectan automáticamente para protegerse, y el SADI puede **fragmentarse** en islas eléctricas desconectadas, provocando un apagón masivo.

---

## 1. Resumen ejecutivo

**La pregunta:** San Juan está por convertirse en uno de los polos de cobre más importantes del mundo. ¿Puede su red eléctrica sostener esa demanda?

**La respuesta:** No con la infraestructura actual. Pero el problema no es de generación — la provincia tiene 861 MW instalados y al mediodía exporta energía. El cuello de botella es el transporte, la coordinación entre proyectos y la geografía.

| Concepto | Valor | Qué significa |
|---|---|---|
| Demanda del clúster minero | 1.500+ MW | CEO Glencore Argentina, Expo Minera SJ, mayo 2026 (Tier 2) |
| Capacidad con plan aprobado | 260 MW | Solo Josemaría, vía ENRE Res. 79/2026 (Tier 1) |
| Brecha de transporte minero | ~1.240 MW | 1.500 − 260 (calculado) |
| Generación instalada provincial | 861 MW | 70% solar, 27% hidro, 3% gas (Tier 1) |
| Generación firme (despachable) | ~258 MW | Hidro + térmica, EPSE feb. 2025 (Tier 1) |
| Demanda pico provincial 2021 | 551 MW | Sin minería, EPRE Anuario 2021 (Tier 1) |
| Brecha mínima en 2030 | ~119 MW | Con solo Josemaría + Los Azules (calculado, Tier 1-base) |

> **⚠ Estado al 9 de junio de 2026:** La resolución definitiva del ENRE sobre acceso compartido a la línea San Juan–Rodeo a 500 kV estaba **pendiente** al cierre de este documento. La audiencia pública se realizó el 3 de junio de 2026; ENRE Res. 214/2026 corrigió el alcance pero no resolvió el fondo. La factibilidad de El Pachón no estaba publicada. Su demanda (~600 MW) sigue siendo una estimación Tier 3.

---

## 2. El contexto: por qué este proyecto importa

### 2.1 El boom del cobre y la transición energética

El cobre es el metal de la transición energética. Las proyecciones de demanda global son contundentes:

| Aplicación | Cobre por unidad | Fuente |
|---|---|---|
| Auto eléctrico a batería (BEV) | ~83 kg/vehículo | Copper Development Association (CDA), copper.org |
| Auto a combustión (ICE) | ~23 kg/vehículo | CDA / copper.org |
| Panel solar | ~2,2 t/MW | Wood Mackenzie, 2024 |
| Eólica offshore | ~8 t/MW | Wood Mackenzie, 2024 |

- **IEA (Global Critical Minerals Outlook 2024):** déficit proyectado de ~30% en oferta vs. demanda para 2035 en escenario neto cero. (Tier 1)
- **Wood Mackenzie (2024):** demanda global de cobre crecerá ~24% hasta 42,7 Mt en 2035. (Tier 2)
- **S&P Global (2022):** shortfall acumulado de ~10 Mt para 2040 si los proyectos en pipeline no avanzan. (Tier 2)

El cinturón andino — Chile, Perú y Argentina — concentra ~50% de las reservas globales de cobre. Argentina produce menos de 0,1 Mt/año hoy, pero podría superar 1,5 Mt/año para mediados de la década de 2030.

### 2.2 Los cuatro proyectos: fichas detalladas

#### Josemaría y Filo del Sol — Vicuña Corp (BHP 50% + Lundin Mining 50%)

| Campo | Detalle | Nivel / Fuente |
|---|---|---|
| Operador | Vicuña Corp: BHP 50% + Lundin Mining 50% (JV cerrado ene. 2025, BHP pagó USD 2.000 M) | Tier 1 — Lundin press release |
| Ubicación | Iglesia, San Juan; 3.600–4.400 msnm | Tier 1 |
| Reservas Josemaría | 1,01 Bt @ 0,30% CuEq (Cu + Au + Mo) | Tier 1 — Lundin, dic. 2024 |
| Producción (Vicuña combinado) | ~395.000 t/año CuEq | Tier 1 |
| Throughput | 175.000 t/día | Tier 1 |
| Vida útil | 25 años | Tier 1 — NI 43-101 Lundin |
| Capex Josemaría fase 1 | ~USD 7.000 M | Tier 2 |
| Capex total Vicuña | ~USD 18.000 M | Tier 2 |
| Inicio producción objetivo | 2030 | Tier 1 |
| Demanda eléctrica | 260 MW | Tier 1 — ENRE Res. 79/2026 |
| Estado | En construcción | Tier 1 |

#### Los Azules — McEwen Copper

| Campo | Detalle | Nivel / Fuente |
|---|---|---|
| Operador | McEwen Copper (McEwen Inc. 46,4%; Stellantis 14,4%; otros) | Tier 1 |
| Ubicación | Calingasta, San Juan; ~3.500 msnm | Tier 1 |
| Factibilidad | NI 43-101 completada oct. 2025 | Tier 1 |
| Producción diseño | 215.000 t/año cátodo de cobre | Tier 1 — NI 43-101 |
| Producción promedio vida útil | 148.200 t/año | Tier 1 — NI 43-101 |
| Vida útil | 22 años | Tier 1 — NI 43-101 |
| Demanda eléctrica | 119 MW | Tier 1 — NI 43-101, nov. 2025 |
| Meta ambiental | Carbono-neutral en 2038 | Tier 2 |
| Estado | Buscando financiamiento post-factibilidad | Tier 1 |

Stellantis (Fiat, Peugeot, Chrysler) es accionista de Los Azules: integración vertical para asegurar suministro de cobre para sus vehículos eléctricos, exactamente lo que la IEA recomienda para minerales críticos.

#### El Pachón — Glencore 100%

| Campo | Detalle | Nivel / Fuente |
|---|---|---|
| Operador | Glencore 100% | Tier 1 |
| Ubicación | Calingasta, San Juan; ~3.600–4.200 msnm | Tier 1 — Mindat/PorterGeo |
| Recurso | ~6 Bt @ 0,43% Cu + Mo | Tier 1 — Glencore |
| Throughput plan | 185.000 t/día | Tier 2 |
| Producción estimada Cu | ~350.000 t/año | Tier 2 |
| Capex estimado | USD 8.500–10.500 M | Tier 2 — presentación RIGI |
| Vida útil | ~25 años | Tier 2 |
| Demanda eléctrica | ~600 MW | Tier 3 — estimación benchmark |
| Estado | Estudio de factibilidad en curso | Tier 1 |
| Inicio producción estimado | Fines de 2030s | Tier 2 |

> **⚠ Nota sobre altitud de El Pachón:** el depósito se ubica a ~3.600–4.200 msnm según Mindat y PorterGeo (Tier 1). Josemaría/Filo del Sol alcanzan 3.600–4.400 msnm. Las altitudes se superponen; ninguno es inequívocamente "el más alto".

### 2.3 Cómo funciona el sistema eléctrico argentino

#### Transformadores: por qué la electricidad viaja en alta tensión

La electricidad se genera entre 10 y 25 kV. Un transformador de potencia **eleva** esa tensión a 220 kV o 500 kV para el transporte. Al llegar al destino, otro transformador la **reduce** al nivel de uso. La relación de vueltas entre bobinas determina la relación de tensiones: doble de vueltas = doble de tensión, mitad de corriente, un cuarto de pérdidas.

Una estación transformadora (ET) de 500/220 kV como la que necesita Josemaría (ET Chaparro, ~3.000 msnm) puede costar entre USD 150–300 millones solo en equipamiento, más el costo civil en alta montaña.

#### Despacho CAMMESA y orden de mérito

CAMMESA despacha los generadores según el **orden de mérito**: menor costo variable primero. Renovables e hidro de pasada (costo variable ≈0) siempre despachan. Gas ciclo abierto (caro) solo para picos. Esto genera la curva de pato: mucho solar al mediodía deprime la demanda neta, y las térmicas deben subir rápido al atardecer.

### 2.4 La matriz eléctrica de San Juan: la paradoja

San Juan tiene 861 MW instalados (EPSE, feb. 2025): 70% solar (~603 MW), 27% hidro (~232 MW) y 3% gas (~26 MW). Solo ~258 MW son firmes. La provincia genera de sobra durante el día y exporta energía; de noche depende de las importaciones del SADI. Las minas están a 250–410 km de distancia y necesitan potencia firme 24/7.

---

## 3. La pregunta central y la tesis

> **El problema no es generación, es transporte + coordinación + geografía.**

- **Transporte:** la línea San Juan–Rodeo está diseñada para 500 kV pero opera a 132 kV. Para llegar a las minas faltan líneas y estaciones que ni existen.
- **Coordinación:** cada operador planea su propia línea. El CEO de Glencore Argentina dijo en mayo 2026 que ese modelo genera los costos más altos del mundo.
- **Geografía:** las minas están en dos regiones distintas de la cordillera, separadas ~150 km. No hay un corredor único posible.

---

## 4. Los datos y la jerarquía de evidencia

### 4.1 Los tres niveles

- **Tier 1 — Fuente primaria:** documentos oficiales verificables (resoluciones ENRE, NI 43-101, anuarios EPRE, informes de factibilidad).
- **Tier 2 — Declaración confirmada:** cifra dicha públicamente por una fuente con autoridad (CEO, comunicado de prensa, presentación oficial).
- **Tier 3 — Estimación por benchmark:** inferida por comparación con proyectos similares. Siempre etiquetada explícitamente.

### 4.2 Los números canónicos

| Cifra | Valor | Nivel | Fuente |
|---|---|---|---|
| Josemaría (demanda) | 260 MW | Tier 1 | ENRE Res. 79/2026 |
| Los Azules (demanda) | 119 MW | Tier 1 | McEwen Copper, NI 43-101 (nov. 2025) |
| Clúster total | 1.500+ MW | Tier 2 | CEO Glencore Argentina (mayo 2026) |
| El Pachón (demanda est.) | ~600 MW | Tier 3 | Benchmark 185 kt/día en altitud |
| Filo del Sol + expansiones | ~521 MW residual | Residual | Ver nota ↓ |
| Demanda pico provincial 2021 | 551 MW | Tier 1 | EPRE San Juan, Anuario 2021 |
| Generación instalada | 861 MW | Tier 1 | EPSE San Juan (feb. 2025) |
| Generación firme | ~258 MW | Tier 1 | Hidro + térmica (EPSE) |

> **⚠ Nota sobre el residual de ~521 MW (Filo del Sol + expansiones):** este valor es aritmética inversa — es lo que falta para cerrar en 1.500 MW. No proviene de ningún documento de factibilidad; hereda toda la incertidumbre de la cifra Tier 2 del CEO. Tratar como Tier 3 a los efectos de análisis.

### 4.3 La realidad de la transmisión

- Línea San Juan–Rodeo: ~161 km, diseñada para 500 kV, opera a 132 kV.
- Para Josemaría: nueva línea 500 kV Rodeo–Chaparro (~167 km) + ET Chaparro (500/220 kV, tipo GIS, ~3.000 msnm) + línea 220 kV Chaparro–Josemaría (~93 km).
- Los Azules y El Pachón están en Calingasta (sur), ~150 km separados de Josemaría. Requieren un corredor completamente distinto.

---

## 5. El proceso técnico: cómo se construyó el análisis

### 5.1 Stack y flujo de trabajo

Python 3, pandas, matplotlib. Cada script se escribía, se ejecutaba, se revisaba con ojo crítico y recién ahí se avanzaba. El criterio rector: honestidad sobre la calidad del dato. A partir de la v3.1 se agrega la **regla de oro**: todo número que el documento afirme debe ser el output de un script reproducible.

### 5.2 Los datos de CAMMESA

Portal datos.energia.gob.ar, archivos CSV/Excel mensuales desde 1992. Columnas principales: *periodo* (AAAA-MM), *agente_cammesa*, *tecnologia*, *energia_gwh*, *potencia_mw*, *provincia*.

- `groupby(['provincia','tecnologia'])['energia_gwh'].sum()`: generación por provincia y tecnología.
- `pivot_table(index='periodo', columns='tecnologia', values='energia_gwh')`: composición de la matriz en el tiempo.
- `resample('Y', on='fecha')['energia_gwh'].sum()`: datos mensuales a anuales.
- `fillna(0)`: rellenar meses sin generación (solar antes de 2015).

**Cálculo paso a paso: la brecha eléctrica:**
1. Cargar demanda histórica EPRE. Calcular CAGR ~2%/año.
2. Proyectar demanda provincial con ese CAGR (supuesto etiquetado).
3. Sumar demanda minera: Josemaría 260 MW desde 2030, Los Azules 119 MW desde 2030, El Pachón ~600 MW desde 2036 (est.).
4. Demanda total = provincial + minera.
5. Brecha de transporte minero = 260 + 119 − 260 = **119 MW** (lo que los dos proyectos 2030 demandan vs. el único plan aprobado). Esta brecha NO depende del CAGR provincial.

---

## 6. El modelo: la proyección de demanda 2025–2040

### 6.1 La disciplina dato vs. supuesto

| Variable | Naturaleza |
|---|---|
| Demanda de cada proyecto (260, 119, ~600 MW) | Dato con fuente citada / Tier 3 etiquetado |
| Crecimiento provincial +2%/año | Supuesto conservador del modelo — ver 6.2 |
| Año de entrada de cada proyecto | Cronograma público + inferencia |

### 6.2 Los cronogramas

- **Josemaría:** producción objetivo 2030 (BHP/Lundin, Tier 1).
- **Los Azules:** fines 2029 / principios 2030 (McEwen, Tier 2).
- **El Pachón:** fines de 2030s (Glencore, Tier 2). Horizonte extendido a 2040.

### 6.3 Proyección base y análisis de sensibilidad

*(Ver figuras 12 y 13 en el PDF)*

### 6.4 Proyección provincial: CAGR base vs. boom (script 08)

El CAGR del 2% es el **piso conservador** que refleja el crecimiento histórico de San Juan sin minería. El **escenario boom** usa un CAGR del 3,75% para capturar el efecto indirecto del boom minero sobre la demanda no-minera: 25.000–35.000 empleos directos + 3–5x empleos indirectos aumentan la actividad eléctrica provincial.

**Importante:** el CAGR provincial **NO afecta la brecha de transporte minero** de 2030. Josemaría necesita 260 MW y Los Azules necesita 119 MW independientemente de cuánto crezca San Juan: la brecha de transporte minero es fija en 119 MW (379 MW demanda minera − 260 MW plan). Lo que sí varía con el CAGR es la brecha de generación firme nocturna (sección 6.5).

**Output del script 08 — valores para el documento (base: 551 MW en 2021):**

| Año | CAGR 2% (MW) | CAGR 3,75% (MW) |
|---|---|---|
| 2025 | 596,4 | 638,4 |
| 2028 | 632,9 | 713,0 |
| 2030 | **658,5** | **767,4** |
| 2032 | 685,1 | 826,1 |
| 2035 | 727,0 | 922,5 |
| 2036 | **741,6** | **957,1** |
| 2040 | 802,7 | 1.109,0 |

*Todos los valores provienen del script 08 (output reproducible).*

### 6.5 Brecha de generación firme: el problema nocturno (script 09)

Hay una segunda brecha que el análisis de transporte no captura: la brecha de **generación firme nocturna**. De noche, San Juan solo tiene ~258 MW firmes disponibles (hidro + térmica, EPSE). El resto de la demanda se importa del SADI.

> **Supuesto explícito — demanda nocturna:** No existe un perfil horario desagregado publicado por EPRE San Juan. Este análisis usa el **pico de demanda provincial como cota superior** de la demanda nocturna (supuesto Tier 3).
>
> Sensibilidad al 90%: el descuento aplica **solo a la componente provincial** (la demanda minera es 24/7 constante y no se reduce). Si la demanda nocturna provincial fuera el 90% del pico: 658,5 × 0,90 + 379 − 258 = **713,6 MW** (déficit 2030). Aplicar el 90% al total incluyendo minería —como en la v3— daba 675,7 MW, que es incorrecto conceptualmente.
>
> Fuente pico: EPRE San Juan, Anuario 2021 (551 MW). CAGR 2%/año (script 08).

**Output del script 09 — déficit nocturno proyectado (CAGR 2%):**

| Año | Prov. (MW) | Minera (MW) | Total noche (MW) | Déficit noche (MW) |
|---|---|---|---|---|
| 2025 | 596,4 | 0,0 | 596,4 | **338,4** |
| 2030 | 658,5 | 379,0 | 1.037,5 | **779,5** |
| 2036 | 741,6 | 979,0 | 1.720,6 | **1.462,6** |

*Factor 90% correcto (solo provincial): 658,5 × 0,90 + 379 − 258 = **713,6 MW**. Todos los valores provienen del script 09 (output reproducible).*

### 6.6 Escenario solar + BESS: ¿y si ponen baterías? (script 10)

La pregunta más común: ¿no alcanza con poner paneles solares y baterías para abastecer las minas? La respuesta corta es: técnicamente sí, pero la escala sorprende.

**Caso de estudio:** Los Azules, 119 MW continuos 24/7.

**Parámetros del escenario (script 10):**
- **FC solar real San Juan:** 26,0% (1.372.040 MWh ÷ 603 MW ÷ 8.760 h — portal EPSE/CAMMESA dic. 2024, pipeline propio — Tier 1 derivado). *Nota: este FC asume los 603 MW instalados durante todo 2024. Si hubo altas de capacidad a lo largo del año, el valor real difiere levemente (refinamiento posible con datos mensuales de CAMMESA).*
- **Horas nocturnas:** 13,5 h promedio anual (latitud ~31,5° S, San Juan). Parámetro real — NO se usa FC × 24h (ese sería un error conceptual: el FC es una equivalencia energética, no la duración del día).
- **Eficiencia round-trip BESS:** 87% (litio-ión, estándar industria). Degradación ignorada (supuesto conservador del modelo, Tier 3).
- **Balance:** solar debe producir = demanda diurna directa (119 MW × 10,5 h) + carga de batería para la noche (119 MW × 13,5 h ÷ 0,87).

**Output del script 10 — resultados clave:**

| FC solar | MW solar necesarios | BESS (MWh) |
|---|---|---|
| 22% | 586 MW | 1.606,5 MWh |
| 25% | 516 MW | 1.606,5 MWh |
| **26,0% (real CAMMESA)** | **497 MW** | **1.606,5 MWh** |
| 30% | 430 MW | 1.606,5 MWh |

- **Energía total mina/día:** 119 MW × 24 h = 2.856,0 MWh
- **Solar debe producir/día:** 3.096,1 MWh (= 1.249,5 MWh diurna + 1.846,6 MWh carga BESS)
- **BESS capacidad de descarga:** **1.606,5 MWh** (= 119 MW × 13,5 h) — valor FIJO, no depende del FC solar
- **Costo estimado BESS** (USD 280–320/kWh, mercado 2024–2025, Tier 3): **USD 450–514 M**

*Todos los valores provienen del script 10 (output reproducible).*

---

## 7. El conflicto regulatorio: acceso abierto, RIGI y la audiencia del 3 de junio

### 7.1 El principio de acceso abierto (Ley 24.065, Art. 15)

La Ley 24.065 de 1992 establece el principio de **acceso abierto**: todo agente del MEM tiene derecho a usar la red de transmisión pagando la cuota de transporte. Nadie puede monopolizar una línea de alta tensión.

La transmisión troncal del SADI la financian **todos** los usuarios del MEM vía cuota de transporte. Las líneas de conexión para grandes usuarios nuevos (como las minas) las paga el usuario nuevo. El conflicto concreto: si Josemaría construye y financia la energización de la línea San Juan–Rodeo a 500 kV, ¿puede cobrarle el acceso a Los Azules — o restringírselo hasta recuperar su inversión? Eso es exactamente lo que debate el ENRE.

### 7.2 El sobrecosto del modelo fragmentado: benchmark

**Benchmark: costo por km de línea 500 kV en Argentina:**
- **Fuente:** Segunda LEAT Choele Choel–Puerto Madryn: 350 km de línea doble circuito 500 kV, valor de licitación ~USD 1.600 M. (argentina.gob.ar + power-technology.com/marketdata — Tier 2)
- **Costo unitario base:** ~USD 4,57 M/km (terreno plano patagónico).
- **Ajuste por terreno montañoso:** +30–50% estimado (altitud, acceso vial, suelo rocoso). Rango ajustado: USD 5,9–6,9 M/km (Tier 3).

> **⚠ Nota metodológica:** la licitación Choele Choel–Puerto Madryn es **llave en mano** e incluye estaciones transformadoras y obras complementarias, por lo que sobreestima el costo de "solo línea". Por otra parte, el escenario coordinado también requiere su propia ET de entrada. El diferencial entre escenarios sigue siendo el argumento central.

| Escenario | Infraestructura sur (Calingasta) | Costo estimado | Nivel |
|---|---|---|---|
| Coordinado | 1 línea compartida 500 kV, ~280 km | ~USD 1.800 M | Tier 3 |
| Fragmentado | 2 líneas paralelas × 280 km + 2 ET adicionales | ~USD 4.100 M | Tier 3 |
| Sobrecosto fragmentado | USD ~2.300 M adicionales (+128%) | — | Tier 3 |

### 7.3 RIGI: Régimen de Incentivo para Grandes Inversiones (Ley 27.742)

| Beneficio | Detalle |
|---|---|
| Estabilidad fiscal | 30 años desde la adhesión. Sin nuevas cargas fiscales. |
| Impuesto a las ganancias | 35% → 25% para proyectos RIGI. |
| Estabilidad cambiaria | Sin restricciones a repatriación de utilidades (post-reinversión). |
| Exención aduanera | Bienes de capital e insumos importados sin aranceles. |
| Inversión mínima | USD 200 millones en un plazo máximo de 2 años. |
| Pipeline al jun. 2026 | >USD 95.000 M en proyectos energético-mineros (Tier 2 — Sec. Minería) |

### 7.4 La audiencia pública del 3 de junio de 2026

- ENRE Res. 79/2026: le otorgó a Vicuña (Josemaría) prioridad por 25 años sobre el 90% de la capacidad nueva al energizar la línea a 500 kV.
- La audiencia pública del 3 de junio 2026 contó con múltiples oradores: EPRE San Juan, McEwen/Los Azules, municipios de Iglesia y Jáchal, provincia de La Rioja y asociaciones vecinales, entre otros. (Número exacto de oradores no verificado en fuente primaria.)
- ENRE Res. 214/2026: corrigió el alcance a solo Josemaría Fase 1. Sin resolución definitiva sobre acceso compartido al cierre de este análisis.

---

## 8. Cómo lo resuelve Chile: el modelo SEN + PPA

### 8.1 El Sistema Eléctrico Nacional (SEN) chileno

Chile unificó sus dos grandes sistemas en 2017. El SEN tiene un mercado spot activo con precios horarios. En algunas horas solares el precio spot ha llegado a ser negativo por exceso de solar — esto incentiva el almacenamiento con baterías.

### 8.2 Los PPA de largo plazo

Codelco no resolvió su problema energético construyendo plantas propias. Firmó contratos de suministro de largo plazo (**PPAs**) con generadores privados de renovables:

- **Atlas Renewable Energy (2023):** PPA 15 años, solar + almacenamiento en baterías, garantía de suministro firme 24/7.
- **Grenergy (2025, vigente desde ene. 2026):** PPA 24/7 por 15 años, 0,5 TWh/año. Energía proveniente de proyectos híbridos solar + BESS, incluyendo la planta Monte Águila (340 MW). (Fuente: Grenergy press release / guiaminera.cl — Tier 1)

El modelo: la mina no pone capital en generación; el contrato de largo plazo hace bankable el proyecto del generador para los bancos.

### 8.3 El resultado: 78% renovable en minería en 2024

Según COCHILCO (informe oficial cochilco.cl, Tier 1), en 2024 el sector minero chileno obtuvo el **78% de su electricidad de fuentes renovables**. Meta del sector: 100% para 2030.

La clave no es que Chile "tenga más sol". Es que tiene tres cosas que Argentina todavía no consolida: marco regulatorio de acceso abierto funcionando, PPAs de largo plazo como instrumento estándar, y almacenamiento con baterías integrado en los proyectos.

---

## 9. Qué está en juego: la apuesta de Argentina

| Indicador | Valor proyectado | Fuente / Año |
|---|---|---|
| Exportaciones mineras 2026 (actual) | ~USD 4.000 M/año | Sec. Minería, 2026 |
| Exportaciones mineras 2030 | ~USD 5.269 M/año | Sec. Minería, 2025 |
| Exportaciones mineras 2032 | ~USD 11.400 M/año | Sec. Minería, 2025 |
| Participación en Cu global estimada 2030 | ~2% | Sec. Minería |
| Portfolio de inversión en evaluación | >USD 28.000 M | Sec. Minería, 2025 |
| Empleo directo estimado en operación plena | 25.000–35.000 puestos | Tier 3 — estimación sectorial |

USD 11.400 M de exportaciones mineras en 2032 equivaldrían a más de la mitad de las exportaciones totales de soja de Argentina en un año típico.

> **⚠** Las proyecciones de exportaciones son del propio gobierno argentino (Secretaría de Minería) — Tier 2 con sesgo potencial de optimismo. Leerlas como escenario favorable, no como certeza.

---

## 10. Qué NO prueba este análisis

- **La demanda de El Pachón y Filo del Sol son estimaciones (Tier 3).** Ningún documento de factibilidad publicado confirma esos números.
- **El cronograma de 2030 puede correrse.** Los proyectos en alta altitud tienen historial de demoras.
- **No se modeló el perfil horario de la demanda minera.** Se asumió consumo constante 24/7 a potencia plena.
- **El almacenamiento en baterías cambia el cálculo.** Con FC real 26,0% (CAMMESA 2024), se necesitan 497 MW de solar + 1.606,5 MWh de BESS para 119 MW firmes. Técnicamente viable; costoso (~USD 450–514 M solo en baterías).
- **Los datos CAMMESA a nivel provincial son menos granulares.** La distribución horaria dentro de San Juan se infiere.
- **No se evaluó nueva generación firme provincial** (hidro nueva, geotermia) que podría cerrar parte de la brecha.
- **Las proyecciones de exportaciones son del gobierno.** Sesgo potencial de optimismo.

---

## 11. Escenarios: qué puede pasar

| Escenario | Descripción | Resultado probable |
|---|---|---|
| 1. Coordinado | ENRE establece tronco regional compartido. BHP, McEwen y Glencore co-invierten. | Brecha cubierta ~2033–2035. Costo transmisión 50–60% menor. |
| 2. Fragmentado | Cada operador construye su propia línea. Sin coordinación. | Sobrecosto ~USD 2.300 M adicionales (Tier 3). Cuello de botella en nodo SJ. |
| 3. Estatal | TRANSENER o empresa regional licitada por el Estado financia el tronco. | Viable pero lento: licitación, financiamiento. Horizonte 2035+. |
| 4. Demora | Conflicto regulatorio se prolonga >2 años sin resolución. | Josemaría arranca con generación propia (térmica). Los Azules y El Pachón demoran. |

---

## 12. Tabla resumen: todos los números clave

| # | Dato | Valor | Nivel |
|---|---|---|---|
| 1 | Demanda Josemaría | 260 MW | Tier 1 — ENRE Res. 79/2026 |
| 2 | Demanda Los Azules | 119 MW | Tier 1 — NI 43-101, nov. 2025 |
| 3 | Demanda El Pachón (estimada) | ~600 MW | Tier 3 — benchmark |
| 4 | Demanda clúster total | 1.500+ MW | Tier 2 — CEO Glencore Argentina |
| 5 | Filo del Sol + expansiones | ~521 MW residual | Residual aritmético — ver nota |
| 6 | Generación instalada San Juan | 861 MW | Tier 1 — EPSE, feb. 2025 |
| 7 | Generación firme San Juan | ~258 MW | Tier 1 — EPSE |
| 8 | Demanda pico provincial 2021 | 551 MW | Tier 1 — EPRE, Anuario 2021 |
| 9 | Brecha de transporte minero 2030 | ~119 MW | Calculado: 379 − 260 (Tier 1-base) |
| 10 | Demanda prov. 2030 (CAGR 2%) | 658,5 MW | Script 08 — Tier 1-base |
| 11 | Demanda prov. 2030 (CAGR 3,75%) | 767,4 MW | Script 08 — supuesto modelo |
| 12 | Déficit nocturno 2025 | 338,4 MW | Script 09 — cota sup. (Tier 3) |
| 13 | Déficit nocturno 2030 | 779,5 MW | Script 09 — cota sup. (Tier 3) |
| 14 | Déficit nocturno 2036 | 1.462,6 MW | Script 09 — cota sup. (Tier 3) |
| 15 | FC solar real San Juan (CAMMESA 2024) | 26,0% | Script 10 — Tier 1 derivado |
| 16 | MW solar para Los Azules 24/7 (FC 26%) | 497 MW | Script 10 — Tier 3 |
| 17 | BESS para Los Azules 24/7 | 1.606,5 MWh | Script 10 — Tier 3 |
| 18 | Costo BESS (mercado 2024–2025) | USD 450–514 M | Script 10 — Tier 3 |
| 19 | Costo benchmark 500 kV (plano) | ~USD 4,57 M/km | Tier 2 — licitación TRANSENER |
| 20 | Sobrecosto fragmentado sur (est.) | ~USD 2.300 M adicionales | Tier 3 |
| 21 | BEV vs. ICE: cobre | 83 kg vs. 23 kg | Tier 1 — CDA / copper.org |
| 22 | Déficit Cu global 2035 (IEA) | ~30% en escenario neto cero | Tier 1 — IEA 2024 |
| 23 | Exportaciones mineras Argentina 2032 | ~USD 11.400 M/año | Tier 2 — Sec. Minería |
| 24 | Pipeline RIGI al jun. 2026 | >USD 95.000 M | Tier 2 — Sec. Minería |
| 25 | % renovable minería Chile 2024 | 78% | Tier 1 — COCHILCO 2024 |

> **⚠ Filas 10–11:** valores provienen del script 08 y son reproducibles. **Filas 12–14:** supuesto demanda nocturna = pico provincial (Tier 3). **Filas 16–18:** outputs del script 10.

---

## 13. Tarjetas de memoria: preguntas y respuestas

### Sección 0 — Conceptos

**P: ¿Cuál es la diferencia entre MW y MWh?**
R: MW es potencia (capacidad instantánea). MWh es energía (potencia × tiempo). Una mina de 260 MW continua consume 2,28 TWh/año.

**P: ¿Por qué se usa alta tensión para transmitir electricidad?**
R: Pérdidas = I² × R. Mayor tensión = menor corriente = menos pérdidas. A 500 kV: ~1%/100 km. A 132 kV: ~3–5%/100 km.

**P: ¿Qué significa que una fuente sea 'firme'?**
R: Despachable a voluntad 24/7: hidro con embalse, gas. Las minas necesitan potencia firme. El solar (70% de San Juan) es intermitente.

### Sección 2 — El boom minero

**P: ¿Cuántos kg de cobre usa un auto eléctrico vs. uno a combustión?**
R: ~83 kg (BEV) vs. ~23 kg (ICE). El auto eléctrico usa 3,6x más cobre. (Copper Development Association / copper.org)

**P: ¿Quién es el operador de Josemaría?**
R: Vicuña Corp: JV BHP 50% + Lundin Mining 50%, cerrado en enero 2025. BHP pagó USD 2.000 M por su participación.

**P: ¿Por qué la demanda de El Pachón es 'Tier 3'?**
R: No hay factibilidad publicada. Los ~600 MW se estiman por benchmark con proyectos similares de 185 kt/día en alta altitud.

### Sección 6 — El modelo

**P: ¿Cuál es la brecha de transporte minero en 2030?**
R: 119 MW. Josemaría (260 MW) + Los Azules (119 MW) demandan 379 MW. El único plan aprobado (260 MW) cubre solo a Josemaría. Brecha = 379 − 260 = 119 MW. Esta cifra NO depende del CAGR provincial.

**P: ¿Por qué hay 'dos brechas' en el modelo?**
R: La brecha de transporte minero (119 MW mínimo en 2030, fija) y la brecha de generación firme nocturna (338,4 MW hoy, 779,5 MW en 2030). La segunda existe aunque se resuelva la primera.

**P: ¿Cuánto solar + batería necesita Los Azules para funcionar 24/7?**
R: Con FC real CAMMESA 26,0%: 497 MW de solar + 1.606,5 MWh de BESS. Costo BESS ~USD 450–514 M. El BESS es fijo (13,5 h nocturnas × 119 MW) independientemente del FC. (Script 10 — Tier 3)

**P: ¿Por qué el CAGR provincial del 2% es el 'piso conservador'?**
R: Refleja el crecimiento histórico sin minería. El escenario boom (3,75%) captura 25–35k empleos directos + 3–5x indirectos. El CAGR afecta la demanda nocturna total, no la brecha de transporte minero.

### Sección 7 — Conflicto regulatorio

**P: ¿Qué dice el artículo 15 de la Ley 24.065?**
R: Principio de acceso abierto: todo agente del MEM puede usar la red de transmisión pagando la tarifa. Nadie puede monopolizarla.

**P: ¿Cuánto más caro es el modelo fragmentado vs. el coordinado?**
R: En el corredor sur (Calingasta), el modelo fragmentado suma ~USD 2.300 M adicionales (Tier 3). Benchmark: licitación TRANSENER (~USD 4,57 M/km plano, +30–50% ajuste montaña). Ver nota metodológica en sección 7.2.

### Sección 8 — Chile

**P: 78% renovable en minería chilena: ¿cómo lo lograron?**
R: PPAs de 15–20 años entre minas y generadores privados (solar + BESS). Sin subsidio estatal. La clave: reglas claras de acceso abierto + contratos que hacen bankable la inversión en renovables.

**P: Si ya hay modelo chileno, ¿por qué Argentina no lo replica?**
R: Los ingredientes físicos están (solar, minas, demanda). Lo que falta: acceso abierto funcionando y PPAs como instrumento estándar. El conflicto ENRE/RIGI es exactamente esa barrera regulatoria.

---

## 14. Pitch STAR para entrevistas

### 14.1 Versión en español

| | Qué decir |
|---|---|
| **SITUACIÓN** | San Juan está por convertirse en uno de los mayores productores de cobre del mundo, con cuatro proyectos que suman más de 1.500 MW de demanda eléctrica nueva — casi tres veces el pico histórico de la provincia. |
| **TAREA** | Evaluar si la red eléctrica puede sostener ese crecimiento, usando datos públicos reales: CAMMESA, EPRE, resoluciones ENRE, NI 43-101. |
| **ACCIÓN** | Construí un pipeline de datos en Python y pandas con **16 scripts**. Clasifiqué la evidencia en tres niveles (Tier 1/2/3). Modelé la demanda 2025–2040 con análisis de sensibilidad para El Pachón. Calculé el FC solar real desde datos CAMMESA (26,0%). Produje 21 gráficos y publiqué todo en GitHub. |
| **RESULTADO** | Hallazgo central: el problema no es generación (la provincia tiene 861 MW instalados y exporta al mediodía) sino transporte y coordinación. Ya en 2030, con solo los dos primeros proyectos, el plan aprobado queda 119 MW corto. El análisis coincidió con el debate regulatorio real: la audiencia del 3 de junio 2026 ante el ENRE discutía exactamente el cuello de botella que identifiqué. |

**Repregunta frecuente: '¿y si ponen baterías?'**

Con el FC real de San Juan (26,0%, dato CAMMESA 2024 del propio pipeline), Los Azules necesita 497 MW de solar + 1.606,5 MWh de BESS para suministrar 119 MW continuos. Las baterías solas cuestan USD 450–514 M (Tier 3). Técnicamente posible — Chile lo está haciendo con PPAs. No es gratis ni instantáneo.

Clave: el argumento no es que BESS "no sirve". Es que sin reglas claras de acceso abierto, ningún generador privado va a firmar ese PPA.

### 14.2 Versión en inglés

| | What to say |
|---|---|
| **SITUATION** | San Juan, Argentina is set to become one of the world's largest copper producers, with four major projects representing over 1,500 MW of new electricity demand — nearly three times the province's historical peak consumption. Copper demand is growing fast because EVs use 3.6x more copper than combustion cars (source: Copper Development Association), and solar panels require ~2.2 tons/MW. |
| **TASK** | I wanted to assess whether the grid could support that growth, using publicly available data: CAMMESA (Argentina's grid operator), provincial regulator reports, ENRE resolutions, and mining NI 43-101 reports. |
| **ACTION** | I built a Python/pandas data pipeline with **16 scripts**, classified all evidence into three tiers to avoid treating estimates and hard data equally, modeled demand 2025–2040 with sensitivity analysis for the most uncertain project (El Pachón, ~600 MW, no published feasibility study), calculated the real solar capacity factor from CAMMESA data (26.0%), and modeled the battery storage scenario. 21 charts, all published on GitHub. |
| **RESULT** | Central finding: the bottleneck is not generation — the province already has 861 MW installed and exports power at noon — but transmission and coordination. As early as 2030, with just the two most advanced projects online, the only approved plan (260 MW) falls 119 MW short. This matched the real regulatory debate: a public hearing before Argentina's national electricity regulator (ENRE) on June 3rd, 2026 was debating exactly the transmission access bottleneck I identified. |

**Follow-up: 'What would you do to solve the gap?'**

Start with clear open-access rules (Argentina's Law 24.065 already provides the principle) that enable long-term PPAs between mines and private renewable generators — following Chile's model.

In 2024, 78% of Chilean mining electricity came from renewables via these contracts, with no government subsidies. Just clear rules and 15-year offtake agreements that make renewable + storage projects bankable (Grenergy–Codelco PPA, 2025: 0.5 TWh/year, 24/7, solar+BESS).

The benchmark shows the coordinated model saves ~USD 2.3B vs. the fragmented model for just the southern Calingasta corridor (Tier 3). That's the economic argument for coordination.

---

## 15. La historia del proyecto: decisiones, errores y correcciones

Esta sección documenta cómo evolucionó el análisis. Es la más valiosa para entrevistas: muestra cómo pensás.

### El error del '90 MW' (v1)

Durante mucho tiempo el argumento central era que la línea al norte tenía capacidad de solo ~90 MW. Esa cifra no tenía ninguna fuente verificable. Se eliminó y se reemplazó por la realidad documentada: la línea es de 500 kV operando a 132 kV.

*Lección: un número sin fuente, por más que refuerce tu tesis, es un riesgo.*

### El error de la geografía (v1)

Se propuso un corredor único compartido como solución ideal. Al mirar las coordenadas reales, los proyectos estaban a ~150 km en dos regiones distintas: un corredor único era físicamente imposible. Se corrigió a troncos regionales.

*Lección: cruzá siempre tus propias afirmaciones contra los datos.*

### La honestidad con El Pachón (v1)

Sin factibilidad publicada, la demanda se etiqueta siempre como Tier 3 con análisis de sensibilidad.

*Lección: cuando no sabés, decílo y mostrá el rango.*

### Las fechas: Josemaría 2027 → 2030 (v2)

El primer modelo usaba 2027 como año de entrada de Josemaría, extrapolando del cronograma original de Lundin Mining. Las actualizaciones de BHP/Lundin post-JV desplazaron el objetivo a 2030. Se corrigió en v2 actualizando la fuente a los comunicados de Lundin del primer trimestre de 2025.

*Lección: los cronogramas de proyectos en alta montaña se mueven. Citar la fuente con fecha: permite detectar y corregir rápido.*

### Los costos sin fuente (v2)

La sección de costos de transmisión en v1 y parte de v2 afirmaba rangos de costo sin ninguna fuente citable, basándose solo en la cita del CEO de Glencore. En v3 se buscó activamente un benchmark público y se encontró la licitación Choele Choel–Puerto Madryn (USD 4,57 M/km, Tier 2). En v3.1 se agregó la nota metodológica sobre que la licitación es llave en mano.

*Lección: intentar cuantificar siempre; citar la fuente del benchmark y sus limitaciones. Eso es más valioso que un número de fuente opaca.*

### La inconsistencia del CAGR (v2 → v3)

La versión 2 proyectaba 25.000–35.000 empleos directos pero usaba un CAGR provincial de solo +2% como si el boom no afectara la demanda no-minera. En v3 se agregó el escenario boom (3,75%) etiquetado como supuesto del modelo.

*Lección: la coherencia interna del documento importa tanto como la precisión de cada número individual.*

### La brecha que era dos brechas (v2 → v3)

La versión 2 calculaba solo la brecha de transporte. La brecha de generación firme nocturna quedaba implícita en los datos pero nunca calculada. En v3 se agregó como sección 6.5.

*Lección: a veces el hallazgo más interesante está en los datos que ya tenés, no en los que te faltan.*

### v3 → v3.1: los números que no salían de scripts

La auditoría de la v3 detectó que varios números clave de las secciones 6.4, 6.5 y 6.6 **no coincidían con los outputs de los propios scripts**. Habían sido calculados a mano y presentados como si vinieran del pipeline. Ejemplos concretos:

- 6.4: el texto decía "~730 MW / ~760 MW" para 2030 pero la base correcta (551 MW en 2021, CAGR 2%) da 658,5 MW. El script usaba 2025 como base.
- 6.5: el texto decía "~580 MW provincial en 2030" pero el script da 658,5 MW. La demanda nocturna 2030 era "~701 MW" pero el script da 779,5 MW.
- 6.6: el texto decía "4 horas de almacenamiento" pero el balance real requiere ~13,5 h nocturnas. El FC 22–25% era un supuesto; el FC real de CAMMESA 2024 es 26,0%. Los MW solares y MWh BESS eran inconsistentes entre sí.
- Fuente del problema: secciones escritas antes de ejecutar los scripts y no actualizadas con los outputs reales.

En v3.1 todos los números de las secciones 6.4, 6.5 y 6.6 se calculan corriendo los scripts 08, 09 y 10, y se copian textualmente del output.

*Lección fundamental: si el documento afirma un número derivado del pipeline, ese número tiene que ser el output del código, no un cálculo hecho en paralelo a mano. Escribir el script, correrlo, copiar el output. En ese orden, sin excepciones.*

---

## 16. Qué habilidades demuestra (para tu carrera)

- **Sourcing y rigor:** jerarquía de evidencia Tier 1/2/3, descarte de datos sin respaldo, búsqueda de benchmarks citables, corrección activa de atribuciones incorrectas.
- **Pipeline de datos:** Python/pandas sobre datos reales y desordenados (CAMMESA, EPRE), **16 scripts**.
- **Visualización:** 21 gráficos con criterio de diseño y etiquetado honesto.
- **Modelado:** proyección temporal, análisis de sensibilidad, escenario BESS con balance energético explícito, escenario CAGR alto.
- **Reproducibilidad:** todos los números afirmados son outputs de código. Regla de oro implementada en v3.1.
- **Conocimiento de dominio:** sistema eléctrico argentino, minería de cobre, física de transmisión, RIGI, Ley 24.065.
- **Contexto global:** demanda IEA/WoodMac/S&P, modelo chileno SEN+PPA.
- **Comunicación:** README, infografías, pitch STAR en dos idiomas.

---

## 17. Qué monitorear: hitos que pueden actualizar este análisis

- **Resolución definitiva del ENRE** sobre acceso compartido a la línea San Juan–Rodeo a 500 kV (post-audiencia 3 jun. 2026).
- **Publicación de la factibilidad de El Pachón:** convertiría los ~600 MW de Tier 3 a Tier 1/2.
- **Adhesiones RIGI de los proyectos:** confirmar qué proyectos adhirieron formalmente al RIGI.
- **Cambios de cronograma de Josemaría o Los Azules:** si se corren más allá de 2030.
- **Anuncios de BESS o nueva generación firme provincial.**
- **Evolución de precios de BESS:** si los costos continúan cayendo al ritmo de 2020–2024 (~15%/año), el cálculo de la sección 6.6 mejorará significativamente hacia 2027–2030.

---

## 18. Glosario

| Término | Definición |
|---|---|
| SADI | Sistema Argentino de Interconexión: la red eléctrica nacional. |
| MEM | Mercado Eléctrico Mayorista: donde se compra/vende energía a gran escala. |
| CAMMESA | Empresa que administra el MEM y el despacho del SADI. |
| ENRE | Ente Nacional Regulador de la Electricidad (jurisdicción nacional, transporte). |
| EPRE | Ente Provincial Regulador de la Electricidad (San Juan). |
| EPSE | Energía Provincial Sociedad del Estado (San Juan). |
| RIGI | Régimen de Incentivo para Grandes Inversiones (Ley 27.742, 2024). |
| ET | Estación Transformadora: nodo donde se cambia el nivel de tensión. |
| LEAT / LAT | Línea de Extra Alta Tensión / Línea de Alta Tensión. |
| GIS | Gas-Insulated Switchgear: tecnología compacta de estación, útil en altura. |
| kV | Kilovoltio. A mayor tensión, menos pérdidas por km. |
| MW | Megavatio: unidad de potencia (capacidad instantánea). |
| MWh | Megavatio-hora: unidad de energía. MWh = MW × horas. |
| TWh | Teravatio-hora: 1.000 GWh = 1.000.000 MWh. |
| Capacidad firme | Generación despachable a voluntad (hidro con embalse, térmica). |
| Curva de pato | Patrón donde el solar deprime la demanda neta al mediodía. |
| CAGR | Tasa de crecimiento anual compuesta. |
| PPA | Power Purchase Agreement: contrato de suministro de largo plazo. |
| BESS | Battery Energy Storage System: almacenamiento en baterías. |
| Merit order | Orden de mérito: despacho por costo variable, de menor a mayor. |
| BEV | Battery Electric Vehicle: auto totalmente eléctrico a batería. |
| ICE | Internal Combustion Engine: motor a combustión. |
| NI 43-101 | National Instrument 43-101: estándar canadiense para informes técnicos de proyectos mineros. |
| COCHILCO | Comisión Chilena del Cobre. |
| SEN | Sistema Eléctrico Nacional de Chile (unificado en 2017). |
| CDA | Copper Development Association (copper.org): principal fuente de datos de contenido de cobre en aplicaciones. |
| Acceso abierto | Principio regulatorio (Art. 15, Ley 24.065): todo agente puede usar la red pagando la tarifa. |
| Factor de capacidad | Ratio entre la energía real producida y la que se habría producido a plena potencia (SJ solar real 2024: 26,0%). |

---

## 19. Fuentes

### Fuentes primarias (Tier 1)

- CAMMESA — datos.energia.gob.ar y Estadísticas 2005–2025.
- EPRE San Juan — Anuario 2021.
- EPSE San Juan — Composición de generación (feb. 2025); portal EPSE: generación solar SJ 2024 = 1.372.040 MWh.
- McEwen Copper — NI 43-101 de Los Azules (nov. 2025).
- ENRE — Resoluciones 79, 165 y 214/2026.
- Lundin Mining — Comunicado de prensa JV Vicuña (ene. 2025).
- Lundin Mining — Resource Update Josemaría (dic. 2024).
- IEA — Global Critical Minerals Outlook 2024.
- COCHILCO — "Informe Consumo de Energía en la Minería del Cobre. Actualización 2024". Fuente primaria verificada: [cochilco.cl/web/informe-consumo-de-energia-en-la-mineria-del-cobre-actualizacion-2024/](https://www.cochilco.cl/web/informe-consumo-de-energia-en-la-mineria-del-cobre-actualizacion-2024/) (Tier 1, jun. 2026). PDF descargable desde el mismo sitio.
- Ley 24.065 — Marco Regulatorio Eléctrico, Argentina (1992).
- Ley 27.742 — Ley de Bases y Puntos de Partida, Título VII RIGI (2024).
- Mindat / PorterGeo — El Pachón altitude: ~3.600–4.200 msnm.
- CDA / copper.org — Copper in Electric Vehicles: 83 kg/BEV.
- Grenergy press release / guiaminera.cl — PPA Grenergy–Codelco (15 años, 0,5 TWh/año, solar + BESS, vigente desde ene. 2026).
- argentina.gob.ar + power-technology.com/marketdata — Segunda LEAT Choele Choel–Puerto Madryn (~USD 1.600 M, 350 km).

### Declaraciones confirmadas (Tier 2)

- CEO Glencore Argentina — Expo Minera San Juan (mayo 2026).
- Vicuña Corp / BHP + Lundin — Informe técnico de Josemaría.
- Glencore — Presentación RIGI El Pachón (2024).
- Wood Mackenzie — Global Copper Demand Outlook 2024.
- S&P Global — Copper: The Green Metal (2022).
- Secretaría de Minería de la Nación — Proyecciones exportaciones (2025).
- COCHILCO 2022/2023 — Serie histórica renovables en minería chilena.

### Estimaciones por benchmark (Tier 3)

- Demanda eléctrica El Pachón: benchmark 185 kt/día en alta altitud.
- Sobrecosto modelo fragmentado sur: extrapolación de benchmark TRANSENER + ajuste terreno montañoso. Ver nota metodológica sección 7.2.
- Escenario solar + BESS (secc. 6.6): cálculo propio script 10 (FC 26,0% real CAMMESA, 13,5 h nocturnas, eficiencia 87%).
- Serie renovables minería chilena 2015–2021: estimada por tendencia.
- Demanda nocturna provincial = pico provincial (Tier 3 — sin desagregación).

---

## 20. Apéndice: estructura del repositorio

Repositorio público: **github.com/FTornello/san-juan-energy-gap**

| Script | Contenido |
|---|---|
| 00a–00e | Diagramas explicativos (flujo, mapa institucional, matriz, curva de pato, mapa geográfico) |
| 01a/01b–02 | Descarga y limpieza de datos CAMMESA y EPRE |
| 03 | EDA nacional: matriz Argentina 2005–2025 |
| 04 | Brecha San Juan: gap analysis y proporción minera |
| 05 | Caso 500 kV y conflicto regulatorio |
| 06 | Genera README y log |
| 07 | Proyección 2025–2040 + sensibilidad El Pachón |
| 08 (v3 — 08_escenario_crecimiento_alto.py) | Proyección provincial CAGR base 2% vs. boom 3,75% |
| 09 (v3 — 09_brecha_firme_dia_noche.py) | Brecha de generación firme día vs. noche |
| 10 (v3 — 10_escenario_bess.py) | Escenario solar + BESS (caso Los Azules 119 MW) |

> **Nota:** el repo incluye los scripts 08, 09 y 10 con output impreso. Todos los números de las secciones 6.4, 6.5 y 6.6 de este documento son outputs directos de esos scripts.

---

*San Juan Energy Gap — Guía de estudio profunda v3.1 | Junio 2026*
