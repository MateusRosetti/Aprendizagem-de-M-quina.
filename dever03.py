import csv

dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

dados_lista = []
with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  
    for linha in leitor:
        dados_lista.append((linha[0], int(linha[1])))


nome_digitado = input("Digite um nome: ")


encontrado = False
idades = [idade for _, idade in dados_lista]  
idade_maxima = max(idades)  

for nome, idade in dados_lista:
    if nome.lower() == nome_digitado.lower():
        encontrado = True
        if idade == idade_maxima:
            print(f"{nome} tem {idade} anos, é a pessoa mais velha da lista.")
        else:
            print(f"{nome} tem {idade} anos, não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print("Nome não encontrado.")