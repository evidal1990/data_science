import numpy as np

# 01. Crie um array de 10 números e acesse o terceiro elemento
array_index_01 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f'Elemento procurado = {array_index_01[2]}')
print("---------------------------------------------------------")

# 02. Crie um array 2x3 e acesso o valor na segunda linha e terceira coluna
array_index_02 = np.array([
    [10, 20, 30],
    [11, 21, 31]
])
print(f'Elemento procurado = {array_index_02[1, 2]}')
print("---------------------------------------------------------")

# 03. Crie um array de 5 números e modifique o valor do primeiro elemento.
array_index_03 = np.array([10, 20, 30, 40, 50])
array_index_03[0] = 11
print(f'Novo array = {array_index_03}')
print("---------------------------------------------------------")

# 04. Crie um array 3x3 e acesse os valores da primeira linha.
array_index_04 = np.array([
    [10, 20, 30],
    [11, 21, 31],
    [12, 22, 32]
])
print(f'Elemento procurado = {array_index_04[0]}')
print("---------------------------------------------------------")

# 05. Crie um array 4x4 e acesse a submatriz 2x2 da parte inferior direita.
array_index_05 = np.array([
    [10, 20, 30, 40],
    [11, 21, 31, 41],
    [12, 22, 32, 42],
    [13, 23, 33, 43]
])
print(f'Elemento procurado = {array_index_05[2:, 2:]}')
print("---------------------------------------------------------")

# 06. Crie um array de 6 números e use fatiamento para acessar os 3 primeiros.
array_index_06 = np.array([10, 20, 30, 40, 50, 60])
print(f'Elemento procurado = {array_index_06[:3]}')
print("---------------------------------------------------------")

# 07. Crie um array 2D e use fatiamento para acessar todas as coluna da
# segunda linha.
array_index_07 = np.array([
    [10, 20, 30],
    [11, 21, 31]
])
print(f'Elemento procurado = {array_index_07[1, :]}')
print("---------------------------------------------------------")

# 08. Crie um array 2D e inverta a ordem das linhas.
array_index_08 = np.array([
    [10, 20, 30],
    [11, 21, 31]
])
print(f'Novo array = {array_index_08[::-1, :]}')
print("---------------------------------------------------------")

# 09. Crie um array 5x5 e acesse uma fatia de todas as linhas, mas somente
# as 3 primeiras colunas.
array_index_09 = np.array([
    [10, 20, 30, 40, 50],
    [11, 21, 31, 41, 51],
    [12, 22, 32, 42, 52],
    [13, 23, 33, 43, 53],
    [14, 24, 34, 44, 54]
])
print(f'Elemento procurado = {array_index_09[:, :3]}')
print("---------------------------------------------------------")

# 10. Crie um array 3x3 e inverta a ordem das colunas.
array_index_10 = np.array([
    [10, 20, 30],
    [11, 21, 31],
    [12, 22, 32]
])
print(f'Novo array = {array_index_10[:, ::-1]}')
print("---------------------------------------------------------")
