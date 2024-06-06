def GaussJordan():
    print('Método Gauss Jordan')
    A=input('Ingrese la matriz ')
    b=input('Ingrese el vector de coeficientes ')

    A=np.mat(A,dtype=float)
    b=np.mat(b,dtype=float)
    C=np.concatenate([A,b.T],axis=1)
    a=A.shape
    x=np.zeros(a[1])
    x=np.mat(x)

    #Ciclo para hacer la matriz triangular superior
    #(Arriba abajo, izq. derecha)
    for i in range(0,a[1]):#columnas
        C[:][i]=C[:][i]/C[i,i]#filas
        for j in range (i+1,a[0]):
            C[:][j]=C[:][j]-((C[j,i]/C[i,i])*C[:][i])
            print(np.around(C, decimals=2))
            input()
            
    #Ciclo para obtener la diagonal (Abajo arriba,derecha izq.)
    for i in range(a[1]-1,-1,-1):
        for j in range (i-1,-1,-1):
            C[:][j]=C[:][j]-((C[j,i]/C[i,i])*C[:][i])
            #print(C)
            #input()
            print(np.around(C, decimals=2))
            input() 

    x=np.around(C[::,a[1]],decimals=2)
    print('La solución es ')
    print(x.T)

    #[[3 -2 4 1 -3];[2 -2 0 1 11]; [-1 0 4 -8 4] ; [4 2 7 0 1] ; [2 8 3 5 6]]
    #[[1 3 2 4 6]]

    #[[ 1 -2 4 -8]; [1 -1 1 -1]; [1 1 1 1]; [1 2 4 8]]
    #[[-4 1 2 3]]

    #[[1,0,1,0];[-6,1,0,1];[15,-6,9,0];[0,15,0,9]]
    #[[-1,2,-9,24]]

