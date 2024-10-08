import pandas as pd

dados = pd.read_csv("dados.csv", sep=",", engine="python", encoding="utf-8")

print( "Primeira 15 linhas do conjunto Banco de Dados: ")
print(dados.head(15))
print( "Última 15 linhas do conjunto Banco de Dados: ")
print(dados.tail(15))