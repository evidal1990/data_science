import numpy as np

# 01. Crie um array e altere o valor de um único elemento.
array = np.array([10, 15, 20, 25, 30])
array[2] = 35
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 02. Crie um array e altere todos os valores para um valor específico.
array = np.array([10, 15, 20, 25, 30])
array[:] = 100
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 03. Crie um array e remova todos os elementos maiores que 5.
array = np.array([2, 4, 6, 8, 10])
print(f'Resultado esperado {array[array <= 5]}')
print("---------------------------------------------------------")

# 04. Crie um array e adicione um elemento no final.
array = np.array([2, 4, 6, 8])
print(f'Resultado esperado {np.append(array, 10)}')
print("---------------------------------------------------------")

# 05. Crie um array e adicione um elemento no início.
array = np.array([2, 4, 6, 8])
print(f'Resultado esperado {np.insert(array, 0, 10)}')
print("---------------------------------------------------------")

# 06. Crie um array e insira um valor em uma posição específica.
array = np.array([2, 4, 6, 8])
print(f'Resultado esperado {np.insert(array, 1, 10)}')
print("---------------------------------------------------------")

# 07. Crie um array 3x3 e altere os valores de uma linha específica.
array = np.array([[10, 15, 20], [30, 35, 40], [50, 55, 60]])
array[1, :] = [80, 85, 90]
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 08. Crie um array 3x3 e altere os valores de uma coluna específica.
array = np.array([[10, 15, 20], [30, 35, 40], [50, 55, 60]])
array[:, 0] = [80, 85, 90]
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 09. Crie um array e transforme todos os valores para negativos.
array = np.array([2, 4, 6, 8])
print(f'Resultado esperado {np.negative(array)}')
print("---------------------------------------------------------")

# 10. Crie um array e altere o tipo de dados de todos os elementos.
array = np.array([2, 4, 6, 8])
print(f'Resultado esperado {array.astype(float)}')
print("---------------------------------------------------------")
