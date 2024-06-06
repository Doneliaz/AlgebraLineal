def metodoCramer(a,b,c):
    print('Método de Cramer')
    A=input('Ingrese la matriz ')
    C=input('Ingrese nuevamente la matriz ')
    b=input('Ingrese el vector de coeficientes ')
    A=np.mat(A)
    C=np.mat(C)
    b=np.mat(b)
    a=A.shape
    x=[]
    
    if a[0]==a[1]:
        detA=np.linalg.det(A)
        if detA==0:
            print('No puede usarse este método. A no es invertible')
        else:
            for i in range(0,a[0]):
                A[::,i]=b.T
                print(A)
                x.append(round(np.linalg.det(A)/detA,1))
                print(x)
                print(C)
                A=np.matrix.copy(C)
                
        print('La solución es ')
        print(x)
    
    else:
        print('No se puede utilizar el método de Cramer. A no es cuadrada')
    
    #[[3 -2 4];[2 -2 0]; [-1 0 4]]
    #[[1 3 2]]
