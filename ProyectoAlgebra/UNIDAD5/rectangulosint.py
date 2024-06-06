#Integracion por rectángulos
import numpy as np
def IntegracionRect():
    n=int(input('Ingrese el número de particiones '))
    a=int(input('Ingrese el extremo inferior '))
    b=int(input('Ingrese el extremo superior '))
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h=(b-a)/n
    suma1=0
    suma2=0

    def f(x):
        return((x-4)**2+2) #Aquí se modifica la función

    for i in range(0,n+1):
        x[i]=a+i*h
        y[i]=f(x[i])

    for i in range(0,n):
        suma1=suma1+abs(y[i])*h
    for i in range(1,n+1):
        suma2=suma2+abs(y[i])*h

    if suma1>suma2:
        print('Los límites inferior y superior del área son:', suma2, 'y',  suma1)
    else:
        print('Los límites inferior y superior del área son:', suma1, 'y',  suma2)
                        


    
             
