import sympy
def difLaplace():
    sympy.init_printing()

    import matplotlib.pyplot as plt


    t, s = sympy.symbols('t, s')
    a = sympy.symbols('a', real=True, positive=True)

    f = sympy.exp(-a*t)
    print(f)


    #Método por integración
    res=sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo))
    print(res)

    #Método directo
    lap=sympy.laplace_transform(f, t, s)
    print(lap)

    F = sympy.laplace_transform(Heaviside(t), t, s, noconds=True)
    print(F)
    F2=2/(s**4)
    F3 = ((s + 1)*(s + 2)* (s + 3))/((s + 4)*(s + 5)*(s + 6))
    print(F3)
    print(F3.apart(s))
    def L(f):
        return sympy.laplace_transform(f, t, s, noconds=True)
    def invL(F):
        return sympy.inverse_laplace_transform(F, s, t)

    print(L(f))
    print(invL(F))
    print(invL(F3))
    print(invL(F3).simplify())

