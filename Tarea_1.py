import sympy as sp
from sympy.abc import x, y, z
from sympy import Float, cos,sin, ln, exp, Matrix, diff

class Ejercicio:
    def __init__(self, fn, x_n, cifras_sig, E ):
        self.fn = fn
        self.x_n = x_n
        self.cifras_sig = cifras_sig
        self.E = E
        self.variables = list(fn.atoms(sp.Symbol))

    def newton_raphson(self):
        fn, x_n, cifras_sig, E  = self.fn, self.x_n, self.cifras_sig, self.E
        # Derivada de la ec
        ec_der = diff(fn)
        iterations = 1

        print("================================================")
        while True:
            # Evaluar ambas expresiones con el nuevo valor de x_n
            subs_dic = Ejercicio.get_subs_dic(self.variables, [x_n])
            fn_ev, fn_der_ev = fn.evalf(subs=subs_dic) , ec_der.evalf(subs=subs_dic)

            if (fn_der_ev == 0):
                print("La derivada es 0, se indetermina la division")
                break
            x_n_new = x_n - (fn_ev/fn_der_ev)
            # print(f"x_n: {x_n} x_n_new: {x_n_new}")
            if (x_n_new == x_n) or (iterations > 100):
                x_n_new = Float(x_n_new,cifras_sig)
                fn_ev = fn.evalf(subs=subs_dic)
                exactitud = abs(0-fn_ev)
                if(exactitud<E):
                    print(f"Solucion para {fn}: {x_n_new}")
                    print(f"Iteraciones: {iterations}")
                    print(f"La Exactitud:{exactitud} cumple con el criterio establecido (es menor que {E})")
                    break
                else:
                    print(f"{fn} tiene exactitud: {exactitud}, no cumple con el criterio establecido (menor que {E})")
                    break
            iterations+=1
            x_n = x_n_new

    @staticmethod
    def get_subs_dic(variables, values):
        subs_dic = {}
        for i, variable in enumerate(variables):
            subs_dic[variable] = values[i]
        return subs_dic

E = 10**-4 # Error
# Definicion de las funciones
f1 = x**3 - 2*x**2 - 5
f2 = x - cos(x)
f3 = x - 0.8 - 0.2*sin(x)
f4 = ln(x - 1) + cos(x - 1)
f5 = exp(x) - 3*x**2
# Encuentre una aproximacion de raiz de 5 correcta con exactitud 10-4.
f6 = x**2 - 5
# Encuentre el unico cero negativo de f(x) = ln(x^2+1)-e^(0.4x)*cos(pi*x)
# con exactitud 10-6.
f7 = ln(x**2+1)-exp(0.4*x)*cos(sp.pi*x)

ej1 = Ejercicio(f1, 3, 10, E)
ej2 = Ejercicio(f2, 1, 10, E)
ej3 = Ejercicio(f3, 1, 10, E)
ej4 = Ejercicio(f4, 1.4, 10, E)
ej5 = Ejercicio(f5, 1, 10, E)
ej6 = Ejercicio(f6, 2.3, 10, E)
ej7 = Ejercicio(f7, -0.27, 10, 10**-6)

ejercicios = [ej1,ej2,ej3,ej4,ej5,ej6,ej7]
# for (funcion, x_0, cifras_sig, Error) in ejercicios
for ej in ejercicios:
    ej.newton_raphson()
