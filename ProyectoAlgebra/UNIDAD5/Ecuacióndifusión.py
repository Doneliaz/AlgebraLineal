#Ecuación de Difusión dU/dt=D(d^2U/dx^2 +d^2U/dy^2)
#Diferencias finitas x,y en [0,1] uij(n) con x=ideltax y=jdeltay

import numpy as np
import matplotlib.pyplot as plt
def EcuacionDifusion():
    # tamaño de la placa, mm
    w = h = 10.
    # tamaño del paso, mm
    dx = dy = 0.1
    # coeficiente de difusión térmica del acero D = 4. (mm^2/s)
    D=4
    Tfria, Tcaliente = 300, 700

    nx, ny = int(w/dx), int(h/dy)

    dx2, dy2 = dx*dx, dy*dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    u0 = Tfria * np.ones((nx, ny))
    u = u0.copy()

    # Condiciones iniciales - círculo de radio r con centro en (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r**2
    for i in range(nx):
        for j in range(ny):
            p2 = (i*dx-cx)**2 + (j*dy-cy)**2
            if p2 < r2:
                u0[i,j] = Tcaliente

    def do_timestep(u0, u):
        # Se propagan con diferencias hacia adelante en el tiempo
        # y con diferencias centradas en el espacio
        u[1:-1, 1:-1] = u0[1:-1, 1:-1] + D * dt * (
            (u0[2:, 1:-1] - 2*u0[1:-1, 1:-1] + u0[:-2, 1:-1])/dx2
            + (u0[1:-1, 2:] - 2*u0[1:-1, 1:-1] + u0[1:-1, :-2])/dy2 )

        u0 = u.copy()
        return u0, u

    # Número de pasos
    nsteps = 101
    # Muestra 4 casos (tiempos distintos)
    mfig = [0, 10, 50, 100]
    fignum = 0
    fig = plt.figure()
    fig.suptitle("Difusión en el tiempo t \n", fontsize=15)
    for m in range(nsteps):
        u0, u = do_timestep(u0, u)
        if m in mfig:
            fignum += 1
            ax = fig.add_subplot(220 + fignum)
            im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=Tfria,vmax=Tcaliente)
            ax.set_axis_off()
            ax.set_title('{:.1f} ms'.format(m*dt*1000))
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()




