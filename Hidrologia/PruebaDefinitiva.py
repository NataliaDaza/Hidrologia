# import csv
# with open('DATOSCUNDINAMARCA - copia.csv') as fp:
#     reader = csv.reader(fp)
#     for row in reader:
#         print(row)


import pandas

weather = pandas.read_csv('DATOSCUNDINAMARCA.txt',encoding='utf-8')
print(weather)



import matplotlib.pyplot as plt

rainfall = weather['Fecha'].to_list()
plt.plot(rainfall)
plt.show()