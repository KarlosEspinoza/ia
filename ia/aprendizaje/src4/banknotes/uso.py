import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import joblib

modelo = joblib.load("modelo.pkl")


# ### ETAPA 4: PREDECIR #######
nuevo_dato = [[0.69,2.98,-3.6,-1.3]]
predicion = modelo.predict(nuevo_dato)

# ### ETAPA de REENTRENAMIENTO
if prediccion == dato_real:
    model.fit(nuevo_dato, predicion)

print(predicion)
