import numpy as np

# 01. Crie um array 3x3 e troque a primeira linha pela última.
array_ex01 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
array_ex01[[0, 2]] = array_ex01[[2, 0]]
print(f'Resultado esperado {array_ex01}')
print("---------------------------------------------------------")

# 02. Crie um array 4x4 e troque a primeira coluna pela última.
array_ex02 = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [50, 55, 60, 65],
    [70, 75, 80, 85],
])
array_ex02[:, [0, 3]] = array_ex02[:, [3, 0]]
print(f'Resultado esperado {array_ex02}')
print("---------------------------------------------------------")

# 03. Crie um array 3x3 e calcule a soma de todas as linhas.
array_ex03 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f'Resultado esperado {np.sum(array_ex03, axis=1)}')
print("---------------------------------------------------------")

# 04. Crie um array 3x3 e calcule a soma de todas as colunas.
array_ex04 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f'Resultado esperado {np.sum(array_ex04, axis=0)}')
print("---------------------------------------------------------")

# 05. Crie um array 3x3 e calcule a média de cada linha.
array_ex05 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f'Resultado esperado {np.mean(array_ex05, axis=1)}')
print("---------------------------------------------------------")

# 06. Crie um array 3x3 e calcule a média de cada coluna.
array_ex06 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f'Resultado esperado {np.mean(array_ex06, axis=0)}')
print("---------------------------------------------------------")

# 07. Crie um array 4x4 e remova a segunda linha.
array_ex07 = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [50, 55, 60, 65],
    [70, 75, 80, 85],
])
print(f'Resultado esperado {np.delete(array_ex07, 1, axis=0)}')
print("---------------------------------------------------------")

# 08. Crie um array 4x4 e remova a terceira coluna.
array_ex08 = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [50, 55, 60, 65],
    [70, 75, 80, 85],
])
print(f'Resultado esperado {np.delete(array_ex08, 2, axis=1)}')
print("---------------------------------------------------------")

# 09. Crie um array 3x3 e adicione uma nova linha no final.
array_ex09_old = np.array([
    [10, 15, 20],
    [30, 35, 40],
    [50, 55, 60],
])
array_ex09_new = np.vstack([array_ex09_old, [25, 45, 65]])
print(f'Resultado esperado {array_ex09_new}')
print("---------------------------------------------------------")

# 10. Crie um array 3x3 e adicione uma nova coluna no final.
array_ex10_old = np.array([
    [10, 15, 20],
    [30, 35, 40],
    [50, 55, 60],
])
array_ex10_new = np.hstack([array_ex10_old, [[25], [45], [65]]])
print(f'Resultado esperado {array_ex10_new}')
print("---------------------------------------------------------")
