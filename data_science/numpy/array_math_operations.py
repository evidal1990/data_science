import numpy as np

# 01. Crie dois arrays e faça a soma dos elementos correspondentes
array_ex01_a = np.array([[10, 20], [11, 21], [12, 32]])
array_ex01_b = np.array([[13, 23], [14, 24], [15, 25]])
print(f'Resultado da operação = {array_ex01_a + array_ex01_b}')
print("---------------------------------------------------------")

# 02. Crie dois arrays e faça a subtração dos elementos correspondentes
array_ex02_a = np.array([[90, 60], [80, 50], [70, 40]])
array_ex02_b = np.array([[10, 15], [20, 25], [30, 35]])
print(f'Resultado da operação = {array_ex02_a - array_ex02_b}')
print("---------------------------------------------------------")

# 03. Crie um array e calcule sua média.
array_ex03 = np.array([[10, 20], [30, 40], [50, 60]])
print(f'Resultado da operação = {array_ex03.mean()}')
print("---------------------------------------------------------")

# 04. Crie um array e calcule a soma de todos os seus elementos.
array_ex04 = np.array([[10, 20], [30, 40], [50, 60]])
print(f'Resultado da operação = {array_ex04.sum()}')
print("---------------------------------------------------------")

# 05. Crie um array e calcule o produto de todos os seus elementos.
array_ex05 = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Resultado da operação = {array_ex05.prod()}')
print("---------------------------------------------------------")

# 06. Crie um array e calcule a raiz quadrada de todos os seus elementos.
array_ex06 = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Resultado da operação = {np.sqrt(array_ex06)}')
print("---------------------------------------------------------")