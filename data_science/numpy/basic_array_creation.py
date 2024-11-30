import numpy as np

array_creation_unidimensional = np.array([1, 2, 3, 4, 5])
print("01. Crie um array unidimensional com 5 elementos inteiros.")
print(array_creation_unidimensional)
print("---------------------------------------------------------")

array_creation_2x3 = np.array([[1.1, 1.2, 1.3], [2.1, 2.2, 2.3]])
print("02. Crie um array 2x3 com números flutuantes.")
print(array_creation_2x3)
print("---------------------------------------------------------")

print("03. Crie um array 3x3 com valores de 0 a 8.")
array_creation_3x3 = np.arange(9).reshape(3, 3)
print(array_creation_3x3)
print("---------------------------------------------------------")

print("04. Crie um array 4x4 com números aleatórios entre 0 e 10.")
array_creation_4x4 = np.random.randint(11, size=(4, 4))
print(array_creation_4x4)
print("---------------------------------------------------------")

print("05. Crie um array de 10 zeros")
array_creation_zeros = np.zeros(10, dtype=int)
print(array_creation_zeros)
print("---------------------------------------------------------")

print("06. Crie um array de 10 uns")
array_creation_ones = np.ones(10, dtype=int)
print(array_creation_ones)
print("---------------------------------------------------------")

print("07. Crie um array de 10 números espaçados entre 1 e 10 (float ou int).")
array_creation_1_to_10 = np.linspace(1, 10, num=10)
print(array_creation_1_to_10)
print("---------------------------------------------------------")

print(
    "08. Crie uma matriz identidade 3x3. Exemplo: [[1,0,0], [0,1,0], [0,0,1]]")
array_creation_identity_matrix_3x3 = np.eye(3)
print(array_creation_identity_matrix_3x3)
print("---------------------------------------------------------")

print("09. Crie um array de números negativos de -5 a -1.")
array_creation_negative_numbers = np.array(range(-5, 0))
print(array_creation_negative_numbers)
print("---------------------------------------------------------")

print("10. Crie um array de 15 números, com 5 números por linha e 3 colunas.")
array_creation_reshape_15 = np.arange(15).reshape(5, 3)
print(array_creation_reshape_15)
print("---------------------------------------------------------")
