import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el calor en un punto dado
def funcionCalor(x):
    if x>0:
        return ((np.exp(-2*(x**(-2)))/100)+4*x**3)
    else:
        return 0

N = 100
x = np.linspace(0,1,N+1)

deltax = .1
deltat = .0045
mu = deltat/deltax**2


A = np.zeros([N-1,N-1])
np.fill_diagonal(A,1-2*mu)
for i in range(1,N-1):
    A[i,i-1] = mu
    A[i-1,i] = mu
print("La matriz A es ", A)

u = np.vectorize(f)(x)

deltax = 0.0045
deltat = (deltax**2)/2
#Graficamos la función de la temperatura, almacenando solo sus valores en el tiempo final
tiempofinal = 0.5
nt = int(tiempofinal/deltat)

for i in range(nt):
    u[1:N] = A.dot(u[1:N])
    
plt.plot(x,u)
plt.plot(x,np.vectorize(f)(x),'o-')
plt.grid(True)

plt.show()
