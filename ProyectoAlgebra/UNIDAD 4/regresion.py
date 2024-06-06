import numpy as np
from numpy import linalg
x=np.array([55,85,100,120])
x=np.vander(x,increasing=True)
x=np.mat(x)
y=np.array([15,20,25,35])
y=np.mat(y)
A=x.transpose()*x
b=x.transpose()*y.transpose()


#Regresión Lineal
print(A)
AA=A[0:2,0:2]
print(AA)
bb=b[0:2]
cc=linalg.solve(AA,bb) #Gauss Jordan
print('Los coeficientes de la regresión lineal en orden ascendente son: ')
print(np.around(cc,decimals=2))
#Regresión Polinomial lineal (grado n)
c=linalg.solve(A,b)
print('Los coeficientes de la regresión polinomial en orden ascendente son: ')
print(np.around(c,decimals=10))
