import sympy as sp
from sympy import *

def newton_raphson(ejercicio):
    ec, x_n, cifras_sig, E = ejercicio
    # Derivada de la ec
    ec_der = diff(ec)
    iterations = 1

    print("================================================")
    while True:
        # Evaluar ambas expresiones con el nuevo valor de x_n
        ec_ev, ec_der_ev = ec.evalf(subs={x:x_n}) , ec_der.evalf(subs={x:x_n})

        if (ec_der_ev == 0):
            print("Si la derivada es 0, se indetermina la división")
            break

        x_n_new = x_n - (ec_ev/ec_der_ev)
        x_n_new = Float(x_n_new,cifras_sig)
        # print(f"x_n: {x_n} x_n_new: {x_n_new}")
        if (x_n_new == x_n) or (iterations > 100):
            exactitud = abs(0-ec_ev)
            if(exactitud<E):
                print(f"Solución para {ec}: {x_n_new}")
                print(f"Iteraciones: {iterations}")
                print(f"La Exactitud:{exactitud} cumple con el criterio establecido (es menor que {E})")
                break
            else:
                print(f"Exactitud:{exactitud} no cumple con el criterio establecido (menor que {E})")
                break
        else:
            iterations+=1
            x_n = x_n_new




x = sp.Symbol("x")
E = 10**-4 # Error
# Definición de las funciones
f1 = x**3 - 2*x**2 - 5
f2 = x - cos(x)
f3 = x - 0.8 - 0.2*sin(x)
f4 = ln(x - 1) + cos(x - 1)
f5 = exp(x) - 3*x**2
# Encuentre una aproximación de raíz de 5 correcta con exactitud 10-4.
f6 = x**2 - 5
# Encuentre el único cero negativo de f(x) = ln(x^2+1)-e^(0.4x)*cos(pi*x)
# con exactitud 10-6.
f7 = ln(x**2+1)-exp(0.4*x)*cos(sp.pi*x)

# for (función, x_0, cifras_sig, Error) in ejercicios
ejercicios = [(f1, 3, 10, E), (f2, 1, 10, E), (f3, 1, 10, E), (f4, 1.4, 10, E), (f5, 1, 10, E)]
ejercicios.extend([(f6, 2.3, 10, E), (f7, .5, 10, 10**-6)])

for ejercicio in ejercicios:
    newton_raphson(ejercicio)