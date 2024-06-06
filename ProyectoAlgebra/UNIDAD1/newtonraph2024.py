from sympy import symbols, diff

def funcion(x):
    return x**3 - 2*x - 5

def newton_raphson(a, tol=1e-4, error=1):
    iteracion = 0
    x = symbols('x')
    f_x = funcion(x)
    f_derivada = diff(f_x, x)
    f = lambda x_val: f_x.subs(x, x_val)
    derivada = lambda x_val: f_derivada.subs(x, x_val)

    print("Iteración |   x    |  f(x)  |  f'(x)  |  error=|f(x)|")
    print("-" * 55)
    while error>tol:
        f_a = f(a)
        derivada_a = derivada(a)
        b = a - f_a / derivada_a
        error = abs(f_a)

        print(f"{iteracion:^9} | {a:^7.4f} | {f_a:^7.4f} | {derivada_a:^7.4f} | {error:^11.4f}")

        a = b
        iteracion += 1

    print("-" * 55)
    print(f"La raíz aproximada es: {a:.6f}")
    print(f"Error: {error:.6f}")

# Solicitar intervalo al usuario y verificar si contiene una raíz

a= float(input("Ingrese una estimación inicial para x: "))

 
# Llamar a la función de Newton-Raphson
newton_raphson(a)
