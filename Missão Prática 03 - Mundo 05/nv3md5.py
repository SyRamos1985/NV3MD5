import pandas as pd
import numpy as np


dados = pd.read_csv("dados.csv", sep=",", engine="python", encoding="utf-8")

print("Informações detalhada do conjunto Banco de Dados:")
print(dados.info())
print("\n Primeira 8 linhas, da tabela conjunto Banco de Dados:\n ")
print(dados.head())
print("\n Última 8 linhas, da tabela conjunto Banco de Dados:\n ")
print(dados.tail())

dados_cod_table = dados.copy()

dados_cod_table["Calories"].fillna(0, inplace = True)
print("\nDados após a substituição dos valores nulos na coluna 'Calories': ")
print(dados_cod_table)

print(dados_cod_table).fillna("1900/01/01", inplace = True)
print("\nDados após a substituição dos valores nulos na coluna 'Date':")
print(dados_cod_table)

dados_cod_table['Date'] = pd.to_datetime(dados_cod_table["Date"], erros='coerce')
dados_cod_table['Date'] = replace(pd.Timestamp('1900-01-01'),np.nan, inplace = True) # type: ignore
dados_cod_table['Date'] = pd.Timestamp("dados_cod_table['Date'], erros='coerce'")

print('\nDados após a tentativa de conversão da coluna Date para datetime (com NaNs):\n')
print(dados_cod_table)

dados_cod_table["Date"]= dados_cod_table["Date"].replace("20201226","2020-12-26")
dados_cod_table["Date"]= pd.to_datetime(dados_cod_table['date'], errors='coerce')

print("\nDados após a conversão final da coluna 'Date'")
print(dados_cod_table)

dados_cod_table.dropna(inplace=True)
print("\nDataFrame final após a remoção dos registros com valores nulos")
print(dados_cod_table)
