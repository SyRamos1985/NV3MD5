import pandas as pd

dados = pd.read_csv("dados.csv", sep=",", engine="python", encoding="utf-8")

pd.set_option("display.max_rows", 99999)
print(dados.to_string())
              