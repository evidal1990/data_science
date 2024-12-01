import numpy as np
from numpy import ndim

# 01. Crie um array e verifique o número de dimensões.
array_01 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Array\n {array_01}')
array_01_dimensions = ndim(array_01)
print(f'Dimensões = {array_01_dimensions}')
print("---------------------------------------------------------")

# 02. Crie um array e verifique sua forma (shape).
array_02 = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Array\n {array_02}')
array_02_shape = np.shape(array_02)
print(f'Forma = {array_02_shape}')
print("---------------------------------------------------------")

# 03. Crie um array e verifique o tamanho total (número de elementos).
array_03 = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Array\n {array_03}')
array_03_size = np.size(array_03)
print(f'Tamanho = {array_03_size}')
print("---------------------------------------------------------")

# 04. Crie um array e verifique o tipo de dados dos elementos.
array_04_1 = np.array([1, 2, 3])
print(f'Array\n {array_04_1} com tipo {array_04_1.dtype}')
array_04_2 = np.array([1.1, 2.1, 3.1])
print(f'Array\n {array_04_2} com tipo {array_04_2.dtype}')
array_04_3 = np.array(["Acerola", "Banana", "Caju"])
print(f'Array\n {array_04_3} com tipo {array_04_3.dtype}')
array_04_4 = np.array([1, 2.1, "A"])
print(f'Array\n {array_04_4} com tipo {array_04_4.dtype}')
print("---------------------------------------------------------")

# 05. Crie um array e altere seu tipo de dado para inteiro.
array_05_float = np.array([1.1, 2.1, 3.1])
array_05_integ = array_05_float.astype(int)
print(f'Array do tipo float\n {
      array_05_float} alterado para array do tipo int\n {array_05_integ}')

# 06. Crie um array e obtenha o valor máximo.
array_06 = np.array([1, 2, 3, 4])
print(f'Array\n {array_06} com valor máximo = {array_06.max()}')
print("---------------------------------------------------------")

# 07. Crie um array e obtenha o valor mínimo.
array_07 = np.array([1, 2, 3, 4])
print(f'Array\n {array_07} com valor máximo = {array_07.min()}')
print("---------------------------------------------------------")

# 08. Crie um array e verifique o tipo de dados usando dtype
array_08_1 = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Array\n {array_08_1} com tipo de dados = {array_08_1.dtype}')
print("---------------------------------------------------------")

# 09. Crie um array 3D e verifique suas dimensões
array_09 = np.array(
    [
        [
            [1, 1], [2, 1], [3, 1]
        ],
        [
            [1, 2], [2, 2], [3, 2]
        ]
    ])
print(f'Array\n {array_09} com dimensões {array_09.shape}')
print("---------------------------------------------------------")

# 10. Crie um array e verifique seu itemsize (bytes)
array_10 = np.array(
    [
        [1, 2], [3, 4]
    ]
)
print(f'Array\n {array_10} com itemsize = {array_10.itemsize}')
