import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# Definir parámetros
f = lambda t, s: 2*t*(s**2) # Ec. Diferencial ordinaria
h = 0.5 # Tamaño del paso
t = np.arange(0, 2+h, h) # 
s0 = 1 # Condición Inicial

# Método de Heun
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + (h/2)*(f(t[i], s[i]) + f(t[i+1], s[i]+ h*f(t[i], s[i])))

print(s)
plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximación')
#plt.plot(t, -np.exp(-t), 'g', label='Exacta')
plt.title('Solución exacta y aproximada ')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
