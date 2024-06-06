#Integracion por simpson 1/3 (volumen)
import numpy as np
n=int(input('Ingrese el número de particiones de x '))
m=int(input('Ingrese el número de particiones de y '))
if n%2==0 and m%2==0:
    a=int(input('Ingrese el extremo inferior de x '))
    b=int(input('Ingrese el extremo superior de x ')) 
    c=int(input('Ingrese el extremo inferior de y '))
    d=int(input('Ingrese el extremo superior de y '))
    x=np.zeros(n+1)
    y=np.zeros(m+1)
    h1=(b-a)/n
    h2=(d-c)/m
    suma=0

    def f(x,y):
        return (-4*y+(3*x**2))/(x**3+y**3) #Aquí se modifica la función

#ESTO ES EL ENMALLADO
    for j in range(0,m+1):
        y[j]=c+j*h2
    
    for i in range(0,n+1):
        x[i]=a+i*h1
     
#CALCULO 
    suma=suma-abs(f(x[0],y[0]))-abs(f(x[0],y[-1]))-abs(f(x[-1],y[0]))-abs(f(x[-1],y[-1])) #lOS EXTREMOS

    for j in range(0,m+1,2):
        for i in range(1,n+1,2):
            suma=suma+4*abs(f(x[i],y[j]))

    for j in range(1,m+1,2):
        for i in range(0,n+1,2):
            suma=suma+4*abs(f(x[i],y[j]))

    for j in range(0,m+1,2):
        for i in range (0,n+1,2):
            suma=suma+2*abs(f(x[i],y[j]))

    for j in range(1,m+1,2):
        for i in range (1,n+1,2):
            suma=suma+2*abs(f(x[i],y[j]))

    suma=((h1*h2)/3)*suma
    print('El volumen aproximado por Simpson 1/3 es', np.round(suma,2))
else:
    print('El número de particiones debe ser par. Inténtelo de nuevo.')
