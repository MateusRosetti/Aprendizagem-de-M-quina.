import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Criando um conjunto de dados com 10 entradas conhecidas
data = {
    "IMC": [18.5, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 35.0, 40.0],
    "Obeso": [False, False, False, False, False, True, True, True, True, True]
}


df = pd.DataFrame(data)
csv_filename = "/mnt/data/imc_obesidade.csv"
df.to_csv(csv_filename, index=False)


X = df[["IMC"]]
y = df["Obeso"]


model = DecisionTreeClassifier()
model.fit(X, y)


imc_novo = np.array([[27.0]])
previsao = model.predict(imc_novo)[0]

csv_filename, previsao