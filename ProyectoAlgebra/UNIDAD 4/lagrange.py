from sympy import Symbol, simplify, lambdify
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import operator

def interpolacion_lagrange(x, x_values, y_values):
   
    def _bases(j):
        p = [(x - x_values[m])/(x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)
    assert len(x_values) != 0 and (len(x_values) == len(y_values)), 'x y no pueden ser vacíos'
    k = len(x_values)
    return sum(_bases(j)*y_values[j] for j in range(k)) 

x = Symbol('x')
poly = simplify(interpolacion_lagrange(x,[0,8,16,24,32,40],[14.621,11.843,9.87,8.418,7.35, 6.413]))
print('El polinomio de interpolación de Lagrange es')
print(poly)

x1 = np.linspace(0, 45, 100)
y1 = lambdify(x, poly)(x1)

fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.scatter([27],[7.986 ], c = 'r')
plt.show()
