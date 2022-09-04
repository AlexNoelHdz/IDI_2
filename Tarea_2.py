from sympy.abc import x, y, z
from sympy import sin, ln, Matrix, Symbol

class Ejercicio:
    def __init__(self, nombre, funciones, x_i_dic):
        self.nombre = nombre
        self.funciones = Matrix(funciones)
        self.cifras_sig = 5
        self.x_i = Matrix(list(x_i_dic.values())).evalf(self.cifras_sig)
        self.E  = 10**-4 # Error
        self.variables = list(self.funciones.atoms(Symbol))

    def newton_raphson(self):
        iteraciones = 1
        x_i = self.x_i
        J_inv = self.funciones.jacobian(self.variables).inv()
        J_det = self.funciones.jacobian(self.variables).det()
        print(f"====================={self.nombre}=====================")
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
                    print(f"Solucion para {self.funciones}:\n{subs_dic}. \nIteraciones: {iteraciones}")
                    print(f"La Norma 2:{norm_2} cumple con el criterio establecido (es menor que {self.E})")
                    break

            J_inv_eval = J_inv.subs(subs_dic)
            # Newton-Raphson. Limitado a cifras significativas dadas.
            x_i = (x_i - (J_inv_eval * functions_ev)).evalf(self.cifras_sig)
            iteraciones+=1
            # Forma alternativa de cortar el ciclo. Se alcanza cuando
            # 1. Bug de Sympy desordena x,y,z... y rompe con los valores iniciales
            # 2. No se ha llegado a la respuesta y x_i esta creciendo y decreciendo. (No llegara)
            if iteraciones > 90:
                break

f1 = [x**2+y-1, x-2*y**2]
f2 = [x**2-10*x+y**2+5, x*y**2+x-10*y+8]
f3 = [x*sin(y)-1, x**2+y**2-4]
f4 = [y**2*ln(x)-3, y-x**2]
f5 = [x+y-z-2, x**2+y, -y**2+1-1]

ej1_r1 = Ejercicio("Ejercicio 1 raiz 1", f1, {x:0.7,y:0.6})
ej1_r2 = Ejercicio("Ejercicio 1 raiz 2", f1, {x:1.36,y:-0.83})

ej2_r1 = Ejercicio("Ejercicio 2 raiz 1", f2, {x:0.7,y:1.0})
ej2_r2 = Ejercicio("Ejercicio 2 raiz 2", f2, {x:2.1,y:3.4})

ej3_r1 = Ejercicio("Ejercicio 3 raiz 1", f3, {x:1.0,y:2.0})
ej3_r2 = Ejercicio("Ejercicio 3 raiz 2", f3, {x:2.0,y:0.5})
ej3_r3 = Ejercicio("Ejercicio 3 raiz 3", f3, {x:-1.1,y:-1.8})
ej3_r4 = Ejercicio("Ejercicio 3 raiz 4", f3, {x:-2.0,y:-0.6})

ej4_r1 = Ejercicio("Ejercicio 4 raiz 1", f4, {x:1.6,y:2.6})

ej5_r1 = Ejercicio("Ejercicio 5 raiz 1", f5, {x:1.0,y: 1.0, z:1.0})

for ej in [ej1_r1, ej1_r2, ej2_r1, ej2_r2, ej3_r1, ej3_r2, ej3_r3, ej3_r4, ej4_r1, ej5_r1]:
    ej.newton_raphson()

"""
Respuestas al momento.:
=====================Ejercicio 1 raiz 1=====================
x_i: Matrix([[0.70000], [0.60000]])
x_i: Matrix([[0.65505], [0.57294]])
x_i: Matrix([[0.65425], [0.57195]])
Solucion para Matrix([[x**2 + y - 1], [x - 2*y**2]]): {x: 0.65425, y: 0.57195}. Iteraciones: 3
La Norma 2: 9.5367E-7 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 1 raiz 2=====================
x_i: Matrix([[1.3600], [-0.83000]])
x_i: Matrix([[1.3497], [-0.82153]])
x_i: Matrix([[1.3496], [-0.82147]])
Solucion para Matrix([[x**2 + y - 1], [x - 2*y**2]]): {x: 1.3496, y: -0.82147}. Iteraciones: 3
La Norma 2: 9.5367E-7 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 2 raiz 1=====================
x_i: Matrix([[0.70000], [1.0000]])
x_i: Matrix([[0.62015], [0.91166]])
x_i: Matrix([[0.62231], [0.91424]])
Solucion para Matrix([[x**2 - 10*x + y**2 + 5], [x*y**2 + x - 10*y + 8]]): {x: 0.62231, y: 0.91424}. Iteraciones: 3
La Norma 2: 0.000036240 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 2 raiz 2=====================
x_i: Matrix([[2.1000], [3.4000]])
x_i: Matrix([[2.0756], [3.3836]])
x_i: Matrix([[2.0755], [3.3834]])
Solucion para Matrix([[x**2 - 10*x + y**2 + 5], [x*y**2 + x - 10*y + 8]]): {x: 2.0755, y: 3.3834}. Iteraciones: 3
La Norma 2: 0 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 3 raiz 1=====================
x_i: Matrix([[1.0000], [2.0000]])
x_i: Matrix([[0.98807], [1.7560]])
x_i: Matrix([[1.0118], [1.7256]])
x_i: Matrix([[1.0120], [1.7251]])
Solucion para Matrix([[x*sin(y) - 1], [x**2 + y**2 - 4]]): {x: 1.0120, y: 1.7251}. Iteraciones: 4
La Norma 2: 0.0000038147 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 3 raiz 2=====================
x_i: Matrix([[2.0000], [0.50000]])
x_i: Matrix([[1.9266], [0.54349]])
x_i: Matrix([[1.9239], [0.54659]])
Solucion para Matrix([[x*sin(y) - 1], [x**2 + y**2 - 4]]): {x: 1.9239, y: 0.54659}. Iteraciones: 3
La Norma 2: 0.000032902 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 3 raiz 3=====================
x_i: Matrix([[-1.1000], [-1.8000]])
x_i: Matrix([[-1.0090], [-1.7306]])
x_i: Matrix([[-1.0120], [-1.7251]])
Solucion para Matrix([[x*sin(y) - 1], [x**2 + y**2 - 4]]): {x: -1.0120, y: -1.7251}. Iteraciones: 3
La Norma 2: 0.000055313 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 3 raiz 4=====================
x_i: Matrix([[-2.0000], [-0.60000]])
x_i: Matrix([[-1.9259], [-0.54703]])
x_i: Matrix([[-1.9239], [-0.54660]])
Solucion para Matrix([[x*sin(y) - 1], [x**2 + y**2 - 4]]): {x: -1.9239, y: -0.54660}. Iteraciones: 3
La Norma 2: 0.0000023842 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 4 raiz 1=====================
x_i: Matrix([[1.6000], [2.6000]])
x_i: Matrix([[1.5934], [2.5389]])
x_i: Matrix([[1.5931], [2.5381]])
Solucion para Matrix([[y**2*log(x) - 3], [-x**2 + y]]): {x: 1.5931, y: 2.5381}. Iteraciones: 3
La Norma 2: 0.0000038147 cumple con el criterio establecido (es menor que 0.0001)
=====================Ejercicio 5 raiz 1=====================
x_i: Matrix([[1.0000], [1.0000], [1.0000]])
x_i: Matrix([[0.25000], [-1.2500], [0.50000]])
x_i: Matrix([[-0.37500], [-2.1250], [0.25000]])
x_i: Matrix([[-0.020833], [-1.8958], [0.12500]])
x_i: Matrix([[1.4896], [-0.44790], [0.062500]])
x_i: Matrix([[0.73431], [-1.2344], [0.031250]])
x_i: Matrix([[0.35652], [-1.6279], [0.015625]])
x_i: Matrix([[0.16730], [-1.8249], [0.0078125]])
x_i: Matrix([[0.071977], [-1.9241], [0.0039063]])
x_i: Matrix([[0.022421], [-1.9756], [0.0019531]])
x_i: Matrix([[-0.010568], [-2.0096], [0.00097656]])
x_i: Matrix([[0.017819], [-1.9817], [0.00048828]])
x_i: Matrix([[0.0020587], [-1.9977], [0.00024414]])
x_i: Matrix([[-0.028618], [-2.0285], [0.00012207]])
x_i: Matrix([[-0.013243], [-2.0132], [6.1035e-5]])
x_i: Matrix([[-0.0054690], [-2.0054], [3.0518e-5]])
Solucion para Matrix([[x + y - z - 2], [x**2 + y], [-y**2]]): {x: -0.0054690, z: -2.0054, y: 3.0518e-5}. Iteraciones: 16
La Norma 2: 0.000064243 cumple con el criterio establecido (es menor que 0.0001)
"""
