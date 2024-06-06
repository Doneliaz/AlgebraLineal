print("Bienvenido a la terminal del programa")




def main():
    casoUnidad=100
    while casoUnidad != 0:
        casoUnidad = int(input("Que unidad quiere inicializar?: "))
        match casoUnidad:
            case 1:
                casoMetodo = int(input("Introduce el nombre de la función a ejecutar: 1. Para Método Gráfico, 2. Para el Método Newton Raphson"))
                while casoMetodo not in [1, 2]:
                    casoMetodo = int(input("Solo existen dos métodos, por favor seleccione una opción válida"))
                if casoMetodo == 1:
                    import UNIDAD1.metgrafico2024
                    break
                elif casoMetodo == 2:
                    import UNIDAD1.newtonraph2024
                    break

            case 3:
                casoMetodo = int(input("Introduzca el método a utilizar: 1. para Cramer, 2. GaussJordan, 3. GaussSeidel, 4. GaussSimple, 5. Jacobi, 6. LU, 7. QR"))
                while casoMetodo not in [1, 2, 3, 4, 5, 6, 7]:
                    casoMetodo = int(input("Solo existen siete métodos, por favor seleccione una opción válida"))
                if casoMetodo == 1:
                    import UNIDAD3.cramer
                    break
                elif casoMetodo == 2:
                    import UNIDAD3.GaussJordan
                    break
                elif casoMetodo == 3:
                    import UNIDAD3.GaussSeidel
                    break
                elif casoMetodo == 4:
                    import UNIDAD3.GaussSimple
                    break
                elif casoMetodo == 5:
                    import UNIDAD3.Jacobi
                    break
                elif casoMetodo == 6:
                    import UNIDAD3.LU
                    break
                elif casoMetodo == 7:
                    import UNIDAD3.QR
                    break

            case 4:
                casoMetodo = int(input("Introduzca el método a utilizar: 1. Lagrange, 2. Newtonpol, 3. PIU, 4. Regresión, 5. Regresión multilineal, 6. Regresión Lineal"))
                while casoMetodo not in [1, 2, 3, 4, 5, 6]:
                    casoMetodo = int(input("Solo existen seis métodos, por favor seleccione una opción válida"))
                if casoMetodo == 1:
                    import UNIDAD4.lagrange
                    break
                elif casoMetodo == 2:
                    import UNIDAD4.newtonpol
                    break
                elif casoMetodo == 3:
                    import UNIDAD4.PIU
                    break
                elif casoMetodo == 4:
                    import UNIDAD4.regresion
                    break
                elif casoMetodo == 5:
                    import UNIDAD4.regresionmultilineal
                    break
                elif casoMetodo == 6:
                    import UNIDAD4.regresiónlineal
                    break

            case 5:
                casoMetodo = int(input("Introduce el número de la función a ejecutar: 1. DerivadaLímite, 2. DerivadaParcial, 3. Ecuación de Difusión, 4. Integración por rectángulos, 5. Rectángulo Volumen, 6. Método Simpson 1/3, 7. Método Simpson 1/3 (volumen), 8. Simpson 3/8, 9. Integración por Trapecio, 10. Integración por trapecio volumen"))
                while casoMetodo not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    casoMetodo = int(input("Por favor ingrese un número perteneciente al índice"))
                if casoMetodo == 1:
                    import UNIDAD5.derivadalimite
                    break
                elif casoMetodo == 2:
                    import UNIDAD5.derivadaparcialdifadelante
                    break
                elif casoMetodo == 3:
                    import UNIDAD5.Ecuacióndifusión
                    break
                elif casoMetodo == 4:
                    import UNIDAD5.rectangulosint
                    break
                elif casoMetodo == 5:
                    import UNIDAD5.rectangulovolumen
                    break
                elif casoMetodo == 6:
                    import UNIDAD5.simpson1int
                    break
                elif casoMetodo == 7:
                    import UNIDAD5.simpson1volumen
                    break
                elif casoMetodo == 8:
                    import UNIDAD5.simpson2int
                    break
                elif casoMetodo == 9:
                    import UNIDAD5.trapecioint
                    break
                elif casoMetodo == 10:
                    import UNIDAD5.trapeciovolumen
                    break

            case 6:
                casoMetodo = int(input("Introduce el número de la función a ejecutar: 1. EcuaciónCalor, 2. EcuaciónCalor3D, 3. Diferenciales de Laplace, 4. Heaviside, 5. Heun, 6. Laplace, 7. ODE, 8. RungeKutta, 9. SistemaDeEcuacionesDiferenciales, 10. SistemaDeEcuacionesDiferenciales2023"))
                while casoMetodo not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    casoMetodo = int(input("Por favor ingrese un número perteneciente al índice"))
                if casoMetodo == 1:
                    import UNIDAD6.eccalor
                    break
                elif casoMetodo == 2:
                    import UNIDAD6.eccalor3d
                    break
                elif casoMetodo == 3:
                    import UNIDAD6.ecdiferencialeslaplace
                    break
                elif casoMetodo == 4:
                    import UNIDAD6.heaviside
                    break
                elif casoMetodo == 5:
                    import UNIDAD6.Heun
                    break
                elif casoMetodo == 6:
                    import UNIDAD6.laplace2024
                    break
                elif casoMetodo == 7:
                    import UNIDAD6.ode2024
                    break
                elif casoMetodo == 8:
                    import UNIDAD6.rungekutta42204
                    break
                elif casoMetodo == 9:
                    import UNIDAD6.Sistecdif
                    break
                elif casoMetodo == 10:
                    import UNIDAD6.sistecdif2023
                    break
            case _:
                print("Unidad no reconocida, por favor seleccione una unidad válida.")
                casoUnidad = int(input("Que unidad quiere inicializar?: "))

main()

