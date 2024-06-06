#Integracion por trapecio volumen
import numpy as np
def IntTrapVol():

    n=int(input('Ingrese el número de particiones de x '))
    m=int(input('Ingrese el número de particiones de y '))
    a=int(input('Ingrese el extremo inferior 1 '))
    b=int(input('Ingrese el extremo superior 1 '))
    c=int(input('Ingrese el extremo inferior 2 '))
    d=int(input('Ingrese el extremo superior 2 '))
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h1=(b-a)/n #Incremento en x
    h2=(d-c)/m #Incremento en y
    suma=0
    x=np.zeros(n+1)
    y=np.zeros(m+1)

    def f(x,y):
        return((-4*y+(3*x**2))/(x**3+y**3)) #Aquí se modifica la función

    for j in range(0,m+1):
        y[j]=c+j*h2

    for i in range(0,n+1): 
        x[i]=a+i*h1

    for j in range (0,m+1):
        suma=suma+abs(f(x[0],y[j]))+abs(f(x[-1],y[j]))

    for j in range(1,m):
        for i in range(1,n):
            suma=suma+2*abs(f(x[i],y[j]))
            

    suma=(h1)*(h2/2)*suma
    print('El volumen aproximado por trapecio es', np.round(suma,4))
        
