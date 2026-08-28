# Inteligencia Artificial - IUA

**Mousist, Jorge Martín**

Trabajos prácticos de la asignatura Inteligencia Artificial.

- `E2/` — Actividad 2: análisis exploratorio de datos (EDA).
  - `E2/ejercicio2.ipynb` — notebook con el EDA, ya ejecutada (todas las celdas con su salida).
  - `E2/dataset/` — CSV del dataset. La notebook usa dos: `squads_and_players.csv` y `teams.csv`.

## Actividad 2 — EDA

**Consigna:** realizar un EDA básico del dataset seleccionado: estadística descriptiva, tipos de
variables, relaciones entre variables e incluir al menos 3 gráficos.

**Dataset:** FIFA World Cup 2026 (Kaggle). La unidad de análisis es el **jugador**: se cruzan
`squads_and_players` y `teams` por `team_id` para llegar a un DataFrame de
**1248 filas × 10 columnas**.

**Contenido de la notebook:**

| Sección | Contenido |
|---|---|
| 1–2 | Carga de los datos y primera inspección (nulos y duplicados) |
| 3 | Tipos de variables (numéricas continuas/discretas y categóricas nominales) |
| 4 | Estadística descriptiva: tendencia central, dispersión, forma y frecuencias |
| 5 | Relaciones entre variables: correlación numérica–numérica y numérica–categórica |
| 6 | Los 3 gráficos |
| 7 | Conclusiones |

**Los 3 gráficos:**

1. **Histograma** del valor de mercado — distribución de una variable numérica.
2. **Diagrama de dispersión** de edad vs. partidos con la selección — relación numérica–numérica.
3. **Boxplot** de altura por puesto — relación numérica–categórica.

### Principales hallazgos

- **Dos familias de distribuciones.** `edad` (asimetría +0,33) y `height_cm` (−0,09) son simétricas
  y se resumen bien con la media. `valor_millones` (+3,26), `caps` (+1,61) y `goals` (+5,98) tienen
  una cola derecha larga y hay que describirlas con la mediana y el IQR.
- **El valor de mercado exige la mediana:** media 15,50 M€ contra mediana 6,57 M€.
- **La experiencia no explica el valor:** `caps ~ valor_millones` ≈ 0,00. En cambio
  `edad ~ valor_millones` = −0,22: el mercado paga proyección, no trayectoria.
- **Lo que sí explica el valor es el equipo:** `elo_rating ~ valor_millones` = +0,57.
- **Altura por puesto** es la relación más nítida y ninguna correlación la detecta:
  GK 190 > DEF 184 > FWD 182 > MID 180 cm.

## Quick start

Requiere Python >=3.10.

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
