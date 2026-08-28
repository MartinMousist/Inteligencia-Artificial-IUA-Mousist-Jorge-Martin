# Inteligencia Artificial - IUA

**Mousist, Jorge Martín**

Trabajos prácticos de la asignatura Inteligencia Artificial.

- `E2/` — Actividad 2: análisis exploratorio de datos (EDA).
  - `E2/ejercicio2.ipynb` — notebook con el EDA, ya ejecutada (todas las celdas con su salida).
  - `E2/dataset/` — dataset relacional del torneo (14 tablas en CSV).

## Actividad 2 — EDA

**Consigna:** realizar un EDA básico del dataset seleccionado (estadística descriptiva, tipos de
variables, relaciones entre variables, al menos 3 gráficos).

**Dataset:** FIFA World Cup 2026. La unidad de análisis es el **jugador**: se construye un único
DataFrame de **1248 filas × 26 columnas** cruzando `squads_and_players` + `teams` + `player_stats`.

**Contenido de la notebook:**

| Sección | Contenido |
|---|---|
| 1–2 | Carga de datos y primera inspección (nulos, duplicados, balance) |
| 3 | **Tipos de variables** — numéricas continuas/discretas, categóricas nominales/ordinales |
| 4 | **Estadística descriptiva** — tendencia central, dispersión, cuartiles e IQR, forma (asimetría y curtosis), estadística robusta, `describe()` |
| 5 | Variables categóricas — frecuencias, cardinalidad, concentración y entropía de Shannon |
| 6 | **Relaciones entre variables** — numérica–numérica (Pearson / Spearman / Kendall), categórica–categórica, numérica–categórica y multivariado |
| 7 | Conclusiones |

**29 gráficos** en total: histogramas, KDE, boxplots, violin plots, scatterplots, pairplot,
heatmaps de correlación y de contingencia, gráficos de torta, countplots y stripplot.

### Principales hallazgos

- **Dos familias de distribuciones.** `edad` (asimetría +0,33) y `height_cm` (−0,09) son simétricas y
  casi normales. `valor_millones` (+3,26, curtosis exceso +14,2), `caps` (+1,61) y `goals` (+5,98)
  tienen una cola derecha muy larga.
- **El valor de mercado exige estadística robusta.** Media 15,50 M€ contra mediana 6,57 M€;
  desvío estándar 23,45 contra MAD 5,07. El 10 % más caro concentra el **46,8 %** del valor total
  de todos los planteles. Una transformación `log10` lleva la asimetría de +3,26 a −0,38.
- **`group_letter` alcanza la entropía máxima** (H = H_máx = 3,585 bits): el torneo reparte
  exactamente 104 jugadores por grupo, así que es la variable menos informativa del dataset.
- **La experiencia no explica el valor:** `caps ~ valor` da ≈ 0,00 en los tres métodos de correlación.
  En cambio `edad ~ valor` = −0,22: el mercado paga proyección, no trayectoria.
- **Pearson vs. Spearman importa:** en `height_cm ~ goals`, Pearson da −0,06 (parecería no haber
  relación) pero Spearman da −0,20 y detecta la relación monótona no lineal real.
- **`elo_rating` y `fifa_ranking` son redundantes** (correlación −0,94): miden lo mismo.
- **Altura por puesto** es la relación más nítida: GK 190 > DEF 184 > FWD 182 > MID 180 cm.

## Quick start

Requiere Python >=3.10,<3.13.

```bash
python -m venv .venv
```

```bash
pip install -e .
```

```bash
jupyter notebook
```

En VS Code, seleccionar el kernel del entorno `.venv` para ejecutar las notebooks.
