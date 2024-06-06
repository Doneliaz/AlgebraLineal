import numpy as np
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
def eccalor3d():
    kx = 25
    ky = 25
    kz = 25
    largx = 90  
    largy = 90
    largz = 90   
    
    dt4 = 1/2 
    dx4 = largx/(kx-1)    #Position deltas.
    dy4 = largy/(ky-1)
    dz4 = largz/(kz-1) 
    
    Tin = 25    
    kapp = 0.13
    
    Tamb3d = 150 
    
    
    qq1=0 / (largx*largz)  #Enfriar
    qq2=0 / (largx*largz)
    qq3=0 / (largz*largy)
    qq4=0 / (largz*largy)
    qq5=0 / (largx*largy)
    qq6=1000 / (largx*largy)
    
    
    x4 = np.linspace(0,largx,kx)   
    y4 = np.linspace(0,largy,ky)
    z4 = np.linspace(0,largz,kz)
    
    
    #Defining the function.
    def diff3d(tt):
        
        w2 = np.ones((kx,ky,kz))*Tin        
        wn2 = np.ones((kx,ky,kz))*Tin
        
        for k in range(tt+2):
            wn2 = w2.copy()
            w2[1:-1,1:-1,1:-1] = (wn2[1:-1,1:-1,1:-1] + 
                            kapp*dt4 / dy4**2 *                                       
                            (wn2[1:-1, 2:,1:-1] - 2 * wn2[1:-1, 1:-1,1:-1] + wn2[1:-1, 0:-2,1:-1]) +  
                            kapp*dt4 / dz4**2 *                                       
                            (wn2[1:-1,1:-1,2:] - 2 * wn2[1:-1, 1:-1,1:-1] + wn2[1:-1, 1:-1,0:-2]) +
                            kapp*dt4 / dx4**2 *
                            (wn2[2:,1:-1,1:-1] - 2 * wn2[1:-1, 1:-1,1:-1] + wn2[0:-2, 1:-1,1:-1]))
    
            #Condiciones de Neumann
            w2[0,:,:] =   w2[0,:,:] + 2*kapp* (dt4/(dx4**2)) * (w2[1,:,:] - w2[0,:,:] - qq1 * dx4/kapp)
            w2[-1,:,:] =  w2[-1,:,:] + 2* kapp*(dt4/(dx4**2)) * (w2[-2,:,:] - w2[-1,:,:] + qq2 * dx4/kapp)
            w2[:,0,:] =   w2[:,0,:] + 2*kapp* (dt4/(dx4**2)) * (w2[:,1,:] - w2[:,0,:] - qq3 * dx4/kapp)
            w2[:,-1,:] =  w2[:,-1,:] + 2*kapp* (dt4/(dx4**2)) * (w2[:,-2,:] - w2[:,-1,:] + qq4 * dx4/kapp)
            w2[:,:,0] =   w2[:,:,0] + 2 *kapp* (dt4/(dx4**2)) * (w2[:,:,-1] - w2[:,:,0] - qq5 * dx4/kapp)
            w2[:,:,-1] =   w2[:,:,-1] + 2 *kapp* (dt4/(dx4**2)) * (w2[:,:,-2] - w2[:,:,-1] + qq6 * dx4/kapp)
           
        w2[1:,:-1,:-1] = np.nan    #Solamente se grafican las caras
        w2_uno = np.reshape(w2,-1)    
    
      
        fig = pyplot.figure()
        X4, Y4, Z4 = np.meshgrid(x4, y4,z4)
        ax = fig.add_subplot(111, projection='3d')
        img = ax.scatter(X4, Y4, Z4, c=w2_uno, cmap=pyplot.jet())
        fig.colorbar(img)
        pyplot.show()
    
    diff3d(20000)
