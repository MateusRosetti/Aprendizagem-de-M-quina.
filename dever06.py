from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Carregar o dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Treinar o modelo com KNeighborsClassifier (k=3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)  # Treinamos com todos os dados

# Receber quatro entradas do usuário
print("Digite as quatro características da flor (em cm):")
sepal_length = float(input("Comprimento da Sépala: "))
sepal_width = float(input("Largura da Sépala: "))
petal_length = float(input("Comprimento da Pétala: "))
petal_width = float(input("Largura da Pétala: "))

# Fazer a previsão
user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(user_input)

# Mostrar o nome da flor
print(f"A flor é: {iris.target_names[prediction[0]]}")