#Integracion por simpson 1/3
import numpy as np
def simpson1():
    n=int(input('Ingrese el número de particiones '))
    if n%2==0:
        a=int(input('Ingrese el extremo inferior '))
        b=int(input('Ingrese el extremo superior '))
        x=np.zeros(n+1)
        y=np.zeros(n+1)
        h=(b-a)/n
        suma1=0

        def f(x):
            return ((x-4)**2+2) #Aquí se modifica la función

        for i in range(0,n+1):
            x[i]=a+i*h

        suma1= abs(f(x[0]))+abs(f(x[n]))

        for i in range(1,n,2):
            suma1=suma1+4*abs(f(x[i]))

        for i in range (2,n-1,2):
            suma1=suma1+2*abs(f(x[i]))
        suma1=(h/3)*suma1
        print('El área aproximada por Simpson 1/3 es', np.round(suma1,2))
    else:
        print('El número de particiones debe ser par. Inténtelo de nuevo.')
