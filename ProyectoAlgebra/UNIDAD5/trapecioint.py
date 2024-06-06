#Integracion por trapecio
import numpy as np
def integracionTrap():
    n=int(input('Ingrese el número de particiones '))
    a=int(input('Ingrese el extremo inferior '))
    b=int(input('Ingrese el extremo superior '))
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h=(b-a)/n
    suma1=0

    def f(x):
        return((x-4)**2+2) #Aquí se modifica la función

    for i in range(0,n+1):
        x[i]=a+i*h
        y[i]=f(x[i])

    suma1= abs(f(x[0]))+abs(f(x[n]))

    for i in range(1,n):
        suma1=suma1+2*abs(f(x[i]))
        
    suma1=(h/2)*suma1

    print('El área aproximada por trapecio es', np.round(suma1,4))
        
