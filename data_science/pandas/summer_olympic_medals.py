import pandas as pd

# Leitura do arquivo CSV
origin_file = pd.read_csv(
    "Summer_Olympic_Medals_1976_to_2008.csv", encoding='latin-1')

# Seleção apenas os anos únicos, removendo dados faltantes, e ordenando-os
filtered_data = origin_file[
    ["Year", "City"]].drop_duplicates().dropna().sort_values("Year")

# Criação da série cronológica
summer_olympic_medals_series = pd.Series(
    data=filtered_data["City"].values, index=filtered_data["Year"].astype(int))
print(summer_olympic_medals_series)
