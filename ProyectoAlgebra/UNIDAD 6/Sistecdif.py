#RungeKutta
import numpy as np
import matplotlib.pyplot as plt

c=float(input('Ingrese el tiempo inicial t'))
a=float(input('Ingrese el valor inicial de x'))
b=float(input('Ingrese el valor inicial de y'))

x=[]
y=[]
t=[]
k1=[]
k2=[]
k3=[]
k4=[]
k11=[]
k21=[]
k31=[]
k41=[]
j=0

h=float(input('Ingrese el tamaño del paso '))
aprox=float(input('Ingrese el valor a aproximar '))
x.append(a)
y.append(b)
t.append(c)

def f(t,x,y):
    return(0.65*x-(0.0032*x**2)-(0.002*x*y))

def g(t,x,y):
    return(0.5*y-(.002*y**2)-(0.001*x*y))


for i in np.arange(c,aprox,h):
    t.append(t[j]+h)
    k1.append(f(t[j],x[j],y[j]))
    k2.append(f(t[j]+(h/2),x[j]+(h/2)*k1[j],y[j]+(h/2)*k1[j]))
    k3.append(f(t[j]+(h/2),x[j]+(h/2)*k2[j],y[j]+(h/2)*k2[j]))
    k4.append(f(t[j]+h,x[j]+(h*k3[j]),y[j]+(h*k3[j])))
    y.append(y[j]+(h/6)*(k1[j]+2*k2[j]+2*k3[j]+k4[j]))
  
    k11.append(g(t[j],x[j],y[j]))
    k21.append(g(t[j]+(h/2),x[j]+(h/2)*k1[j],y[j]+(h/2)*k1[j]))
    k31.append(g(t[j]+(h/2),x[j]+(h/2)*k2[j],y[j]+(h/2)*k2[j]))
    k41.append(g(t[j]+h,x[j]+(h*k3[j]),y[j]+(h*k3[j])))
    x.append(x[j]+(h/6)*(k11[j]+2*k21[j]+2*k31[j]+k41[j]))
    j+=1

print(x)
print(y)
ax=plt.gca()
line1=ax.plot(t,y,'#660033', marker='d')
line2=ax.plot(t,x, marker='d')
plt.grid()
plt.show()
