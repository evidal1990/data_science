import numpy as np

# 01. Crie um array de números inteiros de 1 a 10 usando np.arange()
array = np.arange(1, 11)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 02. Crie um array de números flutuantes entre 0 e 1 usando np.linspace()
array = np.linspace(0, 1, dtype=float)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 03. Crie um array 3x3 de valores aleatórios usando np.random.rand()
array = np.random.rand(3, 3)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 04. Crie um array 3x3 de números inteiros aleatórios com valores
# entre 0 e 100.
array = np.random.randint(100, size=(3, 3))
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 05. Crie um array de números complexos
array = np.arange(1, 5, dtype=complex)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 06. Crie um array de 5 números com valores entre -5 e 5 usando np.linspace()
array = np.linspace(-5, 5, 5)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 07. Crie um array de valores negativos usando np.linspace()
array = np.linspace(-5, -1, 5)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")

# 08. Crie um array de números uniformemente distribuídos entre -1 e 1.
array = np.random.uniform(-1, 1, size=5)
print(f'Resultado esperado {array}')
print("---------------------------------------------------------")
