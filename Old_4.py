from sympy import  Matrix, diff, sin
from sympy.abc import x, y, z
cifras_significativas = 4
max_iteraciones = 200
E = 10**-3

def gradiente(funcion, v_i,alpha, variables, desc):
    """Gradiente Descendiente (Míinimos) y Ascendiente (Maximos)

    Args:
        funcion: Función para aplicar el método.
        v_i: Vector valores iniciales de las variables.
        alpha: Escalar para ajuste euristico
        variables: Lista de variables de la función
        desc: True: Gradiente Descendiente. False: Gradiente Ascendiente.
    """
    iteraciones = 0
    gradiantes = []
    for variable in variables:
        #Derivada de funcion con respecto a cada variable
        gradiantes.append(diff(funcion, variable))
    gradiantes = Matrix(gradiantes)

    while True:
        iteraciones += 1
        variables_dic = dict(zip(variables, v_i))
        #Para cada rango de coordenadas, se evaluan todas las variables
        grad_eval = gradiantes.evalf(cifras_significativas, subs = variables_dic)
        if(desc):
            v_i = (v_i-alpha*grad_eval).evalf(cifras_significativas)
        else:
            v_i = (v_i+alpha*grad_eval).evalf(cifras_significativas)

        # Valor absoluto del vector gradiente indica el error
        error_real = grad_eval.norm(1)
        print(f'Gradiente: {grad_eval}, Iteracion: {iteraciones}')
        if(E > error_real or iteraciones == max_iteraciones):
            break

    return v_i, iteraciones, error_real

def imprimir_resultados(v_i, iteraciones, alpha, resultados, variables, error_acumulado, desc, ecuacion):
    print(f'#===Min {ecuacion}:===#') if desc else print(f'#===Max {ecuacion}:===#')
    print(f'{dict(zip(variables, resultados))}')
    print(f'Valor inicial:{v_i}\nIteraciones:{iteraciones}')
    print(f"Alpha: {alpha}")
    print(f"Error: {error_acumulado}")

def Tarea(v_i_dic, alpha, ecuacion, desc):
    variables =  list(v_i_dic.keys())
    v_i = Matrix(list(v_i_dic.values())).evalf(cifras_significativas)
    resultados, iteraciones, error_acumulado = gradiente(ecuacion,v_i, alpha, variables,desc)
    imprimir_resultados(v_i_dic, iteraciones, alpha, resultados, variables, error_acumulado, desc, ecuacion)

#Ecuaciones
f1 = x**4 - 3*x**3 + 2
f2 = 5*x**6 + 21*x**5 - 180*x**4 + 115*x**3 + 750*x**2 - 1260*x + 10
f3 = x**2 - 24*x + y**2 - 10*y
f4 = x*y + 1/x + 1/y
f5 = sin(x) + sin(y) + sin(x+y) # 0 <= π <= 2 π, 0 <= y <= 2 π
f6 = x**2 + y**2 + z**2 + 1
f7 = 3*x**2 + 4*y**2 + z**2 - 9*x*y*z
f8 = x**4 + y**4 + z**4 + x*y*z

# Tarea({x:1}, 10**-2, f1, True) #2.25

# Tarea({x:-6}, 10**-6, f2, True) #-7
# Tarea({x:-1}, 10**-4, f2, False) #-1.5
# Tarea({x:.9}, 10**-3, f2, True) #1

# Tarea({x:13,y:6},.5, f3, True) # {x: 12.00, y: 5.000}

# Tarea({x:.5, y:.5}, 0.2, f4, True) # {x: 1.000, y: 1.000}

# Tarea({x:1,y:1}, 0.2, f5, False) # {x: 1.047, y: 1.047}

# Tarea({x:.5,y:.5,z:.5}, 6**-1, f6, True) # {x: 0.0001002, y: 0.0001002, z: 0.0001002}

# Tarea({x:.2,y:1,z:.1},0.0059, f7, True) # {x: 0.0007676, y: 0.0002572, z: 0.03263}

# Tarea({x:-1,y:-1,z:-1}, 0.25, f8, True) # {x: -0.2500, y: -0.2500, z: -0.2500}
# Tarea({x:-1,y:1,z:1}, 0.25, f8, True) # {x: -0.2500, y: 0.2500, z: 0.2500}
# Tarea({x:1,y:-1,z:1}, 0.25, f8, True) # {x: 0.2500, y: -0.2500, z: 0.2500}
Tarea({x:1,y:1,z:-1}, 0.25, f8, True) # {x: 0.2500, y: 0.2500, z: -0.2500}
