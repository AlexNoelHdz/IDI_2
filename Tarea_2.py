import sympy as sp
from sympy.abc import x, y, z
from sympy import Float, sin, ln, Matrix, Symbol
import string

class Ejercicio:
    def __init__(self, funciones, x_i_dic):
        self.funciones = Matrix(funciones)
        self.cifras_sig = 5
        self.x_i = Matrix(list(x_i_dic.values())).evalf(self.cifras_sig)
        self.E  = 10**-4 # Error
        self.variables = list(self.funciones.atoms(Symbol))

    def newton_raphson(self):
        iterations = 1
        x_i = self.x_i
        J_inv = self.funciones.jacobian(self.variables).inv()
        J_det = self.funciones.jacobian(self.variables).det()
        print(f"================================================")
        while True:
            print(f"x_i: {x_i}")
            subs_dic = dict(zip(self.variables, x_i))
            J_det_ev = J_det.subs(subs_dic)
            if (J_det_ev == 0):
                print("El determinante del Jacobiano es 0, no es posible realizar operaciones")
                break
            functions_ev = self.funciones.subs(subs_dic)
            norm_2 = sum(abs(functions_ev))
            cumple_exactitud = norm_2 < self.E
            if(cumple_exactitud):
                    print(f"Solucion para {self.funciones}: {subs_dic}. Iteraciones: {iterations}")
                    print(f"La Norma 2: {norm_2} cumple con el criterio establecido (es menor que {self.E})")
                    break

            J_inv_eval = J_inv.subs(subs_dic)
            x_i = (x_i - (J_inv_eval * functions_ev)).evalf(self.cifras_sig)
            iterations+=1

# Definicion de las funciones
f1 = [x**2+y-1, x-2*y**2]
f2 = [x**2-10*x+y**2+5, x*y**2+x-10*y+8]
f3 = [x*sin(y)-1, x**2+y**2-4]
f4 = [y**2*ln(x)-3, y-x**2]
f5 = [x+y-z-2, x**2+y, -y**2+1-1]

ej1 = Ejercicio(f1, {x:0.7,y:0.6})
ej2 = Ejercicio(f2, {x:0.7,y:1.0})
ej3 = Ejercicio(f3, {x:1.0,y:2.0})
ej4 = Ejercicio(f4, {x:1.6,y:2.6})
ej5 = Ejercicio(f5, {x:1.0,y: 1.0, z:1.0})
ejercicios = [ej1,ej2,ej3,ej4,ej5]

for ej in ejercicios:
    ej.newton_raphson()

"""
Respuestas al momento:
================================================
x_i: Matrix([[0.70000], [0.60000]])
x_i: Matrix([[0.65505], [0.57294]])
x_i: Matrix([[0.65425], [0.57195]])
Solucion para Matrix([[x**2 + y - 1], [x - 2*y**2]]): {x: 0.65425, y: 0.57195}. Iteraciones: 3
La Norma 2: 9.5367E-7 cumple con el criterio establecido (es menor que 0.0001)
================================================
x_i: Matrix([[0.70000], [1.0000]])
x_i: Matrix([[0.62015], [0.91166]])
x_i: Matrix([[0.62231], [0.91424]])
Solucion para Matrix([[x**2 - 10*x + y**2 + 5], [x*y**2 + x - 10*y + 8]]): {x: 0.62231, y: 0.91424}. Iteraciones: 3
La Norma 2: 0.000036240 cumple con el criterio establecido (es menor que 0.0001)
================================================
x_i: Matrix([[1.0000], [2.0000]])
x_i: Matrix([[0.98807], [1.7560]])
x_i: Matrix([[1.0118], [1.7256]])
x_i: Matrix([[1.0120], [1.7251]])
Solucion para Matrix([[x*sin(y) - 1], [x**2 + y**2 - 4]]): {x: 1.0120, y: 1.7251}. Iteraciones: 4
La Norma 2: 0.0000038147 cumple con el criterio establecido (es menor que 0.0001)
================================================
x_i: Matrix([[1.6000], [2.6000]])
x_i: Matrix([[1.5934], [2.5389]])
x_i: Matrix([[1.5931], [2.5381]])
Solucion para Matrix([[y**2*log(x) - 3], [-x**2 + y]]): {x: 1.5931, y: 2.5381}. Iteraciones: 3
La Norma 2: 0.0000038147 cumple con el criterio establecido (es menor que 0.0001)
================================================
x_i: Matrix([[1.0000], [1.0000], [1.0000]])
x_i: Matrix([[0.50000], [0.25000], [-1.2500]])
x_i: Matrix([[0.25000], [-0.37500], [-2.1250]])
x_i: Matrix([[0.12500], [-0.020833], [-1.8958]])
x_i: Matrix([[0.062500], [1.4896], [-0.44790]])
x_i: Matrix([[0.031250], [0.73431], [-1.2344]])
x_i: Matrix([[0.015625], [0.35652], [-1.6279]])
x_i: Matrix([[0.0078125], [0.16730], [-1.8249]])
x_i: Matrix([[0.0039063], [0.071977], [-1.9241]])
x_i: Matrix([[0.0019531], [0.022421], [-1.9756]])
x_i: Matrix([[0.00097656], [-0.010568], [-2.0096]])
x_i: Matrix([[0.00048828], [0.017819], [-1.9817]])
x_i: Matrix([[0.00024414], [0.0020587], [-1.9977]])
x_i: Matrix([[0.00012207], [-0.028618], [-2.0285]])
x_i: Matrix([[6.1035e-5], [-0.013243], [-2.0132]])
x_i: Matrix([[3.0518e-5], [-0.0054690], [-2.0054]])
Solucion para Matrix([[x + y - z - 2], [x**2 + y], [-y**2]]): {y: 3.0518e-5, x: -0.0054690, z: -2.0054}. Iteraciones: 16
La Norma 2: 0.000064243 cumple con el criterio establecido (es menor que 0.0001)
"""
