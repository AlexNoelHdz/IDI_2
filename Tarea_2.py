import sympy as sp
from sympy.abc import x, y, z
from sympy import Float, sin, ln, Matrix, Symbol
import string

class Ejercicio:
    def __init__(self, funciones, x_i_dic):
        self.funciones = Matrix(funciones)
        self.x_i = Matrix(list(x_i_dic.values()))
        self.cifras_sig = 5
        self.E  = 10**-4 # Error
        self.variables = list(self.funciones.atoms(Symbol))

    def newton_raphson(self):
        iterations = 1
        x_i = self.x_i
        J_inv = self.funciones.jacobian(self.variables).inv()
        J_det = self.funciones.jacobian(self.variables).det()
        print("================================================")
        while True:
            subs_dic = dict(zip(self.variables, x_i))
            # subs_dic = {key:Float(value, self.cifras_sig) for (key,value) in subs_dic.items()}
            J_det_ev = J_det.subs(subs_dic)
            if (J_det_ev == 0):
                print("El determinante del Jacobiano es 0, no s posible realizar operaciones")
                break

            J_inv_eval = J_inv.subs(subs_dic)
            functions_ev = self.funciones.subs(subs_dic)

            x_i_new = x_i - (J_inv_eval * functions_ev)

            print(f"x_n: {x_i} x_n_new: {x_i_new}")

            norm_2 = sum(abs(functions_ev))
            cumple_exactitud = norm_2 < self.E
            if(cumple_exactitud):
                    print(f"Solucion para {self.funciones}: {subs_dic}")
                    print(f"Iteraciones: {iterations}")
                    print(f"La Norma 2:{norm_2} cumple con el criterio establecido (es menor que {self.E})")
                    break
            else:
                x_i = x_i_new.evalf(self.cifras_sig)
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
ejercicios = [ej1] #,ej2,ej3,ej4]
# for (funcion, x_0, cifras_sig, Error) in ejercicios
for ej in ejercicios:
    ej.newton_raphson()
