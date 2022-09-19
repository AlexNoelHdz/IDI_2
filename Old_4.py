import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy import sin, ln, Matrix, Symbol, pprint
cifras_significativas = 4
#Tope de iteraciones
max_iteraciones = 1000

def gradiente(funcion, v_i_dic,alpha, variables, desc):
    error = 10**-3
    v_i = Matrix(list(v_i_dic.values())).evalf(cifras_significativas)
    iteraciones = 0
    #Lista de derivadas
    gradiantes = []
    for variable in variables:
        #Derivada de funcion con respecto a cada variable
        gradiantes.append(sp.diff(funcion, variable))
        #do while
    while True:
        iteraciones += 1
        #Auxiliar para comparar el error.
        acum_gradiantes = 0
        for i in range(len(gradiantes)):
            variables_dic = dict(zip(variables, v_i))
            #Para cada rango de coordenadas, se evaluan todas las variables
            grad_eval = gradiantes[i].evalf(cifras_significativas, subs = variables_dic)
            acum_gradiantes += abs(grad_eval)
            if(desc):
                v_i[i] = (v_i[i]-alpha*grad_eval).evalf(cifras_significativas)
            else:
                v_i[i] = (v_i[i]+alpha*grad_eval).evalf(cifras_significativas)
        # print(f'Suma: {acum_gradiantes}, Iteraciones: {iteraciones}')
        if(error > acum_gradiantes or iteraciones == max_iteraciones):
            break

    return v_i, iteraciones, acum_gradiantes

def imprimir_resultados(v_i, iteraciones, alpha, vectores, variables, error_acumulado, desc, ecuacion):
    print(f'#===Minimas {ecuacion}:===#') if desc else print(f'#===Máximas {ecuacion}:===#')
    for i, v in enumerate(vectores):
        print(f'{variables[i]}: {v}')
        print(f'Valor inicial = {v_i}\nIteraciones = {iteraciones}')
        print(f'Alpha: {alpha}\nError = {error_acumulado}')

def Tarea(v_i_dic, alpha, ecuacion, desc):
    variables =  list(v_i_dic.keys())
    raices, iteraciones, error_acumulado = gradiente(ecuacion, v_i_dic.copy(), alpha, variables,desc)
    imprimir_resultados(v_i_dic, iteraciones, alpha, raices, variables, error_acumulado,desc, ecuacion)

#Ecuaciones
x,y,z = sp.symbols('x,y,z')
e1 = x**4 - 3*x**3 + 2
e2 = 5*x**6 + 21*x**5 - 180*x**4 + 115*x**3 + 750*x**2 - 1260*x + 10
e3 = x**2 - 24*x + y**2 - 10*y
e4 = x*y + 1/x +1/y
e5 = sp.sin(x) + sp.sin(y) + sp.sin(x+y) # 0 <= π <= 2 π, 0 <= y <= 2 π
e6 = x**2 + y**2 + z**2 + 1
e7 = 3*x**2 + 4*y**2 + z**2 + 9*x*y*z
e8 = x**4 + y**4 + z**4 + x*y*z
Tarea({x:2.5}, 10**-2, e1, True)

# Tarea({x:1}, 10**-2, e2, True)
# Tarea({x:1}, 10**-2, e2, False)

# Tarea({x:13,y:6}, 10**-4, e3, True)
# Tarea({x:11,z:4}, 10**-6, e3, False)

# Tarea({x:1, y:1}, 10**-2, e4, True)
# Tarea({x:1, z:1}, 10**-2, e4, False)

# Tarea({x:1,y:1}, 10**-2, e5, True)
# Tarea({x:1,y:1}, 10**-2, e5, False)

# Tarea({x:1,y:1,y:1}, 10**-2, e6, True)
# Tarea({x:1,y:1,y:1}, 10**-2, e6, False)

# Tarea({x:1,y:1,y:1}, 10**-2, e7, True)
# Tarea({x:1,y:1,y:1}, 10**-2, e7, False)

# Tarea({x:1,y:1,y:1}, 10**-2, e8, True)
# Tarea({x:1,y:1,y:1}, 10**-2, e8, False)