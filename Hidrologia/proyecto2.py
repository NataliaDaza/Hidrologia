
import matplotlib.pyplot as plt
import pandas as pd


var= pd.read_excel('G:\\Hidrología\\estaciones\\ELHATO,ELVERJON,SANDIEGO_KEV.xlsx', 'ejemplo')

varNew=var[['Fecha']]
varNew.head()
plt.plot(str(varNew))
v=[0, 80, '1/01/2000', '13/04/2011']
plt.axis(v)
plt.show()



