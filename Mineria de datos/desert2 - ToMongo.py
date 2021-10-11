import connection as net
##import quandl
import pandas as pd

db = net.client.test

mydb = net.client["mydatabase"] 
#Seleccionamos la base de datos

mycol = mydb["desert"]
#Seleccionamos la colección


# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
df = pd.read_csv("mineria de datos/data/surveys.csv")

df10 = df.head(10)

print(df10)