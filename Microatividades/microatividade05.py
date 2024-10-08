import pandas as pd


dados = pd.read_csv("dados.csv", sep=",", engine="python", encoding="utf-8")


print("Informações gerais sobre o conjunto Banco de Dados:\n")
informacoes = dados.info()
print(informacoes)

print("\nQuantidade de dados nulos em cada coluna:\n")
nulos = dados.isnull().sum()
print(nulos)






