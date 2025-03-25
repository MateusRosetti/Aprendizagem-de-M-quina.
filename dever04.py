import pandas as pd
import random

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]


quantidades = {}


for fruta in frutas:
    quantidade = random.randint(0, 100)
    if fruta in quantidades:
        quantidades[fruta] += quantidade
    else:
        quantidades[fruta] = quantidade


df = pd.DataFrame(list(quantidades.items()), columns=["Fruta", "Quantidade"])


arquivo = "minhas_frutas.txt"
df.to_csv(arquivo, index=False, sep=",")

df_lido = pd.read_csv(arquivo)
print(df_lido)
