# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:22:42 2022

@author: Enrique Rojas
"""
from sympy import symbols, diff
import sympy as sp


x = sp.Symbol("x")
E = 10**-4

def nr_root(function):
    x = symbols("x")
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    x0 = float(input('Enter Guess: '))
    f = function
    x1 = 0
    step = 0
    while x0 != x1:
        x1 = x0
        x0 = x0 - float((f.subs(x,x0))/(diff(f,x).subs(x,x0)))
        if ( diff(f,x).subs(x,x0) == 0):
            print("Se indetermina la division")
            break
        if x0 == x1 or step > 1000:
            exactitud = abs((0-f.subs(x,x0)))
            if exactitud<E:
                print(f"La Exactitud:{exactitud} cumple con el criterio establecido (es menor que {E})")
                break
            else:
                print(f"Exactitud:{exactitud} no cumple con el criterio establecido (menor que {E})")
        print (f"Iteraciones: {step} x= {x0:0.10}")
        step += 1

    return x0



f1 =nr_root( x**3 - 2*x**2 - 5)
f2 = nr_root(x - sp.cos(x))
f3 = nr_root(x - 0.8 - 0.2*sp.sin(x))
f4 = nr_root(sp.ln(x - 1) + sp.cos(x - 1))
f5 = nr_root(sp.exp(x) - 3*x**2)
# Encuentre una aproximacion de raiz de 5 correcta con exactitud 10-4.
f6 = nr_root(x**2 - 5)
# Encuentre el unico cero negativo de f(x) = ln(x^2+1)-e^(0.4x)*cos(pi*x)
# con exactitud 10-6.
f7 = nr_root(sp.ln(x**2+1)-sp.exp(0.4*x)*sp.cos(pi*x))
