from sympy import Symbol
import numpy as np

#x=[10,20,30]
#y=[.1763,.3640,.5774]
x=[-2, 3, 1, 4,8,14,5,-6,9]
y=[-1,-3,6,9,-2,5,6,7,-4]
n=len(x)

x=np.array(x)
y=np.array(y)

A=np.vander(x,len(x))

MA=np.linalg.solve(A,y.T) #Resuelve de ecuaciones Gauss Jordan

x = Symbol('x')
pol=0
for i in range(0,len(MA)):
    pol=pol+round(MA[i],4)*(x**(len(MA)-i-1))

print("El polinomio de interpolación único es:")
print(pol)
