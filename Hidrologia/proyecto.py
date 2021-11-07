#Importante instalar python -m pip install -U pip
#                    python -m pip install -U matplotlib
# Puede arrojar error por compatibilidad, se puede componer con anaconda
# cmd: py -m pip install matplotlib
#      https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
# cmd: carpeta de la descarga 
# cmd: py -m pip install "el nombre del archivo"
# entrar al lenguaje y detectar version: matplotlib.__version__
# Ejecutar la prueba de este repositorio para instalar el kernel en caso de que no esté instalado
# Altas instrucciones las del kev la verdad

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



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

