# San Juan Energy Gap: Can the Grid Support the Mining Boom?

**A data analysis project examining Argentina's electricity infrastructure
gap in the context of a historic mining expansion in San Juan province.**

---

## The Core Finding

San Juan province faces an electricity infrastructure crisis hiding in plain
sight. The mining cluster developing in the province's north — anchored by
three copper projects (Josemaría, Los Azules, and El Pachón) — will require
a combined demand exceeding **1,500 MW**, per the CEO of Glencore Argentina.
The province's current peak demand is approximately **551 MW** (EPRE, 2021).
The main transmission line to the northern mining zone — the San Juan–Rodeo
500 kV line — was built but currently operates at only **132 kV**, a fraction
of its design capacity. The regulatory fight is over energizing it at 500 kV.

Counterintuitively, this gap is not caused by a shortage of generation. San Juan
has **861 MW installed** (70% solar) and is a *net electricity exporter* during
midday solar hours. The real problem is moving power: the province cannot export
all of its surplus solar, and it cannot deliver firm, around-the-clock power to
the remote mining north. The bottleneck is transmission and coordination — and
no coordinated infrastructure plan exists to bridge it.

---

## Background: How the System Works (start here)

This project is designed to be readable without prior knowledge of how
electricity grids work. Five explanatory diagrams (scripts `00_`) build the
necessary intuition before the technical analysis begins.

**1. The flow of the system** — `00_01_flujo_sistema_electrico.png`
Electricity moves through four stages: generation → transmission →
distribution → consumption, coordinated by CAMMESA (the national operator)
and traded in the wholesale market (MEM). One physical fact anchors the whole
analysis: electricity is *not stored* on the grid. Generation must equal demand
at every instant — which is exactly why a constant, 24/7 consumer like a mine
is so demanding on the system.

**2. Who does what — province vs. nation** — `00_02_mapa_institucional.png`
Generation is sold into the *national* market; distribution is *provincial*
(Energía San Juan S.A. + DECSA buy from the MEM, and EPRE regulates them).
Mines connect as "Grandes Usuarios" directly to high-voltage transmission,
bypassing the provincial distributor entirely. High-voltage transmission is
national jurisdiction (ENRE) — which is why the 500kV line conflict is decided
by ENRE and not by the province.

**3. What San Juan actually generates** — `00_03_matriz_generacion_sanjuan.png`
San Juan has 861 MW installed (EPSE, Feb 2025): 70% solar, 27% hydro, 3% gas.
That is more than its own 551 MW peak demand — but only ~258 MW is *firm*
(dispatchable hydro + thermal). At midday the province exports surplus solar;
at night, with only firm capacity available, it falls short of its own demand
and imports from the national grid.

**4. Why abundant solar doesn't solve it** — `00_04_curva_pato.png`
The "duck curve" (a documented phenomenon coined by CAISO in 2012) shows how
solar pushes *net* demand down at midday and lets it spike at sunset. A mine
consumes a flat load 24 hours a day, including when solar output is zero. Solar
abundance cannot serve that profile without firm capacity or transmission to
import power around the clock. *(This diagram is a clearly-labeled conceptual
schematic of the phenomenon, anchored to real San Juan figures — not measured
hourly data.)*

**5. Where everything is — the geography** — `00_05_mapa_geografico.png`
A schematic map (real coordinates) showing the core spatial problem: generation
and demand sit in the central/eastern valley, while the mining projects are
strung ~230 km along the western cordillera, 250–410 km from the capital. The
gap is not only about capacity but about distance and terrain — and the projects
fall into two separate regions (north/Iglesia and south/Calingasta).

---

## Project Structure

```
analisis_sanjuan_energia/
├── data/
│   ├── raw/                    # Original files — never modified
│   │   ├── potencia_instalada_raw.csv
│   │   ├── demanda_raw.csv
│   │   ├── balance_raw.csv
│   │   └── estadisticas_2005_2025.xlsx
│   └── clean/
│       ├── matriz_nacional_long.csv
│       └── variables_referencia.csv
├── scripts/
│   ├── 00a_diagrama_sistema.py
│   ├── 00b_mapa_institucional.py
│   ├── 00c_matriz_generacion_sanjuan.py
│   ├── 00d_curva_pato.py
│   ├── 00e_mapa_geografico.py
│   ├── 01a_descarga_exploracion.py
│   ├── 01b_explorar_excel.py
│   ├── 02_limpieza.py
│   ├── 03_eda_nacional.py
│   ├── 04_analisis_san_juan.py
│   ├── 04_fix_gap_chart.py
│   ├── 05_caso_500kv.py
│   ├── 06_readme_log.py
│   ├── 07_proyeccion_demanda.py
│   ├── 08_escenario_crecimiento_alto.py
│   ├── 09_brecha_firme_dia_noche.py
│   └── 10_escenario_bess.py
├── reports/                    # All output charts (PNG) — 21 figures
├── logs/                       # Quality reports and decision logs (JSON)
└── README.md
```

---

## Data Sources

| Source | Description | Access | Last Updated |
|---|---|---|---|
| CAMMESA Open Data (datos.gob.ar) | Installed capacity, demand, MEM balance (CSV) | Public / CC Attribution | May 2026 |
| CAMMESA Annual Report 2025 | National electricity statistics 2005–2025 (Excel) | Public | May 2026 |
| ENRE Resolution 79/2026 | Vicuña priority over new capacity from 500kV energization | Public / Official | Feb 18, 2026 |
| ENRE Resolution 214/2026 | Correction: scope reduced to Josemaría Phase 1 | Public / Official | Apr 2026 |
| McEwen Copper NI 43-101 (Nov 2025) | Los Azules feasibility study — 119 MW power demand | Public / SEDAR | Nov 2025 |
| CEO Glencore Argentina — Expo Minera SJ | >1,500 MW aggregate demand for 3 projects | Public statement | May 2026 |
| Tiempo de San Juan / Econojournal / Diario de Cuyo | Regulatory conflict coverage | Public / Press | Feb–Jun 2026 |

**Note on CAMMESA CSV coverage:** The portal CSVs
(`potencia_instalada`, `demanda`, `balance`) only cover 2015–2020.
The 2005–2025 time series used for the national matrix analysis
comes from the CAMMESA Annual Report Excel file.

---

## Methodology

### Script pipeline

| Script | Input | Output | Purpose |
|---|---|---|---|
| `00_` | — (conceptual) | 5 explanatory diagrams (00_01 to 00_05) | Accessible background layer |
| `01_` | CAMMESA API URLs | 3 raw CSVs + quality report | Download & explore |
| `01b_` | `estadisticas_2005_2025.xlsx` | Sheet structure report | Excel exploration |
| `02_` | Excel file | `matriz_nacional_long.csv` | Clean & reshape (wide→long) |
| `03_` | Clean CSV | 4 charts (03_01 to 03_04) | National matrix EDA |
| `04_` | Raw CSVs + audited data | 2 charts (04_01, 04_02) | San Juan gap analysis |
| `05_` | Audited data | 3 charts (05_01 to 05_03) | 500kV case study |
| `06_` | — | README.md + project_log.json | Documentation |
| `07_` | Audited data + model assumptions | 2 charts (07_01, 07_02) | Demand projection 2025–2040 + El Pachón sensitivity |
| `08_` | Audited data + CAGR assumptions | 1 chart (08_01) | High-growth scenario (CAGR 3.75% vs 2%) |
| `09_` | Audited data | 1 chart (09_01) | Firm night-generation gap (corrected 90% sensitivity) |
| `10_` | Audited data + FC real (26.0%) | 1 chart (10_01) | BESS sizing for overnight gap |

### Key design decisions

**Why format the Excel as long (tidy) data?**
The CAMMESA Excel has years as columns (wide format). Reshaping to long
format (one row per variable × year) makes filtering, grouping, and
plotting significantly simpler with pandas and seaborn/matplotlib.

**Why combine CSV data (2015–2020) with the Excel (2005–2025)?**
The portal CSVs have machine-level granularity (useful for regional
breakdowns) but stopped updating in 2020. The Excel has the complete
2005–2025 annual series at the national aggregate level. Both are used
for what they do best.

**Why use audited research data for mining projections (not a CSV)?**
Power demand figures come from primary sources wherever possible, organized
by a clear evidence hierarchy:

- **Tier 1 — primary technical sources:** Josemaría (260 MW, ENRE Resolution
  79/2026) and Los Azules (119 MW, McEwen Copper NI 43-101 feasibility study).
- **Tier 2 — confirmed public statement:** the >1,500 MW cluster total, stated
  by the CEO of Glencore Argentina at Expo Minera San Juan (May 2026).
- **Tier 3 — benchmark estimate:** El Pachón at ~600 MW. No feasibility study
  is published yet, so this figure is derived from the project's stated
  throughput (185,000 t/day, conventional flotation) at high altitude
  (3,600–4,200 m), benchmarked against comparable Andean porphyry copper
  operations (QB2, Quellaveco). It is explicitly labeled as an estimate in
  all charts.

This tiering is deliberate: presenting a benchmark estimate transparently is
more defensible than a precise-looking figure derived from an unverifiable
residual calculation. The ~600 MW estimate replaced an earlier residual
(>1,121 MW) that incorrectly attributed the entire cluster's excess demand to
a single project.

---

## Key Charts

### Background / accessible layer (scripts 00_)

**`00_01_flujo_sistema_electrico.png`**
How electricity flows from generation through transmission and distribution to
consumption, with the roles of CAMMESA (operator) and the MEM (wholesale market).
Highlights the instantaneous-balance principle (generation = demand at all times)
and how large users like mines connect directly to high-voltage transmission.

**`00_02_mapa_institucional.png`**
Institutional map separating the national sphere (SADI, MEM, CAMMESA, ENRE) from
the provincial sphere (generation, distribution, EPRE). Shows that generation
sells to the national market while distribution is provincial, and that mining
bypasses the provincial level entirely — explaining why the 500kV conflict falls
under national (ENRE) jurisdiction.

**`00_03_matriz_generacion_sanjuan.png`**
San Juan's corrected generation matrix: 861 MW installed (70% solar, 27% hydro,
3% gas; EPSE Feb 2025). A dual panel contrasts total installed capacity with
*firm* capacity (~258 MW), illustrating why the province exports surplus solar at
midday but imports at night when only firm generation is available. This replaced
an earlier, understated local-generation figure.

**`00_04_curva_pato.png`**
The "duck curve" (CAISO, 2012): how solar generation pushes net demand down at
midday and lets it spike at sunset, contrasted against the flat 24/7 load profile
of a mine. Explicitly labeled as a conceptual schematic anchored to real San Juan
figures (551 MW peak, ~603 MW solar), not measured hourly data.

**`00_05_mapa_geografico.png`**
Schematic map (real lat/lon) of the spatial gap: generation + demand in the
central/eastern valley vs. the mining projects strung ~230 km along the western
cordillera (250–410 km from the capital). Distinguishes the existing San Juan–
Rodeo 500 kV line (operating at 132 kV) from the insufficient/absent spurs to
the mines, and groups the projects into the two regions they actually occupy
(north/Iglesia, south/Calingasta). Los Azules' coordinates are exact (technical
sheet); the others are positioned from public descriptions.

### National context (scripts 03_)

**`03_01_potencia_instalada_evolucion.png`**
Stacked bar chart showing Argentina's installed electricity capacity
by technology from 2005 to 2025. Total grew from 24,124 MW to 44,058 MW
(+83%). Thermal remains dominant (57%), but renewable capacity
(solar + wind + small hydro) grew from near zero to ~7,600 MW,
almost entirely after 2017 (RenovAr program).

**`03_02_composicion_2005_vs_2025.png`**
Donut comparison of the electricity mix in 2005 vs. 2025.
In 2005: 94% thermal + large hydro. In 2025: solar (6%) and wind (10%)
are now visible, though thermal still leads.

**`03_03_crecimiento_renovable.png`**
Growth curves for solar, wind, and total renewables under Law 26,190.
Both solar and wind were essentially zero until 2017–2018.
San Juan is Argentina's leading solar province.

**`03_04_demanda_potencia_max.png`**
National electricity demand (TWh) and peak demand (MW) 2005–2025.
Note: dual y-axis; right axis starts at ~18,000 MW, not at zero.
Demand grew +53% over 20 years; peak demand accelerated post-2020
driven by air conditioning growth and more intense heat waves.

### San Juan gap analysis (scripts 04_)

**`04_01_gap_analysis_san_juan.png`** ← *The central chart*
Horizontal bar chart contrasting the mining cluster's stacked power demand
(>1,500 MW, built up from Josemaría, Los Azules, El Pachón, and Filo del Sol +
expansions) against the only capacity that currently has a transmission plan:
Josemaría's 260 MW (ENRE Resolution 79/2026). The ~1,240 MW balance has no
coordinated solution in place. Provincial peak demand (551 MW) is shown only
as context.

**`04_02_proporcion_minera_provincial.png`**
Bar chart putting each project's power demand in perspective against
the provincial peak of 551 MW (EPRE 2021):
Josemaría is 0.5×, Los Azules 0.2×, and El Pachón ~1.1× the entire
provincial demand. El Pachón's figure is a benchmark estimate
(see methodology note below).

### Regulatory case study (scripts 05_)

**`05_01_timeline_regulatorio.png`**
Timeline of the regulatory conflict over the 500kV line, from
August 2024 (Los Azules–YPF Luz MOU) to the June 3, 2026 public hearing
on access to and use of the line.

**`05_02_modelo_fragmentado_vs_coordinado.png`**
Side-by-side diagram comparing the current model (each operator builds its own
line) against regional shared trunks. Because the projects fall into two regions
~150 km apart, a single corridor for all four is not feasible; coordination is
regional. The northern trunk (San Juan–Rodeo, 500 kV) already exists; the clearest
opportunity is a shared southern corridor (Calingasta) for Los Azules and El Pachón
instead of two parallel lines. Per the CEO of Glencore Argentina, the fragmented,
build-your-own model produces "the highest costs in the world."

**`05_03_fragmentacion_infraestructura.png`**
The concrete infrastructure chain required to power just one project — Josemaría,
the first and smallest at 260 MW. To serve it: re-energize the existing San Juan–
Rodeo line from 132 kV to 500 kV, build two new lines (~260 km total) and a new
500/220 kV substation (ET Chaparro, GIS, ~3,000 m). Los Azules, El Pachón, and
Filo del Sol each require their own chain — there is no shared-corridor plan.
(Sources: ENRE Res. 79/2026, Transener, EPRE, Minería y Desarrollo Dec. 2024.)

### Demand projection 2025–2040 (script 07_)

**`07_01_proyeccion_demanda_base.png`**
Stacked area chart projecting electricity demand through 2040, layering confirmed
project demand (Josemaría 260 MW, Los Azules 119 MW — both primary-source figures)
on top of the provincial baseline. El Pachón's ~600 MW is shown as a clearly labeled
benchmark estimate with a 400–800 MW uncertainty band. The green dashed line marks
the capacity covered by the current infrastructure plan (Vicuña's 500 kV line,
+260 MW — ENRE Res. 214/2026). Key finding: Josemaría and Los Azules reach full
operation simultaneously around 2030, adding 379 MW in approximately two years —
already exceeding the plan by ~119 MW before El Pachón enters the picture.
*Model assumptions: provincial growth +2%/yr (conservative historical CAGR);
entry timelines consistent with Vicuña Corp (2030 target) and McEwen Copper
("late 2029/early 2030"); El Pachón "late 2030s" per Glencore RIGI submission.
All timelines are model assumptions, not contractual commitments.*

**`07_02_sensibilidad_pachon.png`**
Sensitivity analysis isolating the impact of El Pachón's uncertain demand
(400 / 600 / 800 MW — illustrative range, no published feasibility figure).
The base-known trajectory (provincial + Josemaría + Los Azules, sourced from
primary documents) is shown as a shaded area; the three El Pachón scenarios
diverge from ~2034 onward. Even without El Pachón, the 2030 gap versus the
plan is approximately 119 MW. With El Pachón at base (~600 MW, ~2038), total
cluster demand reaches ~1,750 MW — none of which beyond Josemaría's 260 MW has
a coordinated transmission solution.

### High-growth scenario (script 08_)

**`08_01_proyeccion_cagr_alto.png`**
Comparison of provincial demand trajectories under two CAGR assumptions: the
conservative baseline (+2%/yr, historical CAGR) versus a high-growth scenario
(+3.75%/yr, reflecting accelerated industrial and residential load driven by
mining-sector development). By 2030, the high-growth baseline reaches 796.5 MW
vs. 658.5 MW in the conservative case — a 138 MW difference even before adding
mining project demand. By 2036, the spread widens further (1,025.0 MW vs. 741.6 MW).
This scenario quantifies the additional grid pressure if the mining boom drives
broader provincial economic activity beyond the direct project loads.
*Script output: 2030 high-CAGR provincial = 796.5 MW; 2036 = 1,025.0 MW.*

### Firm night-generation gap (script 09_)

**`09_01_brecha_dia_noche.png`**
Time-series chart (2025–2036) of the overnight firm-generation gap: total
electricity demand (provincial + mining) minus firm dispatchable capacity (~258 MW
hydro + thermal). At night, when solar output is zero, the only supply available
is firm capacity — and the mining cluster's flat 24/7 load makes this the binding
constraint. By 2030, total overnight demand reaches 1,037.5 MW (658.5 MW provincial
+ 379.0 MW mining), producing a firm-generation deficit of 779.5 MW.

**Sensitivity correction (v3.1):** A 90% load-factor sensitivity is applied
*only* to the provincial component (which has demand-side variability), not to
mining demand (which is a constant 24/7 process load). The corrected formula is:

```
déficit_90% = 658.5 × 0.90 + 379.0 − 258.0 = 713.6 MW
```

An earlier version incorrectly applied the 90% factor to the combined total
(1,037.5 × 0.90 − 258.0 = 675.7 MW), underestimating the deficit by 37.9 MW.
*Script output confirmed: Factor 90% correcto → déficit 2030 = 713.6 MW.*

### BESS sizing scenario (script 10_)

**`10_01_escenario_bess.png`**
Battery Energy Storage System (BESS) sizing analysis for Los Azules' 119 MW
overnight demand. The chart shows the required storage capacity to cover the
project's load during the 13.5 nighttime hours (when solar output is unavailable),
as a function of the solar capacity factor (FC). Using the real measured FC for
San Juan (26.0%, derived from CAMMESA/EPSE data: 1,372,040 MWh / (603 MW × 8,760 h)),
the required BESS is 119 MW × 13.5 h = **1,607 MWh**.

Note: BESS sizing depends only on the overnight load and duration, not on the
solar FC. The FC determines the daytime charge window but does not change the
nighttime discharge requirement. Using FC = 26.0% (real) vs. the commonly cited
30% (nominal) has no effect on the 1,607 MWh result.
*Script output: FC real = 26.0%; BESS sizing = 1,607 MWh for 119 MW × 13.5 h.*

---

## Key Findings Summary

1. **Argentina doubled its electricity capacity in 20 years**
   (24,124 MW → 44,058 MW), but thermal generation still dominates
   at 57% of installed capacity.

2. **The renewable boom is real but recent:** solar and wind capacity
   were near zero until 2017–2018 and reached ~7,600 MW by 2025.
   San Juan is the national leader in solar.

3. **San Juan generates plenty — but in the wrong place and the wrong form:**
   the province has 861 MW installed (EPSE, Feb 2025), 70% of it solar,
   and is a net electricity exporter during midday solar hours. However,
   only ~258 MW is firm (dispatchable hydro + thermal), and that generation
   sits in the central/eastern valley, far from the mining cordillera. The
   line toward the northern mining zone (San Juan–Rodeo) was built for 500 kV
   but operates at only 132 kV, and the spurs to the individual mines are
   insufficient or absent. San Juan therefore faces two opposite transmission
   problems at once: it cannot export all of its surplus solar, and it cannot
   deliver power to the remote mining projects. The bottleneck is transmission
   and coordination — not a shortage of generation.

4. **The mining cluster will demand >1,500 MW combined:**
   Josemaría (260 MW, under construction, ENRE filing), Los Azules
   (119 MW, feasibility approved, NI 43-101), and El Pachón
   (~600 MW estimated by benchmark, feasibility in progress). These
   three named projects sum to ~979 MW; the >1,500 MW cluster total
   cited by Glencore's CEO additionally includes Filo del Sol and
   El Pachón expansion phases. Even the conservative figure represents
   ~2.7× current provincial peak demand.

5. **The infrastructure response is fragmented:**
   Josemaría's plan covers only Josemaría. Los Azules is building a separate
   line through YPF Luz. El Pachón plans its own independent infrastructure.
   Because the projects span two regions ~150 km apart, coordination has to be
   regional — but even the clearest case (a shared southern corridor for Los
   Azules and El Pachón instead of two parallel lines) has no plan.

6. **The regulatory conflict confirms the urgency:**
   ENRE Resolution 79/2026 granted Vicuña 25-year priority access to 90% of
   the *new* capacity unlocked by energizing the line at 500 kV, triggering
   objections from 8 actors including the provincial regulator (EPRE San Juan),
   Los Azules, municipalities, and La Rioja province. The public hearing was
   held on June 3, 2026.

7. **Two projects arriving at once — the 2030 pinch point:**
   Josemaría and Los Azules are both targeting full production around 2030,
   adding 379 MW of new demand in approximately two years. The only
   infrastructure plan in place (Vicuña's 500 kV line, +260 MW) covers
   Josemaría alone — leaving a gap of roughly 119 MW even before El Pachón
   enters the picture. El Pachón's production timeline ("late 2030s",
   Glencore RIGI) lies beyond the planning horizon of current proposals.
   *(Finding from script 07; entry timelines are model assumptions consistent
   with public company statements, not contractual commitments.)*

8. **The overnight firm-generation deficit reaches 713.6 MW by 2030:**
   Applying a 90% sensitivity factor only to the provincial component
   (658.5 × 0.90 + 379.0 − 258.0), the corrected firm-generation deficit
   at peak 2030 demand is 713.6 MW. Mining demand is excluded from the
   sensitivity discount because it is a constant 24/7 process load with
   no demand-side variability. *(Finding from script 09, v3.1 correction.)*

9. **A BESS solution for Los Azules alone would require 1,607 MWh:**
   Covering the 119 MW overnight load across 13.5 nighttime hours requires
   1,607 MWh of battery storage, regardless of the solar capacity factor
   (FC = 26.0% real, derived from CAMMESA/EPSE data). *(Finding from script 10.)*

---

## Tech Stack

- **Python 3.13**
- **pandas** — data loading, cleaning, reshaping
- **matplotlib** — all visualizations
- **openpyxl** — Excel file reading
- **numpy** — numerical operations

---

## How to Reproduce

```bash
# 1. Clone the repository and navigate to the project root
cd analisis_sanjuan_energia

# 2. Install dependencies
pip3 install pandas matplotlib openpyxl numpy

# 3. Download the CAMMESA Excel manually (automated download blocked by robots.txt)
# URL: https://cammesaweb.cammesa.com/?wpdmdl=51597
# Save as: data/raw/estadisticas_2005_2025.xlsx

# 4. Run the pipeline in order
python3 scripts/00a_diagrama_sistema.py
python3 scripts/00b_mapa_institucional.py
python3 scripts/00c_matriz_generacion_sanjuan.py
python3 scripts/00d_curva_pato.py
python3 scripts/00e_mapa_geografico.py
python3 scripts/01a_descarga_exploracion.py
python3 scripts/01b_explorar_excel.py
python3 scripts/02_limpieza.py
python3 scripts/03_eda_nacional.py
python3 scripts/04_analisis_san_juan.py
python3 scripts/05_caso_500kv.py
python3 scripts/06_readme_log.py
python3 scripts/07_proyeccion_demanda.py
python3 scripts/08_escenario_crecimiento_alto.py
python3 scripts/09_brecha_firme_dia_noche.py
python3 scripts/10_escenario_bess.py
```

---

## Author

Francisco Tornello — San Juan, Argentina
Data Analytics | Customer Retention | Mining & Energy Sector Research

*This project is part of a data analytics portfolio focused on
Argentina's mining and energy sectors.*

---

*v3.1 (16 scripts, 21 figures) — Last updated: June 2026*
