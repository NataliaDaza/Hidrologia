



import pandas as pd
data = pd.read_csv('G:\\Hidrología\\estaciones\\DATOS_CUNDINAMARCA.txt',sep=' ',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]
y = data[1]

plt.axis()
plt.plot(x, y,'b-')


plt.figure(figsize=(3, 3), dpi=1200)
plt.show()
