# Inteligencia Artificial - IUA

**Mousist, Jorge Martín**

Trabajos prácticos de la asignatura Inteligencia Artificial.

- `E2/` — Actividad 2: análisis exploratorio de datos (EDA).
  - `E2/ejercicio2.ipynb` — notebook con el EDA, ya ejecutada (todas las celdas con su salida).
  - `E2/dataset/` — CSV del dataset. La notebook usa dos: `squads_and_players.csv` y `teams.csv`.
- `E3/` — Actividad 3: presentación de 3 diapositivas sobre el mismo dataset.
  - `E3/actividad3_eda_mundial2026.pptx` — carátula + características generales + outliers y técnicas.
  - `E3/graficos.py` — genera las figuras que uso en las diapositivas.

## Actividad 2 — EDA

**Consigna:** realizar un EDA básico del dataset seleccionado: estadística descriptiva, tipos de
variables, relaciones entre variables e incluir al menos 3 gráficos.

**Dataset:** FIFA World Cup 2026, provisto por la cátedra. La unidad de análisis es el **jugador**: se cruzan
`squads_and_players` y `teams` por `team_id` para llegar a un DataFrame de
**1248 filas × 10 columnas**.

**Contenido de la notebook:**

| Sección | Contenido |
|---|---|
| 1–2 | Carga de los datos, nulos y duplicados, y un chequeo de calidad más allá de los nulos |
| 3 | Tipos de variables (numéricas continuas/discretas y categóricas nominales) |
| 4 | Estadística descriptiva: tendencia central, dispersión, forma y frecuencias |
| 5 | Outliers: detección por 1,5 × IQR, quiénes son y qué hacer con ellos |
| 6 | Relaciones entre variables: Pearson, Spearman y relación numérica–categórica |
| 7 | Los 3 gráficos |
| 8 | Conclusiones |

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
- **"Sin nulos" no es "sin errores":** hay 1241 nombres únicos para 1248 filas. Siete jugadores
  quedaron cargados con el apellido truncado en `Mc`. No afecta al análisis, porque ninguna
  conclusión depende del nombre, pero es la única falla de calidad del dataset.

## Actividad 3 — Presentación

**Consigna:** identificar características generales del dataset (tamaño, tipo de información,
curiosidades, desafíos a priori), los outliers y las técnicas que correspondería aplicar,
y resumirlo en 3 diapositivas.

**Outliers** por el criterio de 1,5 × IQR: goles 133 (10,7 %), valor de mercado 113 (9,1 %),
caps 48 (3,8 %), edad 7 (0,6 %) y altura 2 (0,2 %). Ninguno es un error de carga, así que los
conservo.

**Quiénes son:** los valores más altos corresponden a Lamine Yamal y Erling Haaland (200 millones de euros cada uno), a Cristiano Ronaldo (143 goles en 229 partidos), y a los
arqueros más veterano y más alto del torneo. Ninguno es un error de carga, así que se conservan. Como
quedan, el valor de mercado se describe con la mediana y no con el promedio, y conviene
pasarlo a escala logarítmica antes de usarlo en un modelo.

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
