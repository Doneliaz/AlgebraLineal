#Programa de terminal

import UNIDAD1.metgrafico2024
import UNIDAD1.newtonraph2024
import UNIDAD3.cramer
import UNIDAD3.GaussJordan
import UNIDAD3.GaussSeidel
import UNIDAD3.GaussSimple
import UNIDAD3.Jacobi
import UNIDAD3.LU
import UNIDAD3.QR
import UNIDAD4.lagrange
import UNIDAD4.newtonpol
import UNIDAD4.PIU
import UNIDAD4.regresion
import UNIDAD4.regresionmultilineal
import UNIDAD4.regresiónlineal
import UNIDAD5.derivadalimite
import UNIDAD5.derivadaparcialdifadelante
import UNIDAD5.Ecuacióndifusión
import UNIDAD5.rectangulosint
import UNIDAD5.rectangulovolumen
import UNIDAD5.simpson1int
import UNIDAD5.simpson1volumen
import UNIDAD5.simpson2int
import UNIDAD5.trapeciovolumen
import UNIDAD5.trapecioint
import UNIDAD6.Ecuacióndifusión
import UNIDAD6.eccalor
import UNIDAD6.eccalor3d
import UNIDAD6.ecdiferencialeslaplace
import UNIDAD6.heaviside
import UNIDAD6.Heun
import UNIDAD6.laplace2024
import UNIDAD6.ode2024
import UNIDAD6.rungekutta42204
import UNIDAD6.Sistecdif
import UNIDAD6.sistecdif2023

print("Bienvenido a la terminal del programa")
casoUnidad = int(input("Que unidad quiere inicializar?: "))

while casoUnidad != 1 or 2 or 3 or 4 or 5 or 6:
    if casoUnidad == 2:
        casoUnidad = int(input("La unidad 2 No se encuentra Disponible, por favor intente otra unidad: "))
        metgrafico.f(3)
    else:
        casoUnidad = int(input("El valor seleccionado no pertenece a la unidad, por favor seleccione una unidad del 1 al 6"))
        
        break

def SwitchUnidades(casoUnidad):
    match casoUnidad:
    
        case 1:
            casoMetodo = int(input("Introduce el nombre de la funcion a ejecutar: 1. Para Metodo Grafico, 2. Para el     Metodo Newton Raphson"))

            while casoMetodo != 1 or 2:
                casoMetodo = int(input("Solo existen dos metodos, por favor seleccione una opcion valida"))
            def Switch_Caso_1(casoMetodo):
                match casoMetodo:
                    case 1:
                        
                    case 2: 
                        
            break))
        case 3:
            casoMetodo = int(input("Introduzca el metodo a utilizar: 1. para "))
        case 4:
        case 5:
        case 6:
