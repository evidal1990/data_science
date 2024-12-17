import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv(
    "Summer_Olympic_Medals_1976_to_2008.csv", encoding='latin-1')

# Seleção apenas os anos únicos, removendo dados faltantes, e ordenando-os
filtered_data = df[
    ["Year", "City"]].drop_duplicates().dropna().sort_values("Year")

# Criação da série cronológica
summer_olympic_medals_series = pd.Series(
    data=filtered_data["City"].values, index=filtered_data["Year"].astype(int))
print(summer_olympic_medals_series)

# Separar os nome próprios de sobrenomes, em duas colunas distintas,
# usando vírgula como seprador
df[['Surname', 'Name']] = df["Athlete"].str.split(",", n=1, expand=True)
print(df[['Surname', 'Name']])

# Obter medidas resumidas do conjunto de dados. Qual país ganhou mais medalhas?
medals_by_country = df.groupby(
    "Country")["Medal"].count().sort_values(ascending=False)
print(f'O país com mais medalhas é {medals_by_country.idxmax()}')

# Construir uma tabela mostrando quantas medalhas foram ganhas, pelos homens,
# no total em cada ano em que o evento foi realizado.

df_men = df[df["Gender"] == "Men"]
medals_by_men = df_men.groupby("Year")["Medal"].count().reset_index()
medals_by_men.columns = ["Year", "Medals_Total"]
print(medals_by_men)
