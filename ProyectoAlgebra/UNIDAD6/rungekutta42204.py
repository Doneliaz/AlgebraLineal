import numpy as np
import matplotlib.pyplot as plt

def rungekutta():
    y0 = 1
    def f(y,t):
        return 2*(1-y) - np.exp(-4*t)

    points = 21
    t = np.linspace(0,2,points)
    ##### Calculo del tamaño del paso #####
    h = t[2]-t[1]

    ##### Solución Analítica #####
    t_ana = np.linspace(0,2,51)
    y_ana = 1/(2*np.exp(4*t_ana)) + 1 - 1/(2*np.exp(2*t_ana))

    def Euler_metodo(f,y0,t):
        y = np.zeros(len(t))
        y[0] = y0
        for i in range(0,len(t)-1):
            y[i+1] = y[i] + f(y[i],t[i])*(t[i+1]-t[i])
        return y
    y_Euler = Euler_metodo(f,y0,t)

    def RK_metodo(f,y0,t):
        y = np.zeros(len(t))
        y[0] = y0
        for i in range(0,len(t)-1):
            h = t[i+1]-t[i]
            F1 = h*f(y[i],t[i])
            F2 = h*f((y[i]+F1/2),(t[i]+h/2))
            F3 = h*f((y[i]+F2/2),(t[i]+h/2))
            F4 = h*f((y[i]+F3),(t[i]+h))
            y[i+1] = y[i] + 1/6*(F1 + 2*F2 + 2*F3 + F4)
        return y
    y_RK = RK_metodo(f,y0,t)


    ##### Solución Analítica #####
    t_ana = np.linspace(0,2,51)
    y_ana = 1/(2*np.exp(4*t_ana)) + 1 - 1/(2*np.exp(2*t_ana))

    plt.figure(num=1, dpi=150, figsize=(7, 5))
    plt.rcParams["font.family"] = "serif"
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['savefig.facecolor']='white'
    plt.plot(t_ana,y_ana,'ro',label = "Solución Analítica",markersize=2.5)
    plt.plot(t,Euler_metodo(f,y0,t),'b-', label = "Euler")
    plt.plot(t,RK_metodo(f,y0,t),'k-', label = "Runge Kutta")
    plt.legend(loc=4)
    plt.grid(True, color='lightgray')
    plt.xlabel("$t$ (-)")
    plt.ylabel("$y$ (-)")
    plt.ylim([0.75,1])
    plt.text(s='Método de Euler vs. Runge Kutta Orden 4', x=1, y=1.03, fontsize=15, ha='center', va='center')
    plt.text(s=f'n = {points}, h = {h:.3f}', x=1, y=1.01, fontsize=11, ha='center', va='center')
    plt.savefig('euler_rk_output.png', transparent=False, bbox_inches="tight")
    plt.show()
