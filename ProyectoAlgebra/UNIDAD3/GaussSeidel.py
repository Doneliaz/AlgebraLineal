def GaussSeidel(a,b):
    print('Método de Gauss Seidel')
    print('Método Iterativo')
    import numpy as np
    A=input('Ingrese la matriz ')
    b=input('Ingrese el vector de coeficientes ')
    tol=float(input('Ingrese la tolerancia '))
    A=np.mat(A,dtype=float)
    b=np.mat(b,dtype=float)
    a=A.shape
    x=np.zeros(a[1])
    x=np.mat(x)
    y=np.zeros(a[1])
    y=np.mat(y)
    error=1100
    while error>tol:
        y=np.copy(x)
        for i in range(0,a[1]):
            x[0,i]=(b[0,i]-(np.dot(A[i,0:i],x.T[0:i]))-(np.dot(A[i,i+1:a[1]-1],x.T[i+1:a[1]-1])))/A[i,i]             
            
        error=np.amax(abs(y-x))
        print(x)
    

        
    print('La mejor aproximación es')
    print(x)
