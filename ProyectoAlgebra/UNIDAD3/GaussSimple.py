def GaussSimple(a,b):
   print('Método Gauss simple')
   print('Triangular Superior usando sustitución regresiva')
   A=input('Ingrese la matriz ')
   b=input('Ingrese el vector de coeficientes ')
   A=np.mat(A,dtype=float)
   b=np.mat(b,dtype=float)
   C=np.concatenate([A,b.T],axis=1) #concatenate añade una columna
   a=A.shape
   x=np.zeros(a[1])# x=[0 0 0]el vector de 0's porque empiezo del final #append empiezo del principio
   x=np.mat(x)
   print(C)
   
    #CALCULAR LA MATRIZ TRIANGULAR SUPERIOR
   for i in range(0,a[1]):  # i representa las columnas  range(0,7) 
      for j in range (i+1,a[0]): #j representa las filas
           C[:][j]=C[:][j]-((C[j,i]/C[i,i])*C[:][i])  
           print(np.around(C, decimals=2)) #around redondea 
           input()
           
   #RESOLVEMOS SISTEMA DE ECUACIONES
   x[0,a[1]-1]=(C[a[0]-1,a[1]])/(C[a[0]-1,a[1]-1]) #solo calcula el último valor
   
   for i in range(a[1]-2,-1,-1): #Empiezo posición dos,
      
      x[0,i]=(C[i,a[1]]-(np.dot(C[i,i+1:a[1]],x.T[i+1:a[1]])))/C[i,i]
      
   print('La solución del sistema es ')
   print(x)
   
   #[[3 -2 4];[2 -2 0]; [-1 0 4]]
   #[[1 3 2]]
    

