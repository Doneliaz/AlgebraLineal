from sympy import Symbol, simplify, lambdify
import numpy as np

float_formatter = "{:.6f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})
def polinomio_newton_coeficientes(valx,valy):
    poli=0
    m = len(valx)

    valx = np.copy(valx)
    a = np.copy(valy)
    for k in range(1,m):
        a[k:m] = ((a[k:m] - a[k-1])/(valx[k:m] - valx[k-1]))

    f = np.zeros(m)
    
    for i in range(0, m):
        f[i] = a[i]

    #Imprimir el polinomio como producto
    print("El polinomio es:")
    print("p(x)={:+.5f}".format(f[0]), end="")
    for i in range(1, m):
        print("{:+.4f}".format(f[i]), end="")
        for j in range(1, i+1 ):
            print("(x{:+.4f})".format(valx[j] * -1), end="")
            poli=poli+valx[j] * -1
    print("")
    
    return [poli]

#pol=polinomio_newton_coeficientes([10,20,30],[.1763,.364,.5774])
pol=polinomio_newton_coeficientes([0,1/3,2/3,1],[1,1.39561,1.94773,2.71828])







#print(newton_pol([-4,-3,1,2,4,5,8,10],[-1.4,1,-.03,.4,.6,.5,.2,-.5]),x)
