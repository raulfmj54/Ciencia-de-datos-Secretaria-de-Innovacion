import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
titanic_df = pd.read_csv("Tarea 3/Listade Pasajeros del Titanic.csv")

print(titanic_df , " \n")

#Generamos un nuevo dataset con campos no vacios en la columna de Sexo
survivor_counts = titanic_df.groupby('Sobrevivió')['Sobrevivió'].count()
print(survivor_counts)

y = np.array([ survivor_counts[0], survivor_counts[1]])

mylabels = ["No sobrevivio", "Sobrevivio"]

plt.pie(y, labels = mylabels, shadow = True,
        autopct='%1.1f%%', startangle=90, colors =["#8c564b","#9467bd"])
plt.legend(title = "Cantidad de sobrevivientes \n"+"del titanic:")
plt.show()