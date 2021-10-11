import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importamos la data de pasajeros del titanic ya preparada en csv
titanic_df = pd.read_csv("Tarea 3/Listade Pasajeros del Titanic.csv")

while True: #Generamos el Ciclo repetitivo para el menu
    
    os.system("clear") #Limpieza de pantalla
    print("Menu:")
    print("1. Buscador por tickets")
    print("2. Gráfica de pastel de muertos y sobrevivientes")
    print("3. Gráfica de barra de sobrevivientes por clase")
    print("4. Información de tickets(maximo y minimo)")
    print("5. Salir del menú")

    opcion = input("Ingrese su opción: ") #Capturamos Opción

    if opcion == "1":
        print("Ingrese ticket")
        tkt = input()
        filtro_tkt = titanic_df[titanic_df['Ticket'] == tkt]
        print('\nResult search df :\n',filtro_tkt, " \n")

        input()

    if opcion == "2":
        print("Gráfica de pastel de muertos y sobrevivientes")
        #Generamos un nuevo dataset con el recuento de sobrevivientes
        survivor_counts = titanic_df.groupby('Sobrevivió')['Sobrevivió'].count()
        #Agregamos los valores de sobrevientes a un array de numpy
        y = np.array([ survivor_counts[0], survivor_counts[1]])
        mylabels = ["No sobrevivio", "Sobrevivio"]
        #Graficamos 
        plt.pie(y, labels = mylabels, shadow = True,
        autopct='%1.1f%%', startangle=90, colors =["#8c564b","#9467bd"])
        plt.legend(title = "Cantidad de sobrevivientes \n"+"del titanic:")
        plt.title('Gráfica de pastel de muertos y sobrevivientes',fontsize=20)
        plt.show()

        input()


    if opcion == "3":
        print("Gráfica de barra de sobrevivientes por clase")
        #Generamos un nuevo dataset con el recuento de sobrevivientes por clase
        survivor__class_counts = titanic_df.groupby('Clase')['Sobrevivió'].sum()
        #Generamos x con los labels, y con los valores
        x = np.array(["Clase 1", "Clase 2", "Clase 3"])
        y = np.array([survivor__class_counts[1],survivor__class_counts[2],survivor__class_counts[3]])
        
        #Graficamos 
        plt.bar(x,y, color=['blue','cyan', 'red'])
        plt.xlabel('Clase', fontsize=16)
        plt.ylabel('Cantidad de sobrevivientes', fontsize=16)
        
        plt.title('Gráfica de barra de sobrevivientes por clase',fontsize=20)
        #metodo para setear a mano las legends del grafico de barras
        import matplotlib.patches as mpatches
        c1 = mpatches.Patch(color='blue', label='c1')
        c2 = mpatches.Patch(color='cyan', label='c2')
        c3 = mpatches.Patch(color='red', label='c3')
        plt.legend(handles=[c1, c2,c3])
        
        plt.show()

        input()

    if opcion == "4":
        print("Información de tickets(maximo y minimo)")
        #sacamos min y max
        tarifas =  titanic_df['Tarifa'].replace(0, np.NaN)
        tarifas_fx = tarifas[titanic_df['Tarifa'].notnull()]

        max = tarifas_fx.max()
        min = tarifas_fx.min()

        # Echemos un vistazo a los valores
        print("Ticket mas caro: ",max, " \n")
        print("Ticket mas barato: ",min, " \n")
        input()

    elif opcion == "5":
        print("Saliendo del Sistema")
        input()
        break  #saliendo del ciclo repetitivo

    else:
        print("Opción incorrecta")
        
        continue     #Continuando el ciclo repetitivo
