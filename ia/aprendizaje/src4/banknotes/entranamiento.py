import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

c_p = 0.4
#modelo = Perceptron()
# modelo = svm.SVC()
modelo = KNeighborsClassifier(n_neighbors=5)
#modelo = GaussianNB()

# #### ETAPA 0: EXTRAER DATOS ########

# #### ETAPA 1: IMPORTAR DATOS #######
# Read datos in from file
with open("banknotes.csv") as f:
    lector = csv.reader(f)
    next(lector)

    datos = []
    for fila in lector:
        diccionario = {
            "entrada": [float(cell) for cell in fila[1:3]],
            "salida": "Autentico" if fila[4] == "0" else "falso"
        }
        datos.append(diccionario)

# #### ETAPA 2: PARTIR DATSO #######
entrada = [fila["entrada"] for fila in datos]
salida = [fila["salida"] for fila in datos]
x_e, x_p, y_e, y_p = train_test_split(entrada, salida, test_size=c_p)

# ### ETAPA 3: ENTRENAR #######
modelo.fit(x_e, y_e)

# ### SUBETAPA 3.1: GUARDAR MODELO #####
import joblib
joblib.dump(modelo, "modelo.pkl")

# ### ETAPA 4: PREDECIR #######
prediciones = modelo.predict(x_p)

# ### ETAPA 5: EVALUACION #####
contador_correctas = (y_p == prediciones).sum()
contador_incorrectas = (y_p != prediciones).sum()
total = len(prediciones)
accuracy = contador_correctas / total * 100
print(f"Accuracy: {accuracy}")

