"""Genera las tres figuras que uso en las diapositivas de la Actividad 3.

Parte del mismo DataFrame que la notebook de la Actividad 2 (E2/ejercicio2.ipynb):
squads_and_players cruzado con teams por team_id. Todos los numeros que aparecen
en los titulos y en las anotaciones se calculan aca, ninguno esta escrito a mano.

    python graficos.py
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATOS = '../E2/dataset/'
SALIDA = 'img/'

AZUL, ROJO, VERDE = '#4C72B0', '#C44E52', '#55A868'
plt.rcParams.update({'font.size': 11,
                     'axes.spines.top': False,
                     'axes.spines.right': False})


def coma(texto):
    """Usa la coma como separador decimal, que es como se escribe en el texto."""
    return texto.replace('.', ',')


jugadores = pd.read_csv(DATOS + 'squads_and_players.csv')
equipos = pd.read_csv(DATOS + 'teams.csv')

df = jugadores.merge(equipos, on='team_id')
df['edad'] = ((pd.Timestamp('2026-06-11') - pd.to_datetime(df['date_of_birth'])).dt.days / 365.25).astype(int)
df['valor_millones'] = (df['market_value_eur'] / 1_000_000).round(2)

valor = df['valor_millones']
log_valor = np.log10(valor)

# --- 1. Distribucion del valor de mercado -----------------------------------
q1, q3 = valor.quantile([0.25, 0.75])
lim_sup = q3 + 1.5 * (q3 - q1)
n_out = int((valor > lim_sup).sum())

fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.hist(valor, bins=45, color=AZUL, edgecolor='white', linewidth=.5)
ax.axvline(valor.mean(), color=ROJO, ls='--', lw=2,
           label=coma(f'promedio = {valor.mean():.1f}'))
ax.axvline(valor.median(), color=VERDE, ls='--', lw=2,
           label=coma(f'mediana = {valor.median():.1f}'))
ax.annotate(f'{n_out} jugadores valen\nmas de {lim_sup:.0f} millones',
            xy=(70, 55), xytext=(103, 300),
            arrowprops=dict(arrowstyle='->', color='#555'), fontsize=10, color='#333')
ax.set_xlabel('valor de mercado (millones de euros)')
ax.set_ylabel('cantidad de jugadores')
ax.set_title('Valor de mercado de los jugadores', fontsize=12, loc='left')
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(SALIDA + 'valor.png')
plt.close()

# --- 2. Efecto del logaritmo ------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.4), dpi=200)

axes[0].hist(valor, bins=40, color=AZUL, edgecolor='white', linewidth=.5)
axes[0].set_title(coma(f'Valor original (asimetria {valor.skew():.2f})'), fontsize=11, loc='left')
axes[0].set_xlabel('millones de euros')
axes[0].set_ylabel('jugadores')

axes[1].hist(log_valor, bins=40, color=VERDE, edgecolor='white', linewidth=.5)
axes[1].set_title(coma(f'Con logaritmo (asimetria {log_valor.skew():.2f})'), fontsize=11, loc='left')
axes[1].set_xlabel('logaritmo del valor')

plt.tight_layout()
plt.savefig(SALIDA + 'log.png')
plt.close()

# --- 3. Altura por puesto ---------------------------------------------------
orden = ['GK', 'DEF', 'MID', 'FWD']
fig, ax = plt.subplots(figsize=(4.6, 3.4), dpi=200)
ax.boxplot([df.loc[df.position == p, 'height_cm'] for p in orden],
           patch_artist=True, widths=.6,
           boxprops=dict(facecolor=AZUL, alpha=.6),
           medianprops=dict(color=ROJO, lw=2))
ax.set_xticks(range(1, len(orden) + 1))
ax.set_xticklabels(orden)
ax.set_ylabel('altura (cm)')
ax.set_title('Altura por puesto', fontsize=11, loc='left')
ax.grid(axis='y', alpha=.3)
plt.tight_layout()
plt.savefig(SALIDA + 'altura.png')
plt.close()

print('Figuras generadas en', SALIDA)
print(f'  asimetria original {valor.skew():.2f} -> con logaritmo {log_valor.skew():.2f}')
print(f'  outliers de valor: {n_out} por encima de {lim_sup:.2f} millones')
