def metodoQR(a,b):
    print('Método QR')
    A=input('Ingrese la matriz ')
    b=input('Ingrese el vector de coeficientes ')
    
    A=np.mat(A,dtype=float)
    b=np.mat(b,dtype=float)
    a=A.shape
    proy=np.zeros(a[1])
    proy=np.mat(proy,dtype=float)
    x=np.zeros(a[1])
    x=np.mat(x,dtype=float)
    Q=np.zeros([a[0],a[1]],dtype=float)
    Q=np.mat(Q,dtype=float)
    R=np.zeros([a[0],a[1]],dtype=float)
    R=np.mat(R,dtype=float)
    
    Q[::,0]=A[::,0]/LA.norm(A[::,0])
    
    for i in range(1,a[1]):
        for j in range(0,i):
            proy=np.dot(np.dot(A[::,i].T,Q[::,j]),Q[::,j].T)+proy
            Q[::,i]=A[::,i]-proy.T;
            Q[::,i]=Q[::,i]/LA.norm(Q[::,i])
        proy=np.zeros(a[1])
        proy=np.mat(proy,dtype=float)
    
    R=Q.T*A
    print('La matriz Q es ')
    print(np.around(Q, decimals=2))
    print('La inversa de Q es ')
    print(np.around(Q.T, decimals=2))
    print('La matriz R es ')
    print(np.around(R, decimals=2))
    