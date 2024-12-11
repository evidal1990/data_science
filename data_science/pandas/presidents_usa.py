import pandas as pd

df_presidents_file = pd.read_csv("us_presidents.csv")

# Exibir o nome de todos os presidentes
df_presidents = pd.Series(df_presidents_file["president"])
print(df_presidents)

# Exibir o nome de todos os presidentes em caixa alta
print(df_presidents.str.upper())
