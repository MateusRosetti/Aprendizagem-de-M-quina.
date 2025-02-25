import pandas as pd
from datetime import datetime

#  entradas
conteudo = """Nome,Data_Nascimento,Data_Cadastro
Carlos Silva,15/05/1990,20/02/2025 14:30
Mariana Souza,23/09/1985,21/02/2025 09:15
Fernando Lima,08/07/1993,22/02/2025 16:45
Ana Oliveira,30/01/2000,23/02/2025 11:10
Paulo Mendes,12/12/1997,24/02/2025 18:00
"""

# arquivo
arquivo_csv = "dados.csv"

#dados
with open(arquivo_csv, "w", encoding="utf-8") as file:
    file.write(conteudo)


df = pd.read_csv(arquivo_csv, parse_dates=["Data_Nascimento", "Data_Cadastro"], dayfirst=True)


n = int(input("Digite o número do registro (0 a 4): "))

if 0 <= n < len(df):
    registro = df.iloc[n]
    print(f"{registro['Nome']}, Nascimento: {registro['Data_Nascimento'].strftime('%d/%m/%Y')}, Cadastro: {registro['Data_Cadastro'].strftime('%d/%m/%Y %H:%M')}")
else:
    print("Número inválido. Escolha entre 0 e 4.")