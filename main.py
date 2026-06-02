
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

dados = pd.read_csv("missoes.csv")

print("=== SISTEMA ESPECIALISTA ===")
def agente(risco, bateria):
    if bateria < 20:
        return "Retornar para base"
    if risco == 2:
        return "Evitar rota"
    return "Prosseguir"

print(agente(2, 80))

print("\n=== REGRESSAO LINEAR ===")
X = dados[["distancia", "obstaculos"]]
y = dados["tempo_entrega"]

reg = LinearRegression()
reg.fit(X, y)

print(f"Coeficiente distancia: {reg.coef_[0]:.2f}")
print(f"Coeficiente obstaculos: {reg.coef_[1]:.2f}")
novo = pd.DataFrame({
    "distancia": [20],
    "obstaculos": [5]
})

print(f"Previsao exemplo: {reg.predict(novo)[0]:.2f}")

print("\n=== NAIVE BAYES ===")
X = dados[["distancia", "obstaculos", "clima"]]
y = dados["risco"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

nb = GaussianNB()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

print("\n=== KMEANS ===")
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
dados["cluster"] = kmeans.fit_predict(
    dados[["distancia", "obstaculos"]]
)

print(dados[["distancia","obstaculos","cluster"]].head())

print("\n=== MLP ===")
X = dados[["distancia","obstaculos","clima","bateria"]]
y = dados["sucesso"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=2000, random_state=42)
mlp.fit(X_train, y_train)

pred = mlp.predict(X_test)

print("Accuracy MLP:", accuracy_score(y_test, pred))
