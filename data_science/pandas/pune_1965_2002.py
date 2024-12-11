import pandas as pd

# Ler um arquivo csv e exibir todos os seus dados
df_rain_file = pd.read_csv("pune_1965_to_2002.csv")
print(df_rain_file)

# Exibir as primeiras 05 linhas
print(df_rain_file.head())

# Exibir as primeiras 10 linhas
print(df_rain_file.head(n=10))

# Exibir as últimas 05 linhas
print(df_rain_file.tail())

# Exibir as últimas 10 linhas
print(df_rain_file.tail(n=10))

# Exibir todas as colunas (Meses) exceto a coluna Year
months = df_rain_file.columns[1:]
print(months)

# Exibir todas as colunas (Meses) exceto a coluna Year
values = df_rain_file.values[:, 1:]
print(values)

# Transformar nossos dados em um DataFrame
df_rain = pd.DataFrame(values, index=df_rain_file['Year'], columns=months)
print(df_rain)

# Agregar os valores por mês (soma)
print(df_rain.sum())

# Agregar os valores por mês (média)
print(df_rain.mean())

# Informações estatísticas do DataFrame (transposto)
print(df_rain.T.describe().round())

# Informações estatísticas do DataFrame (normal)
print(df_rain.describe().round())
