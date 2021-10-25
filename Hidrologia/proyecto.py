import numpy as np
import matplotlib.pyplot as plt

def a(x):
    return np.sin(x)

g= lambda x: np.cos(x)

v=[0, 10, -1, 1]

x=np.linspace(0, 10, 100)

plt.plot(x, a(x), 'r--', label="seno", )
plt.plot(x, g(x), label="coseno")
plt.xlabel("Tiempo")
plt.ylabel("Posicion")
plt.legend(loc=1)
plt.title("Prueba Hidrología")
plt.text(4, 0, "Prueba")
plt.axis(v)
plt.grid()