from pandas import read_excel
import numpy as np
from math import inf

from sympy import false
np.random.seed(666)


class Perceptron:
    def __init__(self, data_location, numero_entradas, numero_salidas, indicador_desconocido, alpha):
        """Perceptrón Multicapa

        Args:
            data_location (string):         Path del archivo de excel con los datos.
            numero_entradas (integer):      Número de entradas del modelo.
            numero_salidas (integer):       Número de salidas del modelo.
            indicador_desconocido (string): Caracter o cadena que indica que el dato es desconocido.
        """
        df = np.array(read_excel(data_location))
        N = numero_entradas
        M = numero_salidas
        # Numero de neuronas ocultas
        L = N + M

        # df slicing df[inicio_fila:fin_fila, indice_columna]
        # N (numero_entradas) resulta ser el indice de la columna con datos desconocidos
        columna_desc = df[:,N]
        datos_conocidos = df[columna_desc != indicador_desconocido] # Se entrenará con todos los datos conocidos

        # df slicing df[inicio_fila:fin_fila, inicio_columna:fin_columna]
        x = datos_conocidos[:,:N]
        d = datos_conocidos[:,N:]
        w_h = np.random.uniform(-1, 1, (L,N))
        w_o = np.random.uniform(-1, 1, (M,L))

        w_h, w_o, E, epocas = self.train_data(N, M, x, d, w_h, w_o, alpha)

        y_res = self.test_data(df, N, w_h, w_o)

        self.print_results(E,epocas, y_res, df[:,N:], false)

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

    def train_data(self, N, M, x, d, w_h, w_o, alpha):
        E = inf
        epocas = 0
        while abs(E) >= 10**-6 and epocas < 100000:
            for j in range(len(x)):
                new_w_o, new_w_h, E = self.backward(x[j].reshape(1,N), w_h, w_o, d[j].reshape(1,M), alpha)
                w_o = w_o + new_w_o
                w_h = w_h + new_w_h
            epocas += 1
        return w_h,w_o,E,epocas

    def test_data(self, df, N, w_h, w_o):
        x2 = df[:,:N]
        d2 = df[:,N:]
        y_res = np.empty(d2.shape)
        for j in range(len(x2)):
            _, y = self.forward(x2[j].reshape(1,N), w_h, w_o)
            y_res[j] = y.reshape(len(y),)
        return y_res

    def print_results(self, error, epocas, y_res, salidas_originales, redondear):
            print(f'Error: {error}, Epocas:{epocas}')
            print("[y1 y2] | [d1 d2]")
            for j in range(len(y_res)):
                print(f"{np.round(y_res[j]) if redondear else y_res[j]} | {salidas_originales[j]}")

Perceptron('data/tabla_para_probar.xlsx', 4, 2, "?", 1)