import numpy as np
import matplotlib.pyplot as plt
import time
from pandas import read_excel
from math import inf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sympy import re
from functools import wraps
MIN_ERROR = 10**-6
MAX_EPOCAS = 100000

def print_duration(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Función {func.__name__} toma {total_time:.4f} seconds')
        return result
    return timeit_wrapper

class Perceptron:
    def __init__(self, df, numero_entradas, numero_salidas, por_test, alpha, L):
        """Perceptron

        Args:
            df (NdArray): Normalized not tidy DataSet [(x1,...,xn),(y1,...,yn)].
            numero_entradas (int): Numero de entradas del modelo.
            numero_salidas (int): Numero de salidas del modelo.
            por_test(float): Porcentaje de datos de prueba
            alpha (int): Escalar Alpha.
            L (int): Numero de neuronas ocultas.
        """
        N, M = numero_entradas, numero_salidas

        # df slicing df[inicio_fila:fin_fila, inicio_columna:fin_columna]
        n_entrenamiento = int(len(df)*por_test)
        datos_entrenamiento = df[:n_entrenamiento]
        datos_prueba = df[n_entrenamiento:]

        w_h, w_o, E, epocas = self.train_data(N, M, L, datos_entrenamiento, alpha)

        y_pred = self.test_data(datos_prueba, N, w_h, w_o)

        self.print_results(E, N,epocas, y_pred, datos_prueba, "Probando con Datos de prueba",0)

        y_pred = self.test_data(datos_entrenamiento, N, w_h, w_o)

        self.print_results(E,N,epocas, y_pred, datos_entrenamiento, "Probando con Datos de entrenamiento",(n_entrenamiento-len(df)))

    def sigmoid(self, x, a = 1):
        return 1/(1+np.e**(-a*x))

    def forward(self, x, w_h, w_o):
        net_h = w_h@x.T
        y_h = self.sigmoid(net_h)
        net_o = w_o@y_h
        y = self.sigmoid(net_o)
        return y_h, y

    def backward(self, x, w_h, w_o, d, alpha):
        y_h, y = self.forward(x, w_h, w_o)
        delta_o = (d.T-y)*y*(1-y)
        delta_h = y_h*(1-y_h)*(w_o.T@delta_o)
        w_o_new = alpha*delta_o@y_h.T
        w_h_new = alpha*delta_h@x
        E = np.linalg.norm(delta_o)
        return w_o_new, w_h_new, E

    @print_duration
    def train_data(self, N, M, L, datos_entrenamiento, alpha):
        x = datos_entrenamiento[:,:N]
        d = datos_entrenamiento[:,N:]
        w_h = np.random.uniform(-1, 1, (L,N))
        w_o = np.random.uniform(-1, 1, (M,L))
        E = inf
        epocas = 0
        while abs(E) >= MIN_ERROR and epocas < MAX_EPOCAS:
            for j in range(len(x)):
                new_w_o, new_w_h, E = self.backward(x[j].reshape(1,N), w_h, w_o, d[j].reshape(1,M), alpha)
                w_o = w_o + new_w_o
                w_h = w_h + new_w_h
            epocas += 1
        return w_h,w_o,E,epocas

    @print_duration
    def test_data(self, df, N, w_h, w_o):
        x2 = df[:,:N]
        d2 = df[:,N:]
        y_res = np.empty(d2.shape)
        for j in range(len(x2)):
            _, y = self.forward(x2[j].reshape(1,N), w_h, w_o)
            y_res[j] = y.reshape(len(y),)
        return y_res

    def print_results(self, error, N, epocas, y_pred, data_real, nombre, offset):
            y_real = data_real[:,N:]
            y_pred_round = np.round(y_pred.astype(float))
            y_real = y_real.astype(float)
            matriz_confusion = confusion_matrix(y_real, y_pred_round)
            precision = precision_score(y_real, y_pred_round)
            recall = recall_score(y_real, y_pred_round)
            f1 = f1_score(y_real, y_pred_round)
            accuracy = accuracy_score(y_real, y_pred_round)
            print(f'================{nombre}================')
            print("[y_pred]|[y_real]. ([y_pred_original])")
            n_datos = len(y_pred_round)
            for i in range(n_datos):
                print(f"{i+1+offset:0>4}: {y_pred_round[i]}    {y_real[i]}. ({y_pred[i]})")

            print(f'Error: {error}, Epocas:{epocas}.')
            print(f'Accuracy: {round(accuracy,4)}. Precision: {round(precision,4)}. Recall: {round(recall,4)}. F1: {round(f1,4)} ')
            print(f'Matriz Confusión:\n{matriz_confusion}')

df = np.array(read_excel('data/PercMultAplicado.xlsx'))
np.random.shuffle(df)
# En este caso, los datos normalizados comienzan en la posición 8
df = df[:,8:]

Perceptron(
    df=df,
    numero_entradas=3,
    numero_salidas=1,
    por_test=0.7,
    alpha=1,
    L=3*2)