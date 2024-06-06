import sympy as sy
from sympy import * # type: ignore

def DerivadaLimite():
    
    #Programar la derivada usando límites
    #Diferencias Centradas
    a=float(input('Ingrese el valor de h: '))

    x=sy.symbols('x')
    y=sy.symbols('y')
    h=sy.symbols('h')
    def f(x,y):
        return (3*sy.exp(-x**3*y**2))

    def der(x,y):
        a=sy.expand(f(x+h,y))
        b=sy.expand(f(x-h,y))
        return (a-b)/(2*h)

    def der2(x,y):
        c=sy.expand(f(x,y+h))
        d=sy.expand(f(x,y-h))
        return (c-d)/(2*h)
    y1=der(x,y)
    y1=y1.subs(h,a)
    y1=simplify(y1)
    print('La parcial con respecto a x es:\n')
    print(y1,' \n')
    y2=der2(x,y)
    y2=y2.subs(h,a)
    y2=simplify(y2)
    print('La parcial con respecto a y es: \n')
    print(y2)

    #num=int(input('¿Qué numero de derivada desea calcular?'))
    #y=f(x)
            
    #for i in range(0,num):
    #        y=der(y)

    #print(f(x))



