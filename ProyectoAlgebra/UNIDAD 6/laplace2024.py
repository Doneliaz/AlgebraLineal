import sympy
sympy.init_printing()
import matplotlib.pyplot as plt


t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

f = sympy.exp(-a*t)
print(f)

#print(sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo)))

F = sympy.laplace_transform(f, t, s, noconds=True)
print(F)

def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)
