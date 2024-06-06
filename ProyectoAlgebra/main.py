#Programa de terminal

from UNIDAD1 import *
import UNIDAD1.metgrafico2024 as metgrafico


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
