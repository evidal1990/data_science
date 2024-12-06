import numpy as np

# 01. Crie um array e calcule a mediana dos elementos.
array_stats_ex01 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.median(array_stats_ex01)}')
print("---------------------------------------------------------")

# 02. Crie um array e calcule a variância dos elementos.
array_stats_ex02 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.var(array_stats_ex02)}')
print("---------------------------------------------------------")

# 03. Crie um array e calcule o desvio padrão.
array_stats_ex03 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.round(np.std(array_stats_ex03))}')
print("---------------------------------------------------------")

# 04. Crie um array e calcule o valor máximo.
array_stats_ex04 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.max(array_stats_ex04)}')
print("---------------------------------------------------------")

# 05. Crie um array e calcule o valor mínimo.
array_stats_ex05 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.min(array_stats_ex05)}')
print("---------------------------------------------------------")

# 06. Crie um array e calcule a soma acumulada.
array_stats_ex06 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.cumsum(array_stats_ex06)}')
print("---------------------------------------------------------")

# 07. Crie um array e calcule a soma dos elementos de cada coluna.
array_stats_ex07 = np.array([[10, 15, 20], [25, 30, 35]])
print(f'Resultado esperado = {np.sum(array_stats_ex07, axis=0)}')
print("---------------------------------------------------------")

# 08. Crie um array e calcule a soma dos elementos de cada linha.
array_stats_ex08 = np.array([[10, 15, 20], [25, 30, 35]])
print(f'Resultado esperado = {np.sum(array_stats_ex08, axis=1)}')
print("---------------------------------------------------------")

# 09. Crie um array e calcule a distribuição dos elementos (percentis).
array_stats_ex09 = np.array([50, 20, 30, 10, 40])
print(f'Percential 25o = {np.percentile(array_stats_ex09, [25])}')
print(f'Percential 50o = {np.percentile(array_stats_ex09, [50])}')
print(f'Percential 75o = {np.percentile(array_stats_ex09, [75])}')
print("---------------------------------------------------------")

# 10. Crie um array e calcule a média dos elementos.
array_stats_ex10 = np.array([50, 20, 30, 10, 40])
print(f'Resultado esperado = {np.mean(array_stats_ex10)}')
print("---------------------------------------------------------")
