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

import UNIDAD5.derivadalimite as derlim
import UNIDAD5.derivadaparcialdifadelante as derivpardelante
import UNIDAD5.Ecuacióndifusión as ecdif
import UNIDAD5.rectangulosint as rectintegr
import UNIDAD5.rectangulovolumen as rectvol
import UNIDAD5.simpson1int as simp1int
import UNIDAD5.simpson1volumen as simpson1vol
import UNIDAD5.simpson2int as simpson2int
import UNIDAD5.trapeciovolumen as trapVol
import UNIDAD5.trapecioint as trapint

import UNIDAD6.eccalor as eCcalor
import UNIDAD6.eccalor3d as Ec3d
import UNIDAD6.ecdiferencialeslaplace as eclaplace
import UNIDAD6.heaviside as hvside
import UNIDAD6.Heun as heun
import UNIDAD6.laplace2024 as laplace24
import UNIDAD6.ode2024 as ode24
import UNIDAD6.rungekutta42204 as rungkut
import UNIDAD6.Sistecdif as sistecdif
import UNIDAD6.sistecdif2023 as sistecdf23

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
                        UNIDAD1.metgrafico2024.f()
                    case 2: 
                        UNIDAD1.newtonraph2024.f()
                        
            break))
        case 3:
            casoMetodo = int(input("Introduzca el metodo a utilizar: 1. para creamer, 2. GaussJordam, 3. GaussSeinel, 4. GaussSimple, 5. Jacobi, 6. Lu, 7. QR "))
            while casoMetodo != 1 or 2 or 3 or 4 or 5 or 6 or 7:
                casoMetodo = int(input("Solo existen siete metodos, por favor seleccione una opcion valida"))
                match casoMetodo:
                    case 1:
                        UNIDAD3.cramer.f()
                    case 2:
                        UNIDAD3.GaussJordan.f()
                    case 3:
                        UNIDAD3.GaussSeidel.f()
                    case 4:
                        UNIDAD3.GaussSimple.f()
                    case 5:
                        UNIDAD3.Jacobi.f()
                    case 6:
                        UNIDAD3.LU.f()
                    case 7:
                        UNIDAD3.QR.f()
        case 4:
            casoMetodo = int(input("Introduzca el metodo a utilizar: 1. Lagrange, 2. Newtonpol, 3. PIU, 4. Regresion, 5. Regresion multilineal, 6. Regresion Lineal "))
            while casoMetodo != 1 or 2 or 3 or 4 or 5 or 6:
                casoMetodo = int(input("Solo existen seis metodos, por favor seleccione una opcion valida"))
                match casoMetodo:
                    case 1:
                        UNIDAD4.lagrange.f()
                    case 2:
                        UNIDAD4.newtonpol.f()
                    case 3:
                        UNIDAD4.PIU.f()
                    case 4:
                        UNIDAD4.regresion.f()
                    case 5:
                        UNIDAD4.regresionmultilineal.f()
                    case 6:
                        UNIDAD4.regresiónlineal.f()
        case 5:
            casoMetodo = int(input("Introduce el numero de la funcion a ejecutar: 1.DerivadaLimite 2. DerivadaParcial 3. Ecuacion de Difusion  4. Integracion por rectangulos 5. Rectangulo Volumen 6. Metodo Simpson 1/3 7. Metodo Simpson 1/3 (volumen) 8. Simpson 3/8 9. Integracion por Trapecio 10. Integracion por trapecio volumen "))
            while casoMetodo != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                casoMetodo = int(input("Por favor Ingrese un numero perteneciente al indice: "))

            def Switch_Caso_5(casoMetodo):
                match casoMetodo:
                    case 1:
                        derlim.DerivadaLimite()
                    case 2:
                        derivpardelante.DerivadaParcial()
                    case 3:
                        ecdif.EcuacionDifusion()
                    case 4:
                        rectintegr.IntegracionRect()
                    case 5:
                        rectvol.RecVol()
                    case 6:
                        simp1int.simpson1()
                    case 7:
                        simpson1vol.simpson1vol()
                    case 8:
                        simpson2int.simpson2()
                    case 9:
                        trapint.integracionTrap()
                    case 10:
                        trapVol.IntTrapVol()

        case 6:
            casoMetodo = int(input("Introduce el numero de la funcion a ejecutar: 1.EcuacionCalor 2. EcuacionCalor3D 3. Diferenciales de Laplace  4. Heaviside 5. Heun 6. laplace 7. ode 8. Rungekutta 9. SistemaDeEcuacionesDiferenciales 10. SistemaDeEcuacionesDiferenciales2023"))
            while casoMetodo != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                casoMetodo = int(input("Por favor Ingrese un numero perteneciente al indice: "))
            def Switch_Caso_6(casoMetodo):
                match casoMetodo:
                    case 1:
                        eCcalor.FuncionCalor()
                    case 2:
                        Ec3d.eccalor3d()
                    case 3:
                        eclaplace.difLaplace()
                    case 4:
                        hvside.Heavyside
                    case 5:
                        heun.heun
                    case 6:
                        laplace24.laplace
                    case 7:
                        ode24.ode24()
                    case 8:
                        rungkut.rungekutta()
                    case 9:
                        sistecdif.Sistedif()
                    case 10:
                        sistecdf23.sisdif23()


