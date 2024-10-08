import pandas as pd

dados = pd.read_csv("dados.csv", sep=",", engine="python", encoding="utf-8")
print(dados)



