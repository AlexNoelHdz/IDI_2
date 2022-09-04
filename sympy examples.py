from unittest import result
import sympy as sp
from sympy import Matrix, lambdify
from sympy.abc import x,y
from numpy import linalg as LA

x0 = 5.0
y0 = 1.0

x_i = Matrix([x0,y0])

functions = Matrix([x**2+y-1, x-2*y**2])
variables =  list(functions.atoms(sp.Symbol))
J_det = functions.jacobian(variables).det()
# Dentro del while
subs_dic = dict(zip(variables, x_i))
J_det_ev = J_det.subs(subs_dic)
if (J_det_ev == 0):
    print("El determinante del Jacobiano es 0, no s posible realizar operaciones")
else:
    J_inv = functions.jacobian(variables).inv()


    J_inv_eval = J_inv.subs(subs_dic)
    functions_ev = functions.subs(subs_dic)

    norm_2 = sum(abs(functions_ev))

    x_i_new = x_i - (J_inv_eval * functions_ev)


    print(x_i_new)
    print(J_det_ev)