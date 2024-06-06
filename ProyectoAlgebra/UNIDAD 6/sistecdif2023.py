#SISTEMAS DE ECUACIONES DIFERENCIALES
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

h=float(input('Ingrese el tamaño del paso '))
aprox=float(input('Ingrese el valor a aproximar '))
c=float(input('Ingrese el valor de t '))
a=float(input('Ingrese el valor de x '))
b=float(input('Ingrese el valor de y '))
t=[]
x=[]
y=[]
#Estas son de dy 
k1=[]
k2=[]
k3=[]
k4=[]
#Estas son de dx
k11=[]
k21=[]
k31=[]
k41=[]

j=0

x.append(a)
y.append(b)
t.append(c)
print(x,y,c)
def f(t,x,y):
    return(0.50*y-(0.0020*y**2)-(0.001*x*y)) #Aquí se modifica la función de dy
def g(t,x,y):
    return(0.65*x-(0.0032*x**2)-(0.002*x*y)) #Aquí se modifica la función de dx

print('i' 'x   \t   y')
for i in np.arange(c,aprox,h):
    t.append(t[j]+h)
    #Con esto se calcula dy/dt
    k1.append(f(t[j],x[j],y[j]))
    k2.append(f(t[j]+h/2,x[j]+(h/2)*k1[j],y[j]+(h/2)*k1[j]))
    k3.append(f(t[j]+h/2,x[j]+(h/2)*k2[j],y[j]+(h/2)*k2[j]))
    k4.append(f(t[j]+h,x[j]+(h)*k3[j],y[j]+(h)*k3[j]))
    y.append(y[j]+h/6*(k1[j]+2*k2[j]+2*k3[j]+k4[j]))
    #Con esto se calcula dx/dt
    k11.append(g(t[j],x[j],y[j]))
    k21.append(g(t[j]+h/2,x[j]+(h/2)*k11[j],y[j]+(h/2)*k11[j]))
    k31.append(g(t[j]+h/2,x[j]+(h/2)*k21[j],y[j]+(h/2)*k21[j]))
    k41.append(g(t[j]+h,x[j]+(h)*k31[j],y[j]+(h)*k31[j]))
    x.append(x[j]+h/6*(k11[j]+2*k21[j]+2*k31[j]+k41[j]))
    print(j, '\t ', np.around(x[j],4), y[j]) 
    j+=1
    

ax=plt.gca()

plt.plot(t,x)
plt.plot(t,y)
plt.xlabel('tiempo')
plt.ylabel('y(t), x(t)')
plt.show()
