import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def ode24():

    plt.style.use('seaborn-poster')



    F = lambda t, s: np.cos(t)

    t_eval = np.arange(0, np.pi, 0.1)
    sol = solve_ivp(F, [0, np.pi], [0], t_eval=t_eval)
    print(sol)

    plt.figure(figsize = (12, 4))
    plt.subplot(121)
    plt.plot(sol.t, sol.y[0])
    plt.xlabel('t')
    plt.ylabel('S(t)')
    plt.subplot(122)
    plt.plot(sol.t, sol.y[0] - np.sin(sol.t))
    plt.xlabel('t')
    plt.ylabel('S(t) - sin(t)')
    plt.tight_layout()
    plt.show()
