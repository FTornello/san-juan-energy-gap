# ESQUELETO — Guía del relato v2 (enfoque "el cable que falta")

**Estado:** propuesta de estructura para aprobación (Fase 2). NO es el documento todavía.
**Fecha:** 16-jun-2026
**Decisión de enfoque (tomada, no se discute):**
- Eje único = **transporte de alta tensión (500 kV) a la cordillera**. La pregunta no es si San Juan
  genera lo suficiente, sino si existe el cable para llevar la demanda minera 24/7 hasta la mina.
- La mina se conecta al **SADI como gran usuario**; no se abastece de generación provincial.
- Generación provincial (matriz, curva de pato, día/noche, BESS) = **soporte, no protagonista**:
  sólo sirve para descartar la hipótesis fácil ("falta generación") y descartar la salida local
  ("pongamos solar"). Baja a párrafos, no a secciones extensas.
- **Supuesto SADI como acotación de alcance** (no como hecho probado): "el SADI nacional tiene
  generación suficiente; este análisis no evalúa la disponibilidad firme nacional hora a hora".
  Respaldo honesto: AlmaSADI muestra un sistema ajustado en reserva, no holgado.

**Regla de oro:** todo número afirmado sale de un script reproducible (07/08/09/10) o de fuente citada con tier.

---

## Arquitectura narrativa (el arco)

> **Una sola idea, repetida y probada:** *San Juan puede generar y el país puede generar — lo que no
> existe es el cable de 500 kV con capacidad para llevar esa energía 24/7 hasta las minas de la cordillera.
> Y eso ya no es teoría: en junio de 2026 ocho actores se pelearon ante el ENRE por el único cable que hay.*

El número central del relato es **119 MW** (la brecha de transporte minero en 2030, dato firme, no depende de
supuestos). El **1.500+ MW** aparece **sólo como horizonte temporal** ("a dónde va esto en los 2030s"), nunca
como la cifra que prueba la tesis.

---

## ÍNDICE PROPUESTO

### 0. Conceptos mínimos (recortado)
- **Rol:** dar las 3 herramientas que el lector necesita y nada más.
- Contenido: (0.1) MW vs MWh; (0.2) por qué alta tensión = menos pérdidas (P=I²R, 500 vs 132 kV);
  (0.3) firme vs intermitente (para el párrafo "solar no sirve de noche").
- **Recorte vs v3.1:** se saca el detalle de frecuencia/apagones (0.4) salvo una línea; no es del eje.
- Figuras: ninguna nueva. Reusar `et_diagrama` como apoyo visual de "qué es una ET / 500 kV".

### 1. Gancho — "La pelea por un solo cable" *(orden usuario #1)*
- **Rol:** abrir con la escena real del 3-jun-2026: audiencia ENRE, 13 expositores, 8+ opositores
  peleando por acceder al único 500 kV de San Juan. El conflicto ES la prueba del problema.
- Cierra con la tesis en una línea: *no falta energía, falta el cable.*
- Números: 13 expositores, 8+ opositores (Tier 2 prensa). Sin números de generación acá.
- Figura central candidata: **NUEVA — "mapa del cable que falta"** (ver Fase 3). Hoy no existe.

### 2. Descarte de la hipótesis fácil: "¿no será que falta generación?" *(orden usuario #2)*
- **Rol:** un párrafo (máx. dos) que cierra la puerta a la hipótesis equivocada y nunca más vuelve.
- Contenido comprimido:
  - San Juan tiene **861 MW instalados** (70% solar / 27% hidro / 3% gas, EPSE feb-2025); al mediodía
    **exporta** energía. → No falta generación.
  - **Pero solar no sirve de noche** y sólo ~**258 MW** son firmes → tampoco se resuelve generando local.
  - **Y de todos modos no importa**, porque la mina **no se abastece de San Juan**: se conecta al **SADI**
    como gran usuario. El problema se muda de "generar" a "transportar".
- **Aquí entra el supuesto SADI como acotación de alcance** (1–2 líneas + nota): asumimos generación
  nacional suficiente; no evaluamos disponibilidad firme hora a hora; AlmaSADI (700 MW BESS, 100 MW Cuyo)
  sugiere que la holgura firme no es un hecho dado → por eso lo declaramos como límite, no como certeza.
- Figuras: reusar **00_03 (matriz)** y/o **00_04 (curva de pato)** EN PEQUEÑO como apoyo del párrafo.
  Pierden protagonismo (antes eran centrales).

### 3. El eje: el cable que falta *(orden usuario #3 — corazón del documento)*
- **Rol:** la sección más larga y la que sostiene el resto.
- 3.1 **La geografía del problema:** minas a 250–410 km del nodo San Juan; dos corredores distintos
  (Iglesia norte: Josemaría; Calingasta sur: Los Azules / El Pachón), ~150 km entre sí → no hay corredor único.
- 3.2 **La realidad física del transporte:** línea Nueva San Juan–Rodeo diseñada 500 kV pero **opera a 132 kV**;
  para llegar a Josemaría faltan: campo 500 kV en ET Nueva San Juan, playa 500 kV en Rodeo, **LEAT Rodeo–Chaparro
  ~167 km**, **ET Chaparro 500/220 kV GIS ~3.000 msnm**, **220 kV Chaparro–Josemaría ~93 km** (verificado en
  Res. 214/2026 + prensa). Inversión LEAT ~USD 200 M (Tier 2).
- 3.3 **PIEZA DESTACADA — "la mina que se construyó su propio cable":** el acuerdo **Los Azules–YPF Luz**.
  YPF Luz **diseña, construye y financia** una línea de alta tensión que conecta Los Azules al SADI; suministro
  100% renovable desde activos de YPF Luz. → **Prueba viva del eje:** el cuello de botella es el transporte, tan
  claro que la mina lo resolvió por su cuenta en vez de esperar el cable de Vicuña. (Tier 1 vía comunicado YPF Luz,
  oct-2025 / 2026). Esto también es el puente natural hacia la sección Chile (modelo PPA + línea privada).
- Figuras: **NUEVA figura central de transporte** (esquema corredores + qué existe vs qué falta) — ver Fase 3.

### 4. La prueba con datos firmes: 119 MW en 2030 *(orden usuario #4)*
- **Rol:** convertir el eje en número defendible. **119 MW es el protagonista numérico.**
- 4.1 **El cálculo que no depende de supuestos:** Josemaría 260 MW (ENRE) + Los Azules 119 MW (NI 43-101)
  = 379 MW de demanda minera 2030; el único plan de transporte aprobado cubre 260 MW (solo Josemaría).
  **Brecha = 379 − 260 = 119 MW** (script 07; no depende del CAGR provincial). Tier 1-base.
- 4.2 **El horizonte temporal (no el número central):** hacia los 2030s el clúster apunta a **1.500+ MW**
  (CEO Glencore, Tier 2) con El Pachón (~600 MW, **Tier 3 etiquetado**) + Filo del Sol + expansiones.
  Se presenta como "a dónde escala el problema", explícitamente NO como la cifra que prueba la tesis.
- 4.3 **Por qué el solar local no cierra la brecha (párrafo, demota el BESS):** para 119 MW firmes 24/7 con
  FC solar real **26,0%** (CAMMESA 2024, script 10) harían falta **497 MW de solar + 1.606,5 MWh de BESS**
  (~USD 450–514 M solo baterías). Técnicamente posible, no gratis ni instantáneo → refuerza que la salida
  real es transporte + contrato, no generación on-site. (Antes era sección 6.6; ahora baja a párrafo.)
- Figuras: reusar **04_01 (gap analysis)** reenfocada al 119 MW; **07_01** (proyección) como apoyo del horizonte.
  El detalle día/noche (09_01) y BESS (10_01) se citan pero NO encabezan.

### 5. Jurisdicción nacional y el ENRE: por qué esto se decide en Buenos Aires *(orden usuario #5)*
- **Rol:** explicar por qué el transporte de alta tensión es jurisdicción **nacional** (no provincial) y
  cómo el conflicto regulatorio es el cuello de botella institucional.
- 5.1 **Acceso abierto (Ley 24.065, Art. 15):** nadie monopoliza una LEAT; todo agente del MEM accede pagando.
- 5.2 **La cadena de resoluciones (verificada):** **79 → 165 → 214 (fe de erratas: saca Filo del Sol, deja
  Josemaría Fase 1, 260 MW) → 219 (convoca audiencia 3-jun-2026) → resolución de fondo PENDIENTE.** Vicuña pidió
  **30 días de prórroga**; fallo no esperable antes de ~julio 2026. (Todo Tier 1 oficial / Tier 2 prensa.)
- 5.3 **El nudo concreto:** ¿puede Vicuña quedarse con prioridad sobre el 90% por 25 años? Eso debatió la
  audiencia; EPRE, Los Azules, Barrick, Gualcamayo, Hualilán, La Rioja y municipios se opusieron por acceso abierto.
- 5.4 **RIGI (Ley 27.742):** marco de incentivo que vuelve bancables las inversiones; pipeline >USD 95.000 M (Tier 2).
- 5.5 **El costo de no coordinar:** benchmark fragmentado vs coordinado en el corredor sur (~USD 2.300 M
  adicionales, Tier 3, con nota metodológica). 
- Figuras: reusar **05_01 (timeline regulatorio)** actualizado con 214/219; **05_02 (fragmentado vs coordinado)**.

### 6. El espejo de Chile: cómo se resuelve cuando las reglas funcionan *(orden usuario #6)*
- **Rol:** mostrar que el problema es solucionable y que el modelo existe al lado.
- 6.1 SEN unificado (2017) + mercado spot horario.
- 6.2 **PPAs de largo plazo** (Codelco–Atlas 2023; Grenergy 2025, 0,5 TWh/año, solar+BESS): la mina no pone
  capital en generación; el contrato hace bancable la línea + generación del privado.
- 6.3 **Resultado: 78% renovable en minería chilena 2024** (COCHILCO, Tier 1).
- 6.4 **El paralelo argentino ya empezó:** el acuerdo **Los Azules–YPF Luz** es exactamente este modelo
  (contrato + línea privada conectada al SADI). Lo que falta para escalarlo: acceso abierto resuelto.
- Figuras: reusar **chile_renovables_timeline**.

### 7. Qué NO prueba este análisis (límites honestos)
- El Pachón / Filo del Sol = Tier 3. Cronogramas 2030 pueden correrse. No se modeló perfil horario minero.
  **Disponibilidad firme nacional NO evaluada** (acotación de alcance; AlmaSADI como matiz). Datos CAMMESA
  provinciales menos granulares. No se evaluó nueva generación firme provincial.

### 8. Cierre / qué monitorear
- Resolución de fondo del ENRE (post-prórroga, ~julio 2026). Factibilidad El Pachón. Adjudicación AlmaSADI
  (19-jun-2026). FID Los Azules (fin-2026). Avance línea YPF Luz. Cronogramas Josemaría/Los Azules.

### Apéndices (se conservan de v3.1, comprimidos)
- A. Tabla resumen de números canónicos (con tier).
- B. Tarjetas de memoria (reordenadas al nuevo eje).
- C. Pitch STAR (ES/EN) — reescrito para que el "resultado" sea el 119 MW y el cable, no la generación.
- D. Historia del proyecto (incl. nueva entrada: "v1→v2: del eje generación al eje transporte").
- E. Glosario + Fuentes (sumar Res. 219/2026, AlmaSADI, YPF Luz, cadena de resoluciones verificada).

---

## Mapa: qué pasa con cada sección de la v3.1

| v3.1 | Destino en v2 | Motivo |
|---|---|---|
| 0 Conceptos | §0 recortado | Sólo MW/MWh, alta tensión, firme |
| 1 Resumen ejecutivo | Se integra al §1 gancho + §4 | El número central pasa a 119 MW |
| 2 Contexto/boom/fichas | Comprimido en §1 y §4.2 | El boom es horizonte, no eje |
| 2.4 Matriz "paradoja" | §2 (párrafo) | Descarte hipótesis generación |
| 3 Pregunta/tesis | §1 + §3 | Es el eje |
| 4 Datos/tiers | §4 + apéndice A | Se mantiene la disciplina tier |
| 5 Proceso técnico | Apéndice / §4 | Soporte, no protagonista |
| 6.1–6.3 Modelo | §4.1 | 119 MW = corazón |
| 6.4 CAGR | §4 (mención) | Demota: no afecta brecha transporte |
| 6.5 Día/noche | §2 (párrafo) | Soporte del descarte |
| 6.6 BESS | §4.3 (párrafo) | "Por qué solar local no cierra" |
| 7 Regulatorio | §5 (ampliado, verificado) | Eje institucional |
| 8 Chile | §6 (+ puente YPF Luz) | Solución/espejo |
| 9 Qué está en juego | §4.2 / §8 | Horizonte |
| 10 Qué no prueba | §7 | Se mantiene |
| 11 Escenarios | §5.5 / §8 | Coordinado vs fragmentado |
| 12–20 | Apéndices | Se conservan, comprimidos |

---

## Qué es NUEVO en v2 respecto de v3.1 (contenido, no sólo orden)
1. **Reordenamiento al eje transporte** (lo de arriba).
2. **Pieza destacada Los Azules–YPF Luz** (no existía en v3.1).
3. **Cadena de resoluciones verificada** 79→165→214→219 + prórroga 30 días (v3.1 no tenía la 219).
4. **Supuesto SADI declarado como acotación de alcance** + AlmaSADI como matiz honesto.
5. **El 1.500+ MW degradado a horizonte temporal**; el 119 MW asciende a número central.
6. **Figura central de transporte** (a definir en Fase 3) que hoy el proyecto no tiene.
