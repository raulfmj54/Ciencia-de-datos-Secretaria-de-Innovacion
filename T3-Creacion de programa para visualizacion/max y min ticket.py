import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
sobrevivio_df = pd.read_csv("Tarea 3/Listade Pasajeros del Titanic.csv")

print(sobrevivio_df , " \n")

print(sobrevivio_df.describe(), " \n")

print(sobrevivio_df.info(), " \n")

# Echemos un vistazo a las columnas
print(sobrevivio_df.columns, " \n")


#sacamos min y max
sobrevivio_df_c =  sobrevivio_df['Tarifa'].replace(0, np.NaN)
survivors_count = sobrevivio_df_c[sobrevivio_df['Tarifa'].notnull()]
print(survivors_count, " \n")
max = survivors_count.max()
min = survivors_count.min()

# Echemos un vistazo a los valores
print("Ticket mas caro: ",max, " \n")
print("Ticket mas barato: ",min, " \n")
