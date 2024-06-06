def LU(a,b):
   print('Método LU')
   A=input('Ingrese la matriz ')
   b=input('Ingrese el vector de coeficientes ')
   A=np.mat(A,dtype=float)
   b=np.mat(b,dtype=float)
   a=A.shape
   U=np.matrix.copy(A)
   y=np.zeros(a[1])
   y=np.mat(y,dtype=float)
   x=np.zeros(a[1])
   x=np.mat(x,dtype=float)
   L=np.zeros([a[0],a[0]],dtype=float)
   L=np.mat(L,dtype=float)
   
   for i in range(0,a[1]):
      L[i,i]=1
      for j in range (i+1,a[0]):
           L[j,i]=U[j,i]/U[i,i]
           U[:][j]=U[:][j]-((U[j,i]/U[i,i])*U[:][i])
   
   print(A)
   input()
   print('La matriz U es')
   print(np.around(U, decimals=2))
   print('La matriz L es')
   print(np.around(L, decimals=2))
   print('La solución del sistema Ly=b es')
   #[[4 -2 1];[20 -7 12]; [-8 13 17]]
   #[[11 70 17]]
   
   y[0,0]=b[0,0]
   
   print(L[2,0:2])
   print(b.T[0:2])
   
   for i in range(1,a[1]):
      y[0,i]=b[0,i]-np.dot(L[i,0:i],y.T[0:i])
   print(np.around(y, decimals=2))
   
   
   x[0,a[1]-1]=(round(y[0,a[1]-1]/U[a[0]-1,a[1]-1],2))
   print(x)
   print('La solución del sistema Ux=y ')
   for i in range(a[1]-2,-1,-1):
       x[0,i]=(y[0,i]-np.dot(U[i,i+1:a[1]],x.T[i+1:a[1]]))/U[i,i]
   print(np.around(x, decimals=2))


