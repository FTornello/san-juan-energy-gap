# SAN JUAN ENERGY GAP
## Guía de estudio profunda — v3
### Infraestructura eléctrica para el boom minero de San Juan, Argentina

> **Idea fuerza:** San Juan no tiene un problema de generar energía — tiene un problema de transportarla hasta sus minas.

**Junio 2026 — Versión 3**

---

## Índice

- [0. Conceptos que tenés que entender sí o sí](#0-conceptos)
- [1. Resumen ejecutivo](#1-resumen-ejecutivo)
- [2. El contexto: por qué este proyecto importa](#2-contexto)
- [3. La pregunta central y la tesis](#3-pregunta-y-tesis)
- [4. Los datos y la jerarquía de evidencia](#4-datos)
- [5. El proceso técnico: cómo se construyó el análisis](#5-proceso-tecnico)
- [6. El modelo: la proyección de demanda 2025–2040](#6-modelo)
- [7. El conflicto regulatorio: acceso abierto, RIGI y la audiencia del 3 de junio](#7-conflicto-regulatorio)
- [8. Cómo lo resuelve Chile: el modelo SEN + PPA](#8-chile)
- [9. Qué está en juego: la apuesta de Argentina](#9-que-esta-en-juego)
- [10. Qué NO prueba este análisis](#10-que-no-prueba)
- [11. Escenarios: qué puede pasar](#11-escenarios)
- [12. Tabla resumen: todos los números clave](#12-tabla-resumen)
- [13. Tarjetas de memoria: preguntas y respuestas](#13-tarjetas)
- [14. Pitch STAR para entrevistas](#14-pitch-star)
- [15. La historia del proyecto: decisiones, errores y correcciones](#15-historia)
- [16. Qué habilidades demuestra](#16-habilidades)
- [17. Qué monitorear](#17-que-monitorear)
- [18. Glosario](#18-glosario)
- [19. Fuentes](#19-fuentes)
- [20. Apéndice: estructura del repositorio](#20-apendice)

---

## 0. Conceptos que tenés que entender sí o sí {#0-conceptos}

### 0.1 MW vs. MWh: la diferencia que más confunde

El **MW (megavatio)** es una unidad de *potencia*: la capacidad de producir energía en un instante dado. El **MWh (megavatio-hora)** es una unidad de *energía*: potencia × tiempo.

> **Ejemplo concreto**
> - Una planta de **100 MW** que trabaja **10 horas** produce **1.000 MWh**.
> - Una mina que consume **260 MW** continuos consume en un año: 260 MW × 8.760 hs = **2.277.600 MWh** (aproximadamente 2,3 TWh/año).
> - Por eso cuando decimos "Josemáría necesita 260 MW", queremos decir que en cada instante necesita esa capacidad disponible.

### 0.2 Por qué se usa alta tensión: kV y pérdidas en la línea

La fórmula clave es: **P_pérdida = I² × R**. A mayor tensión, menor corriente para la misma potencia, y las pérdidas caen al cuadrado.

> **Pérdidas por nivel de tensión**
> - **500 kV:** aproximadamente 1% de pérdidas cada 100 km.
> - **132 kV:** aproximadamente 3–5% de pérdidas cada 100 km.
> - Las minas de San Juan están a 250–410 km del nodo San Juan. En 132 kV llegaría entre un 10% y un 20% menos de energía. En 500 kV esa pérdida baja a 2–4%.

### 0.3 Generación firme vs. generación intermitente

Una fuente es **firme** si puede producir a voluntad 24/7 (hidro con embalse, gas). Es **intermitente** si solo produce cuando hay recurso natural (solar de día, eólico cuando hay viento). Las minas necesitan suministro **firme** garantizado.

- Factor de capacidad solar en San Juan: ~22–25% (produce a plena potencia solo ~2.000 hs/año de 8.760).
- Factor de capacidad hidro con embalse: ~40–60%.
- Factor de capacidad gas/vapor: >80% cuando se lo despacha.

### 0.4 Frecuencia, equilibrio y apagones

La red argentina opera a **50 Hz**. Si la demanda supera a la oferta, la frecuencia cae. Por debajo de 49 Hz los generadores se desconectan automáticamente para protegerse, y el SADI puede **fragmentarse** en islas eléctricas desconectadas, provocando un apagón masivo.

---

## 1. Resumen ejecutivo {#1-resumen-ejecutivo}

**La pregunta:** San Juan está por convertirse en uno de los polos de cobre más importantes del mundo. ¿Puede su red eléctrica sostener esa demanda?

**La respuesta:** no con la infraestructura actual. Pero el problema no es de generación — la provincia tiene 861 MW instalados y al mediodía exporta energía. El cuello de botella es el transporte, la coordinación entre proyectos y la geografía.

| Concepto | Valor | Qué significa |
|---|---|---|
| Demanda del clúster minero | 1.500+ MW | CEO Glencore Argentina, Expo Minera SJ, mayo 2026 (Tier 2) |
| Capacidad con plan aprobado | 260 MW | Solo Josemáría, vía ENRE Res. 79/2026 (Tier 1) |
| Brecha sin plan | ~1.240 MW | 1.500 − 260 (calculado) |
| Generación instalada provincial | 861 MW | 70% solar, 27% hidro, 3% gas (Tier 1) |
| Generación firme (despachable) | ~258 MW | Hidro + térmica, EPSE feb. 2025 (Tier 1) |
| Demanda pico provincial actual | 551 MW | Sin minería, EPRE Anuario 2021 (Tier 1) |
| Brecha mínima en 2030 | ~119 MW | Con solo Josemáría + Los Azules (cálculo Tier 1-base) |

> **▶ Estado al 9 de junio de 2026 — vigencia de este análisis**
>
> La resolución definitiva del ENRE sobre acceso compartido a la línea San Juan–Rodeo energizada a 500 kV estaba **pendiente** al cierre de este documento. La audiencia pública se realizó el 3 de junio de 2026; ENRE Res. 214/2026 corrigió el alcance pero no resolvió el fondo.
>
> La factibilidad de El Pachón no estaba publicada. Su demanda (~600 MW) sigue siendo una estimación Tier 3.
>
> Los cronogramas de Josemáría (2030) y Los Azules (2030) son los más recientes disponibles, pero pueden correrse.

---

## 2. El contexto: por qué este proyecto importa {#2-contexto}

### 2.1 El boom del cobre y la transición energética

El cobre es el metal de la transición energética. Las proyecciones de demanda global son contundentes:

| Aplicación | Cobre por unidad | Fuente |
|---|---|---|
| Auto eléctrico a batería (BEV) | ~83 kg/vehículo | IEA, Critical Minerals Outlook 2023 |
| Auto a combustión (ICE) | ~23 kg/vehículo | IEA, 2023 |
| Panel solar | ~2,2 t/MW | Wood Mackenzie, 2024 |
| Eólica offshore | ~8 t/MW | Wood Mackenzie, 2024 |

- **IEA (Global Critical Minerals Outlook 2024):** déficit proyectado de ~30% en oferta vs. demanda para 2035 en escenario neto cero. (Tier 1)
- **Wood Mackenzie (2024):** demanda global de cobre crecerá ~24% hasta 42,7 Mt en 2035. (Tier 2)
- **S&P Global (2022):** shortfall acumulado de ~10 Mt para 2040 si los proyectos en pipeline no avanzan. (Tier 2)

El cinturón andino — Chile, Perú y Argentina — concentra ~50% de las reservas globales de cobre. Argentina produce menos de 0,1 Mt/año hoy, pero podría superar 1,5 Mt/año para mediados de la década de 2030.

### 2.2 Los cuatro proyectos: fichas detalladas

#### Josemáría y Filo del Sol — Vicuña Corp (BHP 50% + Lundin Mining 50%)

| Campo | Detalle | Nivel / Fuente |
|---|---|---|
| Operador | Vicuña Corp: BHP 50% + Lundin Mining 50% (JV cerrado ene. 2025, BHP pagó USD 2.000 M) | Tier 1 — Lundin press release |
| Ubicación | Iglesia, San Juan; 3.600–4.400 msnm | Tier 1 |
| Reservas Josemáría | 1,01 Bt @ 0,30% CuEq (Cu + Au + Mo) | Tier 1 — Lundin, dic. 2024 |
| Producción (Vicuña combinado) | ~395.000 t/año CuEq | Tier 1 |
| Throughput | 175.000 t/día | Tier 1 |
| Vida útil | 25 años | Tier 1 |
| Capex Josemáría fase 1 | ~USD 7.000 M | Tier 2 |
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
| Ubicación | Calingasta, San Juan; ~4.700 msnm (la más alta) | Tier 1 |
| Recurso | ~6 Bt @ 0,43% Cu + Mo | Tier 1 — Glencore |
| Throughput plan | 185.000 t/día | Tier 2 |
| Producción estimada Cu | ~350.000 t/año | Tier 2 |
| Capex estimado | USD 8.500–10.500 M | Tier 2 — presentación RIGI |
| Vida útil | ~25 años | Tier 2 |
| Demanda eléctrica | ~600 MW | Tier 3 — estimación benchmark |
| Estado | Estudio de factibilidad en curso | Tier 1 |
| Inicio producción estimado | Fines de 2030s | Tier 2 |

### 2.3 Cómo funciona el sistema eléctrico argentino

#### Transformadores: por qué la electricidad viaja en alta tensión

La electricidad se genera entre 10 y 25 kV. Un transformador de potencia **eleva** esa tensión a 220 kV o 500 kV para el transporte. Al llegar al destino, otro transformador la **reduce** al nivel de uso. La relación de vueltas entre bobinas determina la relación de tensiones: doble de vueltas = doble de tensión, mitad de corriente, un cuarto de pérdidas.

Una estación transformadora (ET) de 500/220 kV como la que necesita Josemáría (ET Chaparro, ~3.000 msnm) puede costar entre USD 150–300 millones solo en equipamiento, más el costo civil en alta montaña.

*(Figura 17. Esquema de infraestructura eléctrica: SADI → ET 500/220 kV → mina — caso Josemáría)*

#### Despacho CAMMESA y orden de mérito

CAMMESA despacha los generadores según el **orden de mérito**: menor costo variable primero. Renovables e hidro de pasada (costo variable ≈0) siempre despachan. Gas ciclo abierto (caro) solo para picos. Esto genera la curva de pato: mucho solar al mediodía deprime la demanda neta, y las térmicas deben subir rápido al atardecer.

### 2.4 La matriz eléctrica de San Juan: la paradoja

San Juan tiene 861 MW instalados (EPSE, feb. 2025): 70% solar (~603 MW), 27% hidro (~232 MW) y 3% gas (~26 MW). Solo ~258 MW son firmes. La provincia genera de sobra durante el día y exporta energía; de noche depende de las importaciones del SADI. Las minas están a 250–410 km de distancia y necesitan potencia firme 24/7.

---

## 3. La pregunta central y la tesis {#3-pregunta-y-tesis}

> **El problema no es generación, es transporte + coordinación + geografía.**

- **Transporte:** la línea San Juan–Rodeo está diseñada para 500 kV pero opera a 132 kV. Para llegar a las minas faltan líneas y estaciones que ni existen.
- **Coordinación:** cada operador planea su propia línea. El CEO de Glencore Argentina dijo en mayo 2026 que ese modelo genera los costos más altos del mundo.
- **Geografía:** las minas están en dos regiones distintas de la cordillera, separadas ~150 km. No hay un corredor único posible.

---

## 4. Los datos y la jerarquía de evidencia {#4-datos}

### 4.1 Los tres niveles

- **Tier 1 — Fuente primaria:** documentos oficiales verificables (resoluciones ENRE, NI 43-101, anuarios EPRE, informes de factibilidad).
- **Tier 2 — Declaración confirmada:** cifra dicha públicamente por una fuente con autoridad (CEO, comunicado de prensa, presentación oficial).
- **Tier 3 — Estimación por benchmark:** inferida por comparación con proyectos similares. Siempre etiquetada explícitamente.

### 4.2 Los números canónicos

| Cifra | Valor | Nivel | Fuente |
|---|---|---|---|
| Josemáría (demanda) | 260 MW | Tier 1 | ENRE Res. 79/2026 |
| Los Azules (demanda) | 119 MW | Tier 1 | McEwen Copper, NI 43-101 (nov. 2025) |
| Clúster total | 1.500+ MW | Tier 2 | CEO Glencore Argentina (mayo 2026) |
| El Pachón (demanda est.) | ~600 MW | Tier 3 | Benchmark 185 kt/día en altitud |
| Filo del Sol + expansiones | ~521 MW residual | Residual | Ver nota ↓ |
| Demanda pico provincial | 551 MW | Tier 1 | EPRE San Juan, Anuario 2021 |
| Generación instalada | 861 MW | Tier 1 | EPSE San Juan (feb. 2025) |
| Generación firme | ~258 MW | Tier 1 | Hidro + térmica (EPSE) |

> ⚠ **Nota sobre el residual de ~521 MW (Filo del Sol + expansiones):** este valor es aritmética inversa — es lo que falta para cerrar en 1.500 MW. No proviene de ningún documento de factibilidad; hereda toda la incertidumbre de la cifra Tier 2 del CEO. Si el "1.500" fue un redondeo optimista, el error se concentra aquí. Tratar como Tier 3 a los efectos de análisis.

### 4.3 La realidad de la transmisión

- Línea San Juan–Rodeo: ~161 km, diseñada para 500 kV, opera a 132 kV.
- Para Josemáría: nueva línea 500 kV Rodeo–Chaparro (~167 km) + ET Chaparro (500/220 kV, tipo GIS, ~3.000 msnm) + línea 220 kV Chaparro–Josemáría (~93 km).
- Los Azules y El Pachón están en Calingasta (sur), ~150 km separados de Josemáría. Requieren un corredor completamente distinto.

---

## 5. El proceso técnico: cómo se construyó el análisis {#5-proceso-tecnico}

### 5.1 Stack y flujo de trabajo

Python 3, pandas, matplotlib. Cada script se escribía, se ejecutaba, se revisaba con ojo crítico y recién ahí se avanzaba. El criterio rector: honestidad sobre la calidad del dato.

### 5.2 Los datos de CAMMESA

Portal datos.energia.gob.ar, archivos CSV/Excel mensuales desde 1992. Columnas principales: *periodo* (AAAA-MM), *agente_cammesa*, *tecnologia*, *energia_gwh*, *potencia_mw*, *provincia*.

- `groupby(['provincia','tecnologia'])['energia_gwh'].sum()`: generación por provincia y tecnología.
- `pivot_table(index='periodo', columns='tecnologia', values='energia_gwh')`: composición de la matriz en el tiempo.
- `resample('Y', on='fecha')['energia_gwh'].sum()`: datos mensuales a anuales.
- `fillna(0)`: rellenar meses sin generación (solar antes de 2015).

> **Cálculo paso a paso: la brecha eléctrica**
> 1. Cargar demanda histórica EPRE. Calcular CAGR ~2%/año.
> 2. Proyectar demanda provincial con ese CAGR (supuesto etiquetado).
> 3. Sumar demanda minera: Josemáría 260 MW desde 2030, Los Azules 119 MW desde 2030, El Pachón ~600 MW desde 2036 (est.).
> 4. Demanda total = provincial + minera.
> 5. Brecha = Demanda total − 260 MW (único plan aprobado).
> 6. En 2030: 379 MW mineros + prov. vs. 260 MW con plan = **119 MW de déficit mínimo.**

### 5.3 Contexto nacional

La matriz eléctrica argentina creció de 24.124 a 44.058 MW entre 2005 y 2025 (+83%), aunque sigue siendo 57% térmica.

---

## 6. El modelo: la proyección de demanda 2025–2040 {#6-modelo}

### 6.1 La disciplina dato vs. supuesto

| Variable | Naturaleza |
|---|---|
| Demanda de cada proyecto (260, 119, ~600 MW) | Dato con fuente citada / Tier 3 etiquetado |
| Crecimiento provincial +2%/año | Supuesto conservador del modelo — ver 6.2 |
| Año de entrada de cada proyecto | Cronograma público + inferencia |

### 6.2 Los cronogramas y el escenario de crecimiento provincial

- **Josemáría:** producción objetivo 2030 (BHP/Lundin, Tier 1).
- **Los Azules:** fines 2029 / principios 2030 (McEwen, Tier 2).
- **El Pachón:** fines de 2030s (Glencore, Tier 2). Horizonte extendido a 2040.

El CAGR provincial del 2% es el **piso conservador**: refleja el crecimiento histórico de la demanda de San Juan sin minería. Pero la sección 9.2 proyecta 25.000–35.000 empleos directos en la minería y 3–5x ese número en empleos indirectos (construcción, servicios, logística). Ese boom de población y actividad económica también aumenta la demanda eléctrica no-minera. El **escenario de boom** usa un CAGR del 3,75% (punto medio del rango 3,5–4%), etiquetado como supuesto del modelo.

### 6.3 Proyección base y análisis de sensibilidad

*(Figura 12. Proyección de demanda eléctrica minera 2025–2040: escenario base)*

*(Figura 13. Análisis de sensibilidad: impacto de El Pachón según tres escenarios de demanda)*

### 6.4 Escenario de crecimiento provincial alto (nuevo en v3)

Al incorporar el CAGR boom (3,75%), la brecha se anticipa y se profundiza. La Figura 18 muestra que incluso antes de que El Pachón entre en operación, el déficit respecto del plan de 260 MW supera los 400 MW en el escenario boom.

> **Brecha 2030 según escenario de crecimiento provincial**
> - **CAGR base 2%:** demanda total 2030 ≈ 730 MW → brecha vs. plan: ~470 MW.
> - **CAGR boom 3,75%:** demanda total 2030 ≈ 760 MW → brecha vs. plan: ~500 MW.
> - La diferencia entre escenarios es ~30 MW en 2030, pero crece a ~120 MW en 2040 por el efecto acumulado del CAGR.
> - Conclusión: el escenario provincial no cambia el veredicto — la brecha es grande en ambos casos — pero sí afina la escala del problema y la urgencia del cronograma.

*(Figura 18. Proyección 2025–2040: escenario base CAGR 2% vs. escenario boom CAGR 3,75%. Supuesto del modelo — ver texto)*

### 6.5 Brecha de generación firme: el problema nocturno (nuevo en v3)

Hasta aquí la brecha se mide en MW de *transporte*. Hay una segunda capa que el documento v2 no resolvía explícitamente: la brecha de **generación firme nocturna**.

De noche, San Juan solo tiene ~258 MW firmes disponibles (hidro + térmica). Su pico de demanda provincial actual es 551 MW, lo que significa que hoy ya importa ~293 MW del SADI durante la noche. Eso es el déficit nocturno *antes* de que arranque una sola mina.

> **Cálculo del déficit nocturno proyectado**
> - **2025 (hoy):** 551 MW demanda − 258 MW firmes = ~293 MW importados del SADI de noche.
> - **2030 con Josemáría + Los Azules:** demanda nocturna total = ~580 MW provincial + 260 + 119 = ~959 MW. Firmes locales: ~258 MW. Déficit nocturno: **~701 MW**.
> - **2036 con El Pachón (escenario base):** demanda nocturna = ~630 MW provincial + 260 + 119 + 600 = ~1.609 MW. Déficit nocturno: **~1.351 MW**.
> - Para cubrir ese déficit nocturno habría que importar del SADI (requiere líneas de transmisión con capacidad suficiente) o generar localmente con fuentes firmes nuevas.

*(Figura 19. Capacidad disponible día 861 MW vs. noche 258 MW firmes y demanda total proyectada 2025–2036. El déficit nocturno se multiplica por cinco entre 2025 y 2036)*

### 6.6 Escenario solar + BESS: ¿y si ponen baterías? (nuevo en v3)

La pregunta más común en entrevistas sobre este proyecto es: ¿no alcanza con poner paneles solares y baterías para abastecer las minas? La respuesta corta es: técnicamente sí, pero la escala sorprende.

**Caso de estudio: Los Azules, 119 MW continuos 24/7.** Supuestos (todos Tier 3 — estimación ilustrativa):

- Factor de capacidad solar San Juan: 22–25%.
- Batería de 4 horas de almacenamiento (estándar de mercado).
- Eficiencia de ciclo de la batería: 87% (litio-ión, estándar de industria).

> **Resultado del cálculo BESS para Los Azules (119 MW firmes)**
> - Con FC solar 22%: se necesitan **~475 MW de placa solar** + **~1.570 MWh de batería** para dar 119 MW firmes las 24 hs.
> - Con FC solar 25%: se necesitan **~410 MW de placa solar** + **~1.430 MWh de batería**.
> - A precios de mercado 2024–2025 (~USD 280–320/kWh para BESS utilidad), solo las baterías representan **USD 400–500 M** de inversión adicional (Tier 3 — estimación, precios variables).
> - La conclusión no es que BESS "no funciona" — Chile lo está haciendo. Es que requiere **3,4–4x los MW de solar instalados respecto de la demanda**, más almacenamiento significativo. Eso hace bankable el contrato PPA, no gratuito.

*(Figura 20. Escenario solar + BESS para Los Azules 119 MW firmes 24/7. Izquierda: MW solares de placa necesarios por factor de capacidad. Derecha: MWh de batería necesarios. Tier 3 — estimación ilustrativa)*

---

## 7. El conflicto regulatorio: acceso abierto, RIGI y la audiencia del 3 de junio {#7-conflicto-regulatorio}

### 7.1 El principio de acceso abierto (Ley 24.065, Art. 15)

La Ley 24.065 de 1992 establece el principio de **acceso abierto**: todo agente del MEM tiene derecho a usar la red de transmisión pagando la cuota de transporte. Nadie puede monopolizar una línea de alta tensión.

La transmisión troncal del SADI la financian todos los usuarios del MEM vía cuota de transporte. Las líneas de conexión para grandes usuarios nuevos (como las minas) las paga el usuario. El conflicto: si Josemáría construye la línea San Juan–Rodeo a 500 kV, ¿puede cobrar acceso a Los Azules? Eso es exactamente lo que debate el ENRE.

### 7.2 El sobrecosto del modelo fragmentado: benchmark citable (nuevo en v3)

> **Benchmark: costo por km de línea 500 kV en Argentina**
> - **Fuente:** Segunda LEAT Choele Choel–Puerto Madryn: 350 km de línea doble circuito 500 kV, valor de licitación ~USD 1.600 M. (argentina.gob.ar + power-technology.com/marketdata — Tier 2)
> - **Costo unitario base:** ~USD 4,57 M/km (terreno plano patagónico).
> - **Ajuste por terreno montañoso:** +30–50% estimado (altitud, acceso vial, suelo rocoso). Rango ajustado: USD 5,9–6,9 M/km (Tier 3).

| Escenario | Infraestructura sur (Calingasta) | Costo estimado | Nivel |
|---|---|---|---|
| Coordinado | 1 línea compartida 500 kV, ~280 km | ~USD 1.800 M | Tier 3 |
| Fragmentado | 2 líneas paralelas × 280 km c/u + 2 ET adicionales | ~USD 4.100 M | Tier 3 |
| Sobrecosto fragmentado | USD ~2.300 M adicionales (+128%) | — | Tier 3 |

> ⚠ Estos números son estimaciones Tier 3: extrapoladas de un benchmark en terreno distinto, con distancias aproximadas. El valor exacto depende de la ingeniería de detalle. Lo que sí es citable: el CEO de Glencore dijo en mayo 2026 que el modelo fragmentado genera "los costos más altos del mundo", y este cálculo da una escala consistente con ese juicio.

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

- ENRE Res. 79/2026: le otorgó a Vicuña (Josemáría) prioridad por 25 años sobre el 90% de la capacidad nueva al energizar la línea a 500 kV.
- 13 oradores en la audiencia: EPRE San Juan, McEwen/Los Azules, municipios de Iglesia y Jáchal, provincia de La Rioja, asociaciones vecinales.
- ENRE Res. 214/2026: corrigió el alcance a solo Josemáría Fase 1 (eliminó a Filo del Sol). Sin resolución definitiva sobre acceso compartido al cierre de este análisis.

---

## 8. Cómo lo resuelve Chile: el modelo SEN + PPA {#8-chile}

### 8.1 El Sistema Eléctrico Nacional (SEN) chileno

Chile unificó sus dos grandes sistemas en 2017. El SEN tiene un mercado spot activo con precios horarios. En algunas horas solares el precio spot ha llegado a ser negativo por exceso de solar — esto incentiva el almacenamiento con baterías.

### 8.2 Los PPA de largo plazo

Codelco no resolvió su problema energético construyendo plantas propias. Firmó contratos de suministro de largo plazo (**PPAs**) con generadores privados de renovables:

- **Atlas Renewable Energy (2023):** PPA 15 años, solar + almacenamiento en baterías, garantía de suministro firme 24/7.
- **Grenergy (2024):** PPA para solar e hidrógeno verde a largo plazo.

El modelo: la mina no pone capital en generación; el contrato de largo plazo hace bankable el proyecto del generador para los bancos.

### 8.3 El resultado: 78% renovable en minería en 2024

Según COCHILCO, en 2024 el sector minero chileno obtuvo el **78% de su electricidad de fuentes renovables**. Meta del sector: 100% para 2030.

*(Figura 21. Electricidad renovable en minería chilena 2015–2024. Fuente: COCHILCO 2024 — 78%, Tier 1; serie 2015–2021 estimada por tendencia, Tier 3)*

La clave no es que Chile "tenga más sol". Es que tiene tres cosas que Argentina todavía no consolida: marco regulatorio de acceso abierto funcionando, PPAs de largo plazo como instrumento estándar, y almacenamiento con baterías integrado en los proyectos.

---

## 9. Qué está en juego: la apuesta de Argentina {#9-que-esta-en-juego}

| Indicador | Valor proyectado | Fuente / Año |
|---|---|---|
| Exportaciones mineras 2026 (actual) | ~USD 4.000 M/año | Sec. Minería, 2026 |
| Exportaciones mineras 2030 | ~USD 5.269 M/año | Sec. Minería, 2025 |
| Exportaciones mineras 2032 | ~USD 11.400 M/año | Sec. Minería, 2025 |
| Participación en Cu global estimada 2030 | ~2% | Sec. Minería |
| Portfolio de inversión en evaluación | >USD 28.000 M | Sec. Minería, 2025 |
| Empleo directo estimado en operación plena | 25.000–35.000 puestos | Tier 3 — estimación sectorial |

USD 11.400 M de exportaciones mineras en 2032 equivaldrían a más de la mitad de las exportaciones totales de soja de Argentina en un año típico. Representarían una transformación estructural de la balanza de pagos.

> ⚠ Las proyecciones de exportaciones son del propio gobierno argentino (Secretaría de Minería) — Tier 2 con sesgo potencial de optimismo. Leerlas como escenario favorable, no como certeza.

---

## 10. Qué NO prueba este análisis {#10-que-no-prueba}

- **La demanda de El Pachón y Filo del Sol son estimaciones (Tier 3).** Ningún documento de factibilidad publicado confirma esos números.
- **El cronograma de 2030 puede correrse.** Los proyectos en alta altitud tienen historial de demoras (regulatorio, financiero, constructivo).
- **No se modeló el perfil horario de la demanda minera.** Se asumió consumo constante 24/7 a potencia plena.
- **El almacenamiento en baterías puede cambiar el cálculo.** La sección 6.6 modela el escenario BESS para Los Azules: requiere ~410–475 MW solares de placa + ~1.430–1.570 MWh de batería para dar 119 MW firmes. Técnicamente viable; costoso.
- **Los datos CAMMESA a nivel provincial son menos granulares.** La distribución horaria dentro de San Juan se infiere.
- **No se evaluó nueva generación firme provincial** (hidro nueva, geotermia) que podría cerrar parte de la brecha por el lado de la oferta.
- **Las proyecciones de exportaciones son del gobierno.** Sesgo potencial de optimismo.

---

## 11. Escenarios: qué puede pasar {#11-escenarios}

| Escenario | Descripción | Resultado probable |
|---|---|---|
| 1. Coordinado | ENRE establece tronco regional compartido. BHP, McEwen y Glencore co-invierten. | Brecha cubierta ~2033–2035. Costo transmisión 50–60% menor. |
| 2. Fragmentado | Cada operador construye su propia línea. Sin coordinación. | Sobrecosto ~USD 2.300 M adicionales (Tier 3). Cuello de botella en nodo SJ. |
| 3. Estatal | TRANSBA o la provincia financia el tronco regional. | Viable pero lento: licitación, financiamiento. Horizonte 2035+. |
| 4. Demora | Conflicto regulatorio se prolonga >2 años sin resolución. | Josemáría arranca con generación propia (térmica). Los Azules y El Pachón demoran. |

---

## 12. Tabla resumen: todos los números clave {#12-tabla-resumen}

| # | Dato | Valor | Nivel |
|---|---|---|---|
| 1 | Demanda Josemáría | 260 MW | Tier 1 — ENRE Res. 79/2026 |
| 2 | Demanda Los Azules | 119 MW | Tier 1 — NI 43-101, nov. 2025 |
| 3 | Demanda El Pachón (estimada) | ~600 MW | Tier 3 — benchmark |
| 4 | Demanda clúster total | 1.500+ MW | Tier 2 — CEO Glencore Argentina |
| 5 | Filo del Sol + expansiones | ~521 MW residual | Residual aritmético — ver nota |
| 6 | Generación instalada San Juan | 861 MW | Tier 1 — EPSE, feb. 2025 |
| 7 | Generación firme San Juan | ~258 MW | Tier 1 — EPSE |
| 8 | Demanda pico provincial | 551 MW | Tier 1 — EPRE, Anuario 2021 |
| 9 | Brecha sin plan | ~1.240 MW | Calculado: 1.500 − 260 |
| 10 | Brecha mínima en 2030 (CAGR 2%) | ~119 MW | Calculado (Tier 1-base) |
| 11 | Brecha mínima en 2030 (CAGR 3,75%) | ~150 MW | Calculado (Tier 1 + supuesto) |
| 12 | Déficit nocturno 2030 (generación firme) | ~701 MW | Calculado (secc. 6.5) |
| 13 | Solar + BESS para Los Azules 24/7 | ~410–475 MW solar + ~1.450 MWh BESS | Tier 3 — secc. 6.6 |
| 14 | Costo benchmark 500 kV Argentina | ~USD 4,57 M/km (plano) | Tier 2 — licitación TRANSENER |
| 15 | Sobrecosto fragmentado sur (est.) | ~USD 2.300 M adicionales | Tier 3 — secc. 7.2 |
| 16 | BEV vs. ICE: cobre | 83 kg vs. 23 kg | Tier 1 — IEA 2023 |
| 17 | Déficit Cu global 2035 (IEA) | ~30% en escenario neto cero | Tier 1 — IEA 2024 |
| 18 | Exportaciones mineras Argentina 2032 | ~USD 11.400 M/año | Tier 2 — Sec. Minería |
| 19 | Pipeline RIGI al jun. 2026 | >USD 95.000 M | Tier 2 — Sec. Minería |
| 20 | % renovable minería Chile 2024 | 78% | Tier 1 — COCHILCO 2024 |

> ⚠ Fila 5 ("Filo del Sol + expansiones ~521 MW"): valor calculado por aritmética inversa para cerrar en 1.500 MW. No proviene de factibilidad. Hereda toda la incertidumbre de la cifra Tier 2 del CEO.

---

## 13. Tarjetas de memoria: preguntas y respuestas {#13-tarjetas}

### Sección 0 — Conceptos

**P: ¿Cuál es la diferencia entre MW y MWh?**
R: MW es potencia (capacidad instantánea). MWh es energía (potencia × tiempo). Una mina de 260 MW continua consume 2,28 TWh/año.

**P: ¿Por qué se usa alta tensión para transmitir electricidad?**
R: Pérdidas = I² × R. Mayor tensión = menor corriente = menos pérdidas. A 500 kV: ~1%/100 km. A 132 kV: ~3–5%/100 km.

**P: ¿Qué significa que una fuente sea "firme"?**
R: Despachable a voluntad 24/7: hidro con embalse, gas. Las minas necesitan potencia firme. El solar (70% de San Juan) es intermitente.

### Sección 2 — El boom minero

**P: ¿Cuántos kg de cobre usa un auto eléctrico vs. uno a combustión?**
R: ~83 kg (BEV) vs. ~23 kg (ICE). El auto eléctrico usa 3,6x más cobre. (IEA, 2023)

**P: ¿Quién es el operador de Josemáría?**
R: Vicuña Corp: JV BHP 50% + Lundin Mining 50%, cerrado en enero 2025. BHP pagó USD 2.000 M por su participación.

**P: ¿Por qué la demanda de El Pachón es "Tier 3"?**
R: No hay factibilidad publicada. Los ~600 MW se estiman por benchmark con proyectos similares de 185 kt/día en alta altitud.

### Sección 6 — El modelo

**P: ¿Cuál es la brecha mínima ya en 2030?**
R: ~119 MW (CAGR 2%) o ~150 MW (CAGR 3,75%). Solo con Josemáría + Los Azules vs. el único plan aprobado (260 MW).

**P: ¿Por qué hay "dos brechas" en el modelo?**
R: La brecha de transmisión (~1.240 MW sin plan) y la brecha de generación firme nocturna (~701 MW en 2030). La segunda existe aunque se resuelva la primera.

**P: ¿Cuánto solar + batería necesita Los Azules para funcionar 24/7?**
R: ~410–475 MW de placa solar + ~1.430–1.570 MWh de BESS (eficiencia 87%, 4 horas de almacenamiento). Las baterías solas cuestan ~USD 400–500 M. Técnicamente posible; requiere un PPA, no generación propia. (Tier 3)

**P: ¿Por qué el CAGR provincial del 2% es el "piso conservador"?**
R: Refleja el crecimiento histórico sin minería. El escenario boom (3,75%) captura el efecto indirecto de 25–35k empleos directos + 3–5x empleos indirectos sobre la demanda eléctrica provincial no-minera.

### Sección 7 — Conflicto regulatorio

**P: ¿Qué dice el artículo 15 de la Ley 24.065?**
R: Principio de acceso abierto: todo agente del MEM puede usar la red de transmisión pagando la tarifa. Nadie puede monopolizarla.

**P: ¿Cuánto más caro es el modelo fragmentado vs. el coordinado?**
R: En el corredor sur (Calingasta), el modelo fragmentado suma ~USD 2.300 M adicionales respecto de un tronco compartido. Tier 3 — estimación basada en benchmark licitación TRANSENER (~USD 4,57 M/km en terreno plano, +30–50% ajuste montaña).

### Sección 8 — Chile

**P: 78% renovable en minería chilena: ¿cómo lo lograron?**
R: PPAs de 15–20 años entre minas y generadores privados (solar + batería). Sin subsidio estatal. La clave: reglas claras de acceso abierto + contratos que hacen bankable la inversión en renovables.

**P: Si ya hay modelo chileno, ¿por qué Argentina no lo replica?**
R: Los ingredientes físicos están (solar, minas, demanda). Lo que falta: acceso abierto funcionando y PPAs como instrumento estándar. El conflicto ENRE/RIGI es exactamente esa barrera regulatoria.

---

## 14. Pitch STAR para entrevistas {#14-pitch-star}

### 14.1 Versión en español

| | Qué decir |
|---|---|
| **SITUACIÓN** | San Juan está por convertirse en uno de los mayores productores de cobre del mundo, con cuatro proyectos que suman más de 1.500 MW de demanda eléctrica nueva — casi tres veces el pico histórico de la provincia. |
| **TAREA** | Evaluar si la red eléctrica puede sostener ese crecimiento, usando datos públicos reales: CAMMESA, EPRE, resoluciones ENRE, NI 43-101. |
| **ACCIÓN** | Construí un pipeline de datos en Python y pandas con 13 scripts. Clasifiqué la evidencia en tres niveles (Tier 1/2/3). Modelé la demanda 2025–2040 con análisis de sensibilidad para El Pachón. Produje 21 gráficos y publiqué todo en GitHub. |
| **RESULTADO** | Hallazgo central: el problema no es generación (la provincia tiene 861 MW instalados y exporta al mediodía) sino transporte y coordinación. Ya en 2030, con solo los dos primeros proyectos, el plan aprobado queda 119 MW corto. El análisis coincidió con el debate regulatorio real: la audiencia del 3 de junio 2026 ante el ENRE discutía exactamente el cuello de botella que identifiqué. |

> **Repregunta frecuente: "¿y si ponen baterías?"**
>
> Para Los Azules (119 MW): se necesitan ~410–475 MW de solar de placa + ~1.450 MWh de BESS. Las baterías solas cuestan USD 400–500 M (Tier 3). Técnicamente posible — Chile lo está haciendo con PPAs. No es gratis ni simultáneo: es otro proyecto de inversión que requiere el mismo acceso abierto a la red para funcionar.
>
> Clave: el argumento no es que BESS "no sirve". Es que sin reglas claras de acceso abierto, ningún generador privado va a firmar ese PPA.

### 14.2 Versión en inglés (para entrevistas internacionales)

| | What to say |
|---|---|
| **SITUATION** | San Juan, Argentina is set to become one of the world's largest copper producers, with four major projects representing over 1,500 MW of new electricity demand — nearly three times the province's historical peak consumption. Copper demand is growing fast because EVs use 3.6x more copper than combustion cars, and solar panels require ~2.2 tons/MW. |
| **TASK** | I wanted to assess whether the grid could support that growth, using publicly available data: CAMMESA (Argentina's grid operator), provincial regulator reports, ENRE resolutions, and mining NI 43-101 reports. |
| **ACTION** | I built a Python/pandas data pipeline with 13 scripts, classified all evidence into three tiers to avoid treating estimates and hard data equally, modeled demand 2025–2040 with sensitivity analysis for the most uncertain project (El Pachón, ~600 MW, no published feasibility study), and added scenarios for battery storage and provincial growth. 21 charts, all published on GitHub. |
| **RESULT** | Central finding: the bottleneck is not generation — the province already has 861 MW installed and exports power at noon — but transmission and coordination. As early as 2030, with just the two most advanced projects online, the only approved plan (260 MW) falls 119 MW short. This matched the real regulatory debate: a public hearing before Argentina's national electricity regulator (ENRE) on June 3rd, 2026 was debating exactly the transmission access bottleneck I identified. |

> **Follow-up: "What would you do to solve the gap?"**
>
> Start with clear open-access rules (Argentina's Law 24.065 already provides the principle) that enable long-term PPAs between mines and private renewable generators — following Chile's model.
>
> In 2024, 78% of Chilean mining electricity came from renewables via these contracts, with no government subsidies. Just clear rules and 15–20-year offtake agreements that make renewable + storage projects bankable. The physics work. The bottleneck is regulatory.
>
> The benchmark shows the coordinated model saves ~USD 2.3B vs. the fragmented model for just the southern Calingasta corridor. That's the economic argument for coordination.

---

## 15. La historia del proyecto: decisiones, errores y correcciones {#15-historia}

### El error del "90 MW" (v1)
Durante mucho tiempo el argumento central era que la línea al norte tenía capacidad de solo ~90 MW. Esa cifra no tenía ninguna fuente verificable. Se eliminó y se reemplazó por la realidad documentada: la línea es de 500 kV operando a 132 kV.

*Lección: un número sin fuente, por más que refuerce tu tesis, es un riesgo.*

### El error de la geografía (v1)
Se propuso un corredor único compartido como solución ideal. Al mirar las coordenadas reales, los proyectos estaban a ~150 km en dos regiones distintas: un corredor único era físicamente imposible. Se corrigió a troncos regionales.

*Lección: cruzá siempre tus propias afirmaciones contra los datos.*

### La honestidad con El Pachón (v1)
Sin factibilidad publicada, la demanda se etiqueta siempre como Tier 3 con análisis de sensibilidad.

*Lección: cuando no sabés, decílo y mostrá el rango.*

### La inconsistencia del CAGR (v2 → v3)
La versión 2 proyectaba 25.000–35.000 empleos directos (sección 9.2) pero usaba un CAGR provincial de solo +2% como si el boom no afectara la demanda no-minera. Esas dos afirmaciones no podían coexistir sin reconocer la inconsistencia. En v3 se agregó el escenario boom (CAGR 3,75%) explícitamente etiquetado como supuesto del modelo.

*Lección: la coherencia interna del documento importa tanto como la precisión de cada número individual.*

### La brecha que era dos brechas (v2 → v3)
La versión 2 calculaba solo la brecha de transmisión. La sección 0.3 y la Figura 3 ya tenían los datos para calcular la brecha de generación firme nocturna, pero nadie lo había hecho explícitamente. En v3 se agregó como sección 6.5: el déficit nocturno crece de ~293 MW hoy a ~701 MW en 2030.

*Lección: a veces el hallazgo más interesante está en los datos que ya tenés, no en los que te faltan.*

### El escenario BESS (v2 → v3)
La versión 2 listaba "no se modeló almacenamiento" como limitación. En v3 se convirtió en un cálculo concreto (sección 6.6): ~410–475 MW solares + ~1.450 MWh de BESS para Los Azules. El resultado refuerza el argumento principal: BESS funciona, pero requiere PPAs y acceso abierto, no resuelve el problema sin el marco regulatorio.

*Lección: convertir una limitación en un escenario modelado es siempre más valioso que nombrarla y seguir adelante.*

### El benchmark de costos (v2 → v3)
El argumento de costos del modelo fragmentado descansaba solo en la cita del CEO de Glencore. Se buscó un benchmark público verificable: se encontró la licitación de la Segunda LEAT Choele Choel–Puerto Madryn (~USD 4,57 M/km, Tier 2). Con ese dato se construyó un cálculo Tier 3 del sobrecosto del modelo fragmentado (~USD 2.300 M adicionales). Se etiquetó explícitamente como estimación con todos sus supuestos.

*Lección: siempre intentar cuantificar; siempre etiquetar los supuestos. Si no encontrás fuente, decir que lo intentaste y por qué no lo hiciste también es valioso.*

---

## 16. Qué habilidades demuestra {#16-habilidades}

- **Sourcing y rigor:** jerarquía de evidencia Tier 1/2/3, descarte de datos sin respaldo, búsqueda de benchmarks citables.
- **Pipeline de datos:** Python/pandas sobre datos reales y desordenados (CAMMESA, EPRE).
- **Visualización:** 21 gráficos con criterio de diseño y etiquetado honesto.
- **Modelado:** proyección temporal, análisis de sensibilidad, escenario BESS, escenario CAGR alto.
- **Conocimiento de dominio:** sistema eléctrico argentino, minería de cobre, física de transmisión, RIGI, Ley 24.065.
- **Contexto global:** demanda IEA/WoodMac/S&P, modelo chileno SEN+PPA.
- **Comunicación:** README, infografías, pitch STAR en dos idiomas.

---

## 17. Qué monitorear: hitos que pueden actualizar este análisis {#17-que-monitorear}

Este análisis tiene una fecha de vigencia. Los siguientes eventos pueden cambiar significativamente las conclusiones:

1. **Resolución definitiva del ENRE** sobre acceso compartido a la línea San Juan–Rodeo a 500 kV (post-audiencia 3 jun. 2026). Si establece acceso abierto efectivo, habilita PPAs y cambia el escenario de coordinación.

2. **Publicación de la factibilidad de El Pachón:** convertiría los ~600 MW de Tier 3 a Tier 1/2, eliminando la principal fuente de incertidumbre del modelo.

3. **Adhesiones RIGI de los proyectos:** confirmar qué proyectos adhirieron formalmente al RIGI cambia el marco de estabilidad fiscal y las condiciones de financiamiento.

4. **Cambios de cronograma de Josemáría o Los Azules:** si se corren más allá de 2030, la brecha de 2030 deja de ser el hito más concreto del documento.

5. **Anuncios de BESS o nueva generación firme provincial:** un parque solar + baterías de gran escala en San Juan, o nueva generación hidro, cerraría parte de la brecha nocturna.

6. **Evolución de precios de BESS:** si los costos de baterías continúan cayendo al ritmo de 2020–2024 (~15%/año), el cálculo de la sección 6.6 mejorará significativamente hacia 2027–2030.

---

## 18. Glosario {#18-glosario}

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
| Acceso abierto | Principio regulatorio (Art. 15, Ley 24.065): todo agente puede usar la red pagando la tarifa. |
| Cuota de transporte | Cargo que pagan los agentes del MEM para financiar la transmisión troncal. |
| Factor de capacidad | Ratio entre la energía real producida y la que se habría producido a plena potencia (ej.: 22% para solar en SJ). |

---

## 19. Fuentes {#19-fuentes}

### Fuentes primarias (Tier 1)

- CAMMESA — datos.energia.gob.ar y Estadísticas 2005–2025.
- EPRE San Juan — Anuario 2021.
- EPSE San Juan — Composición de generación (feb. 2025).
- McEwen Copper — NI 43-101 de Los Azules (nov. 2025).
- ENRE — Resoluciones 79, 165 y 214/2026.
- Lundin Mining — Comunicado de prensa JV Vicuña (ene. 2025).
- Lundin Mining — Resource Update Josemáría (dic. 2024).
- IEA — Global Critical Minerals Outlook 2024.
- COCHILCO — Informe de consumo energético en la minería del cobre 2024.
- Ley 24.065 — Marco Regulatorio Eléctrico, Argentina (1992).
- Ley 27.742 — Ley de Bases y Puntos de Partida, Título VII RIGI (2024).
- argentina.gob.ar — Segunda LEAT Choele Choel–Puerto Madryn (350 km, ~USD 1.600 M): base para benchmark $/km (Tier 2).
- power-technology.com/marketdata — Choele Choel–Puerto Madryn Line (confirmación características técnicas).

### Declaraciones confirmadas (Tier 2)

- CEO Glencore Argentina — Expo Minera San Juan (mayo 2026).
- Vicuña Corp / BHP + Lundin — Informe técnico de Josemáría.
- Glencore — Presentación RIGI El Pachón (2024).
- Wood Mackenzie — Global Copper Demand Outlook 2024.
- S&P Global — Copper: The Green Metal (2022).
- Secretaría de Minería de la Nación — Proyecciones exportaciones (2025).
- COCHILCO 2022/2023 — Serie histórica renovables en minería chilena.

### Estimaciones por benchmark (Tier 3)

- Demanda eléctrica El Pachón: benchmark 185 kt/día en alta altitud.
- Sobrecosto modelo fragmentado sur: extrapolación de benchmark TRANSENER + ajuste terreno montañoso.
- Escenario solar + BESS (secc. 6.6): cálculo propio con supuestos explícitos (FC 22–25%, eficiencia 87%, 4h almacenamiento).
- Serie renovables minería chilena 2015–2021: estimada por tendencia.

---

## 20. Apéndice: estructura del repositorio {#20-apendice}

**Repositorio:** `github.com/FTornello/san-juan-energy-gap`

| Script | Contenido |
|---|---|
| 00a–00e | Diagramas explicativos (flujo, mapa institucional, matriz, curva de pato, mapa) |
| 01a/01b–02 | Descarga y limpieza de datos CAMMESA y EPRE |
| 03 | EDA nacional: matriz Argentina 2005–2025 |
| 04 | Brecha San Juan: gap analysis y proporción minera |
| 05 | Caso 500 kV y conflicto regulatorio |
| 06 | Genera README y log |
| 07 | Proyección 2025–2040 + sensibilidad El Pachón |
| 08 (nuevo v3) | Escenario crecimiento provincial alto (CAGR 3,75%) |
| 09 (nuevo v3) | Brecha de generación firme día vs. noche |
| 10 (nuevo v3) | Escenario solar + BESS (caso Los Azules 119 MW) |

---

*Junio 2026 — v3 | Francisco Tornello*
