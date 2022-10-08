from matplotlib import pyplot as plt
import pandas as pd
from sympy import  Matrix, diff, sin, symbols
from sympy.abc import m,b
import numpy as np
cifras_significativas = 4
max_iteraciones = 21370
E = 10**-3

def gradiente(funcion, v_i_dic ,alpha, desc):
    """Gradiente Descendente (Minimos) y Ascendente (Maximos)

    Args:
        funcion(sympy function):    Funcion matematica objeto del metodo.
        v_i_dic(dic):               Diccionario con valores iniciales de las variables {Sympy Variable:Valor,...}.
        alpha(float):               Escalar para ajuste euristico.
        desc(Boolean):              True: Gradiente Descendente. False: Gradiente Ascendente.
    """
    variables =  list(v_i_dic.keys())
    v_i = Matrix(list(v_i_dic.values()))
    iteraciones = 0
    #Derivada de funcion con respecto a cada variable (by List comprehension)
    gradientes = Matrix([diff(funcion, variable) for variable in variables])
    e_cache = {}

    while True:
        variables_dic = dict(zip(variables, v_i))
        grad_eval = gradientes.evalf(cifras_significativas, subs = variables_dic)
        # La condicion de optimalidad es que el gradiente sea 0 en todas las parciales.
        error_real = grad_eval.norm(1)
        # if(iteraciones%100==0):
        #     print(f"{iteraciones}:{error_real}")
        if(E > error_real or iteraciones == max_iteraciones):
            min_key = min(e_cache, key=e_cache.get)
            print(f"{min_key}:{e_cache[min_key]}")
            return variables_dic, iteraciones, error_real
        e_cache[iteraciones]=error_real
        iteraciones += 1
        # Algoritmo gradiente Descendiente/Ascendiente
        v_i = (v_i-alpha*grad_eval).evalf(cifras_significativas)

class Ejercicio:
    def __init__(self, v_i_dic, alpha, funcion, desc):
        self.v_i_dic = v_i_dic
        self.funcion = funcion
        self.alpha = alpha
        self.desc = desc
        self.resultados, self.iteraciones, self.error_acumulado = gradiente(self.funcion, self.v_i_dic, self.alpha, self.desc)

    def imprimir_resultados(self, n_ejercicio):
        grad_tipo = "Descendente" if self.desc else "Ascendente"
        resultado_tipo = "Minimo" if self.desc else "Maximo"
        print(f'\n#===Ejercicio {n_ejercicio}: Gradiente {grad_tipo}===#')
        # print(f'{self.funcion}')
        print(f'{resultado_tipo}: {self.resultados}')
        print(f'Vector inicial:{self.v_i_dic}. Error Esperado {E}')
        print(f"Iteraciones: {self.iteraciones}. Alpha: {self.alpha}. Error: {self.error_acumulado}")

# Ejercicio 1
np.random.seed(0)
xi = np.arange(1, 101)
yi = xi + 3*np.random.uniform(0, 1)
alpha1 = 0.000590111
n = len(xi)
fi = xi*m + b
ecm1 = sum((yi-fi)**2)/(2*n)

# Ejercicio(Numero de ejercicio, Vector inicial, Alpha, Funcion, Descendente)
e1 = Ejercicio({m:1, b:3},alpha1,ecm1, True)
e1.imprimir_resultados(1)
plt.plot(xi, yi, 'o')
plt.plot(xi, e1.v_i_dic[m]*xi+e1.v_i_dic[b])

# Ejercicio 2
m1,m2,m3,b = symbols('m1,m2,m3,b')
data = np.array(pd.read_excel('data/tareaRGD.xlsx'))
yi = data[:,3]
x1 =  data[:,0]
x2 =  data[:,1]
x3 =  data[:,2]
ecm2 = sum((yi - x1*m1 - x2*m2 - x3*m3 - b)**2)/(2*len(data[:,1]))
max_iteraciones = 100000
E = 10**-5
miu = 0.0006
# Ejercicio(Numero de ejercicio, Vector inicial, Alpha, Funcion, Descendente)
v_i_dic = {m1:10, m2:.0001, m3:.0001, b:.0003}
e2 = Ejercicio(v_i_dic,miu,ecm2, True)
e2.imprimir_resultados(2)
