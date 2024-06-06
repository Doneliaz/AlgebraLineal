#Integración por rectángulos
import numpy as np
def RecVol():
    n=int(input('Ingrese el número de particiones de x '))
    m=int(input('Ingrese el número de particiones de y '))
    a=int(input('Ingrese el extremo inferior '))
    b=int(input('Ingrese el extremo superior '))
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    w=np.zeros(n+1)
    h1=(b-a)/n
    h2=(b-a)/m
    suma1=0
    suma2=0

    def f(x,y):
        return(2*x**2+3*y**2-x**3*y**3) #Aquí se modifica la función

    for j in range(0,m+1):
        y[j]=a+j*h2
        
    for i in range(0,n+1): 
        x[i]=a+i*h1

    for i in range(0,n):
        for j in range(0,m):
            suma1=suma1+abs(f(x[i],y[j]))*h1*h2
            suma2=suma2+abs(f(x[i+1],y[j+1]))*h1*h2

    if suma1>suma2:
        print('Los límites inferior y superior del volumen son:', round(suma2,2), 'y',  round(suma1,2))
    else:
        print('Los límites inferior y superior del volumen son:', round(suma1,2), 'y',  round(suma2,2))
                    


    
             
