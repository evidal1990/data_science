import numpy as np
from numpy import sqrt

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
print(f'Resultado da operação = {np.mean(array_ex03)}')
print("---------------------------------------------------------")

# 04. Crie um array e calcule a soma de todos os seus elementos.
array_ex04 = np.array([[10, 20], [30, 40], [50, 60]])
print(f'Resultado da operação = {np.sum(array_ex04)}')
print("---------------------------------------------------------")

# 05. Crie um array e calcule o produto de todos os seus elementos.
array_ex05 = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Resultado da operação = {np.prod(array_ex05)}')
print("---------------------------------------------------------")

# 06. Crie um array e calcule a raiz quadrada de todos os seus elementos.
array_ex06 = np.array([1, 4, 9, 16])
print(f'Resultado da operação = {np.sqrt(array_ex06)}')
print("---------------------------------------------------------")

# 07. Crie um array e calcule o logaritmo de cada valor.
array_ex07 = np.array([10, 100, 250, 500])
print(f'Resultado da operação = {np.log(array_ex07)}')
print("---------------------------------------------------------")
