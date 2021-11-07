import pandas as pd
import matplotlib.pyplot as plt

var= pd.read_excel('G:\\Hidrología\\estaciones\\ELHATO,ELVERJON,SANDIEGO_KEV.xlsx', 'prueba')
newvar=var[['PRECIPITACION GENERAL']]
plt.plot(newvar, 'r--', label="valor")
plt.xlabel("Año")
plt.ylabel("Precipitación(m.m)")
plt.title("Test Hidrología")
plt.legend(loc=2)
plt.grid()
plt.axis()
plt.xticks() 

newvar.head()
