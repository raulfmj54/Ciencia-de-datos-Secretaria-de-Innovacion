import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
titanic_df = pd.read_csv("Tarea 3/Listade Pasajeros del Titanic.csv")

print(titanic_df , " \n")

#Generamos un nuevo dataset con campos no vacios en la columna de Sexo
survivor__class_counts = titanic_df.groupby('Clase')['Sobrevivió'].sum()
print(survivor__class_counts)

#Generamos x con los labels, y con los valores
x = np.array(["Clase 1", "Clase 2", "Clase 3"])
y = np.array([survivor__class_counts[1],survivor__class_counts[2],survivor__class_counts[3]])


mylabels = ["Clase 1", "Clase 2", "Clase 3"]

plt.bar(x,y, color=['blue','cyan', 'red'])
plt.legend(handles=mylabels, loc='best')  
plt.show()
