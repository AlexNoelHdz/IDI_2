from sympy.abc import x, y, z
from sympy import sin, ln, Matrix, Symbol, pprint

class Ejercicio:
    def __init__(self, nombre, funciones, x_i_dic):
        self.x_i_dic = x_i_dic
        self.nombre = nombre
        self.funciones = Matrix(funciones)
        self.cifras_sig = 5
        self.x_i = Matrix(list(x_i_dic.values())).evalf(self.cifras_sig)
        self.E  = 10**-4 # Error
        self.variables =  list(x_i_dic.keys())

    def newton_raphson(self):
        J_inv = self.funciones.jacobian(self.variables).inv()
        J_det = self.funciones.jacobian(self.variables).det()
        iteraciones = 0
        x_i = self.x_i
        print(f"====================={self.nombre}=====================")
        print(f"Valores iniciales: {self.x_i_dic}\nEcuaciones:{self.funciones.flat()}")
        while True:
            subs_dic = dict(zip(self.variables, x_i))
            J_det_ev = J_det.subs(subs_dic)
            if (J_det_ev == 0):
                print("El determinante del Jacobiano es 0, no es posible realizar operaciones")
                break
            functions_ev = self.funciones.subs(subs_dic)
            norm_2 = sum(abs(functions_ev))
            cumple_exactitud = norm_2 < self.E
            if(cumple_exactitud):
                    print(f"Solucion: {subs_dic}. \nIteraciones: {iteraciones}")
                    print(f"La Norma 2:{norm_2} cumple con el error aceptado (es menor que {self.E})")
                    break

            J_inv_eval = J_inv.subs(subs_dic)
            # ALlgoritmo Newton-Raphson. Limitado a cifras significativas dadas.
            x_i = (x_i - (J_inv_eval * functions_ev)).evalf(self.cifras_sig)
            # print(f"x_i: {x_i}") # En caso de necesitar ver los valores de las iteraciones, descomentar.
            iteraciones+=1

f1 = [x**2+y-1, x-2*y**2]
f2 = [x**2-10*x+y**2+5, x*y**2+x-10*y+8]
f3 = [x*sin(y)-1, x**2+y**2-4]
f4 = [y**2*ln(x)-3, y-x**2]
f5 = [x+y-z+2, x**2+y, z-y**2-1]

ej1_r1 = Ejercicio("Ejercicio 1 raiz 1", f1, {x:0.7,y:0.6})
ej1_r2 = Ejercicio("Ejercicio 1 raiz 2", f1, {x:1.36,y:-0.83})

ej2_r1 = Ejercicio("Ejercicio 2 raiz 1", f2, {x:0.7,y:1.0})
ej2_r2 = Ejercicio("Ejercicio 2 raiz 2", f2, {x:2.1,y:3.4})

ej3_r1 = Ejercicio("Ejercicio 3 raiz 1", f3, {x:1.0,y:2.0})
ej3_r2 = Ejercicio("Ejercicio 3 raiz 2", f3, {x:2.0,y:0.5})
ej3_r3 = Ejercicio("Ejercicio 3 raiz 3", f3, {x:-1.1,y:-1.8})
ej3_r4 = Ejercicio("Ejercicio 3 raiz 4", f3, {x:-2.0,y:-0.6})

ej4_r1 = Ejercicio("Ejercicio 4 raiz 1", f4, {x:1.6,y:2.6})

ej5_r1 = Ejercicio("Ejercicio 5 raiz 1", f5, {x:0.9,y:-0.9,z:1.9})
ej5_r2 = Ejercicio("Ejercicio 5 raiz 2", f5, {x:-0.5,y:-0.3,z:1.1})

# ej1_r1.newton_raphson()
for ej in [ej1_r1, ej1_r2, ej2_r1, ej2_r2, ej3_r1, ej3_r2, ej3_r3, ej3_r4, ej4_r1, ej5_r1, ej5_r2]:
    ej.newton_raphson()

"""
Respuestas:
=====================Ejercicio 1 raiz 1=====================
Valores iniciales: {x: 0.7, y: 0.6}
Ecuaciones:[x**2 + y - 1, x - 2*y**2]
Solucion: {x: 0.65425, y: 0.57195}.
Iteraciones: 2
La Norma 2:9.5367E-7 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 1 raiz 2=====================
Valores iniciales: {x: 1.36, y: -0.83}
Ecuaciones:[x**2 + y - 1, x - 2*y**2]
Solucion: {x: 1.3496, y: -0.82147}.
Iteraciones: 2
La Norma 2:9.5367E-7 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 2 raiz 1=====================
Valores iniciales: {x: 0.7, y: 1.0}
Ecuaciones:[x**2 - 10*x + y**2 + 5, x*y**2 + x - 10*y + 8]
Solucion: {x: 0.62231, y: 0.91424}.
Iteraciones: 2
La Norma 2:0.000036240 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 2 raiz 2=====================
Valores iniciales: {x: 2.1, y: 3.4}
Ecuaciones:[x**2 - 10*x + y**2 + 5, x*y**2 + x - 10*y + 8]
Solucion: {x: 2.0755, y: 3.3834}.
Iteraciones: 2
La Norma 2:0 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 3 raiz 1=====================
Valores iniciales: {x: 1.0, y: 2.0}
Ecuaciones:[x*sin(y) - 1, x**2 + y**2 - 4]
Solucion: {x: 1.0120, y: 1.7251}.
Iteraciones: 3
La Norma 2:0.0000038147 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 3 raiz 2=====================
Valores iniciales: {x: 2.0, y: 0.5}
Ecuaciones:[x*sin(y) - 1, x**2 + y**2 - 4]
Solucion: {x: 1.9239, y: 0.54659}.
Iteraciones: 2
La Norma 2:0.000032902 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 3 raiz 3=====================
Valores iniciales: {x: -1.1, y: -1.8}
Ecuaciones:[x*sin(y) - 1, x**2 + y**2 - 4]
Solucion: {x: -1.0120, y: -1.7251}.
Iteraciones: 2
La Norma 2:0.000055313 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 3 raiz 4=====================
Valores iniciales: {x: -2.0, y: -0.6}
Ecuaciones:[x*sin(y) - 1, x**2 + y**2 - 4]
Solucion: {x: -1.9239, y: -0.54660}.
Iteraciones: 2
La Norma 2:0.0000023842 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 4 raiz 1=====================
Valores iniciales: {x: 1.6, y: 2.6}
Ecuaciones:[y**2*log(x) - 3, -x**2 + y]
Solucion: {x: 1.5931, y: 2.5381}.
Iteraciones: 2
La Norma 2:0.0000038147 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 5 raiz 1=====================
Valores iniciales: {x: 0.9, y: -0.9, z: 1.9}
Ecuaciones:[x + y - z + 2, x**2 + y, -y**2 + z - 1]
Solucion: {x: 1.0000, y: -1.0000, z: 2.0000}.
Iteraciones: 3
La Norma 2:0.0000028610 cumple con el error aceptado (es menor que 0.0001)
=====================Ejercicio 5 raiz 2=====================
Valores iniciales: {x: -0.5, y: -0.3, z: 1.1}
Ecuaciones:[x + y - z + 2, x**2 + y, -y**2 + z - 1]
Solucion: {x: -0.56985, y: -0.32471, z: 1.1054}.
Iteraciones: 2
La Norma 2:0.000012398 cumple con el error aceptado (es menor que 0.0001)
"""
