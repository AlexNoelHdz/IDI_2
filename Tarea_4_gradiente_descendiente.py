from sympy import  Matrix, diff, sin
from sympy.abc import x, y, z
cifras_significativas = 4
max_iteraciones = 1000
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

    while True:
        variables_dic = dict(zip(variables, v_i))
        grad_eval = gradientes.evalf(cifras_significativas, subs = variables_dic)
        # La condicion de optimalidad es que el gradiente sea 0 en todas las parciales.
        error_real = grad_eval.norm(1)
        if(E > error_real or iteraciones == max_iteraciones):
            return variables_dic, iteraciones, error_real
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
        print(f'{self.funcion}')
        print(f'{resultado_tipo}: {self.resultados}')
        print(f'Vector inicial:{self.v_i_dic}')
        print(f"Iteraciones: {self.iteraciones}. Alpha: {self.alpha}. Error: {self.error_acumulado}")

# Funciones
f1 = x**4 - 3*x**3 + 2
f2 = 5*x**6 + 21*x**5 - 180*x**4 + 115*x**3 + 750*x**2 - 1260*x + 10
f3 = x**2 - 24*x + y**2 - 10*y
f4 = x*y + 1/x + 1/y
f5 = sin(x) + sin(y) + sin(x+y) # 0 <= pi <= 2 pi, 0 <= y <= 2 pi
f6 = x**2 + y**2 + z**2 + 1
f7 = 3*x**2 + 4*y**2 + z**2 - 9*x*y*z
f8 = x**4 + y**4 + z**4 + x*y*z

# Ejercicio(Numero de ejercicio, Vector inicial, Alpha, Funcion, Descendente)
Ejercicio({x:2},                .025 ,      f1, True).imprimir_resultados(1)
Ejercicio({x:-8},               0.00001,    f2, True).imprimir_resultados(2)
Ejercicio({x:-1},               10**-4,     f2, False).imprimir_resultados(2)
Ejercicio({x:.9},               10**-3,     f2, True).imprimir_resultados(2)
Ejercicio({x:13,y:6},           .5,         f3, True).imprimir_resultados(3)
Ejercicio({x:.5, y:.5},         0.2,        f4, True).imprimir_resultados(4)
Ejercicio({x:1,y:1},            0.2,        f5, False).imprimir_resultados(5)
Ejercicio({x:.5,y:.5,z:.5},     6**-1,      f6, True).imprimir_resultados(6)
Ejercicio({x:.1,y:.1,z:.1},     0.0059,     f7, True).imprimir_resultados(7)
Ejercicio({x:-1,y:-1,z:-1},     0.25,       f8, True).imprimir_resultados(8)
Ejercicio({x:-1,y:1,z:1},       0.25,       f8, True).imprimir_resultados(8)
Ejercicio({x:1,y:-1,z:1},       0.25,       f8, True).imprimir_resultados(8)
Ejercicio({x:1,y:1,z:-1},       0.25,       f8, True).imprimir_resultados(8)
