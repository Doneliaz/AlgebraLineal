from sympy import *


t=symbols('t')

f=Heaviside(t-pi)-Heaviside(t-2*pi)
plot(f,(t,0,4*pi))

s,t=symbols('s t',positive=True)
#Definimos la funcion escalón en Heaviside
f=2*t+Heaviside(t-2)*(2-2*t)+Heaviside(t-4)*(0-2)
F=laplace_transform(f,t,s) 
print('La transformada de Laplace es',F[0])

print('\n' ,F[0].expand())
