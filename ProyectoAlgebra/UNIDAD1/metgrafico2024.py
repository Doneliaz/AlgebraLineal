def f(a):
    return x**3 - 2*x**2 + 2

# Crea un rango de valores para x
x_values = np.linspace(-5, 5, 100)

# Calcula los valores correspondientes de y
y_values = f(x_values)

# Grafica la función
plt.plot(x_values, y_values, label='f(x) = x^3 - 2x^2 + 2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y=0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x=0
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Ahora puedes continuar con el método de bisección
