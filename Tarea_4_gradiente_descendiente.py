from sympy.abc import x, y, z
from sympy import sin, Matrix, Symbol, pprint

class Ejercicio:
    def __init__(self, nombre, funcion, v_i_dic, alpha, desc):
        self.nombre = nombre
        self.cifras_sig = 4
        self.E  = 10**-3 # Error
        self.funcion = Matrix(funcion)
        self.v_i_dic = v_i_dic
        self.v_i = Matrix(list(v_i_dic.values())).evalf(self.cifras_sig)
        self.variables =  list(v_i_dic.keys())
        self.alpha = alpha
        self.desc = desc

    def gradiente(self):

        pass

    def print_results(self):
        print(f"====================={self.nombre}=====================")
        print(f"Valores iniciales: {self.x_i_dic}\nEcuaciones:{self.funciones.flat()}")

f1 = x**4 - 3*x**3 + 2
f2 = 5*x**6 + 21*x**5 - 180*x**4 + 115*x**3 + 750*x**2 - 1260*x + 10
f3 = x**2 - 24*x + y**2 - 10*y
f4 = x*y + 1/x +1/y
f5 = sin(x) + sin(y) + sin(x+y) # 0 <= π <= 2 π, 0 <= y <= 2 π
f6 = x**2 + y**2 + z**2 + 1
f7 = 3*x**2 + 4*y**2 + z**2 + 9*x*y*z
f8 = x**4 + y**4 + z**4 + x*y*z

ej1_min1 = Ejercicio("Ejercicio 1 ", f1, {x:1})


for ej in [ej1_min1]:
    ej.gradiente()
