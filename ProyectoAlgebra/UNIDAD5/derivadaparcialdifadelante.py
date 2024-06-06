import sympy as sy
import numpy as np
def DerivadaParcial():
    #Programar la derivada parcial usando límites
    #Diferencias adelante
    h=float(input('Ingrese el valor de h: '))
    x=sy.symbols('x')
    y=sy.symbols('y')

    def f(x,y):
        return (2*x**2+3*y**2-x**3*y**3)

    def derx(x):
        a=sy.expand(f(x+h,y))
        b=sy.expand(f(x-h,y))
        return (a-b)/(2*h)

    def dery(y):
        a=sy.expand(f(x,y+h))
        b=sy.expand(f(x,y-h))
        return (a-b)/(2*h)
    

    print(derx(x))
    print(dery(y))
    print(dery(derx(x)))
