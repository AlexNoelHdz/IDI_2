from sympy import  Matrix, diff, sin
from sympy.abc import x, y, z
cifras_significativas = 4
max_iteraciones = 1000
E = 10**-3

def gradiente(funcion, v_i,alpha, variables, desc):
    """Gradiente Descendente (Minimos) y Ascendente (Maximos)

    Args:
        funcion: Funcion a aplicar el metodo.
        v_i: Vector valores iniciales de las variables.
        alpha: Escalar para ajuste euristico
        variables: Lista de variables de la función
        desc: True: Gradiente Descendente. False: Gradiente Ascendente.
    """
    iteraciones = 0
    gradiantes = []
    #Derivada de funcion con respecto a cada variable
    for variable in variables:
        gradiantes.append(diff(funcion, variable))
    gradiantes = Matrix(gradiantes)

    while True:
        iteraciones += 1
        variables_dic = dict(zip(variables, v_i))
        grad_eval = gradiantes.evalf(cifras_significativas, subs = variables_dic)
        if(desc):
            v_i = (v_i-alpha*grad_eval).evalf(cifras_significativas)
        else:
            v_i = (v_i+alpha*grad_eval).evalf(cifras_significativas)

        # La condición de optimalidad es que el gradiente sea 0 en todas las parciales.
        error_real = grad_eval.norm(1)
        if(E > error_real or iteraciones == max_iteraciones):
            break

    return dict(zip(variables, v_i)), iteraciones, error_real

class Ejercicio:
    def __init__(self,n_ejercicio, v_i_dic, alpha, funcion, desc):
        self.nombre = f"Ejercicio {n_ejercicio}"
        self.variables =  list(v_i_dic.keys())
        self.v_i_dic = v_i_dic
        self.v_i = Matrix(list(v_i_dic.values())).evalf(cifras_significativas)
        self.funcion = funcion
        self.alpha = alpha
        self.desc = desc
        self.grad_tipo = "Descendente" if desc else "Ascendente"
        self.resultado_tipo = "Minimo" if desc else "Maximo"
        self.resultados, self.iteraciones, self.error_acumulado = gradiente(self.funcion,self.v_i, self.alpha, self.variables,self.desc)

    def imprimir_resultados(self):
        print(f'\n#==={self.nombre}: Gradiente {self.grad_tipo}===#')
        print(f'{self.funcion}')
        print(f'{self.resultado_tipo}: {self.resultados}')
        print(f'Vector inicial:{self.v_i_dic}')
        print(f"Iteraciones: {self.iteraciones}. Alpha: {self.alpha}. Error: {self.error_acumulado}")

# Funciones
f1 = x**4 - 3*x**3 + 2
f2 = 5*x**6 + 21*x**5 - 180*x**4 + 115*x**3 + 750*x**2 - 1260*x + 10
f3 = x**2 - 24*x + y**2 - 10*y
f4 = x*y + 1/x + 1/y
f5 = sin(x) + sin(y) + sin(x+y) # 0 <= π <= 2 π, 0 <= y <= 2 π
f6 = x**2 + y**2 + z**2 + 1
f7 = 3*x**2 + 4*y**2 + z**2 - 9*x*y*z
f8 = x**4 + y**4 + z**4 + x*y*z

# Ejercicio(Numero de ejercicio, Vector inicial, Alpha, Funcion, Descendente)
Ejercicio(1, {x:2}, .025 , f1, True).imprimir_resultados()
Ejercicio(2, {x:-8}, 0.00001, f2, True).imprimir_resultados()
Ejercicio(2, {x:-1}, 10**-4, f2, False).imprimir_resultados()
Ejercicio(2, {x:.9}, 10**-3, f2, True).imprimir_resultados()
Ejercicio(3, {x:13,y:6}, .5, f3, True).imprimir_resultados()
Ejercicio(4, {x:.5, y:.5}, 0.2, f4, True).imprimir_resultados()
Ejercicio(5, {x:1,y:1}, 0.2, f5, False).imprimir_resultados()
Ejercicio(6, {x:.5,y:.5,z:.5}, 6**-1, f6, True).imprimir_resultados()
Ejercicio(7, {x:.1,y:.1,z:.1}, 0.0059, f7, True).imprimir_resultados()
Ejercicio(8, {x:-1,y:-1,z:-1}, 0.25, f8, True).imprimir_resultados()
Ejercicio(8, {x:-1,y:1,z:1}, 0.25, f8, True).imprimir_resultados()
Ejercicio(8, {x:1,y:-1,z:1}, 0.25, f8, True).imprimir_resultados()
Ejercicio(8, {x:1,y:1,z:-1}, 0.25, f8, True).imprimir_resultados()
