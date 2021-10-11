#Tarea base de datos para Centros Escolares
#Raul Fernando Martinez Jovel
#Evaluación 01

import conexion as net
import os
import pandas as pd

db = net.client.test

mydb = net.client["Evaluacion01"]
mycol = mydb["CE"]
#conectamos con la base de datos y con la colecciones

#input() lo utilizamos para hacer pausas y avanzar cuando se presione el teclado
while True: #Generamos el Ciclo repetitivo para el menu
    
    os.system("clear") #Limpieza de pantalla
    print("Menu:")
    print("1. Añadir un registro")
    print("2. Ver los registros")
    print("3. Actualizar un registro")
    print("4. Eliminar un registro")
    print("5. Agregar registros CE")
    print("6. Borrar coleccion CE")
    print("7. Salir") 
    opcion = input("Ingrese su opción: ") #Capturamos Opción
    
    if opcion == "1":
        print("Añadir un registro")
        ID = input("Digite el ID del Centro Escolar: ")
        Nombre = input("Digite el nombre del Centro Escolar: ")
        Departamento = input("Digite el departamento del Centro Escolar: ")
        Municipio = input("Digite el municipio del Centro Escolar: ")

        mydict = { "ID": ID, "Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio} #Creamos diccionario
        x = mycol.insert_one(mydict) #Lo ingresamos a la base
        input()

    elif opcion == "2":
        print("Ver los registros")
        #Opcion para imprimir dataframe y obs primeros y ultimos registros
        data = pd.DataFrame(list(mycol.find()))
        print(data)

        """ Opcion para imprimir todos los registriso
        for x in mycol.find(): #Ciclo repetitivo para imprimir todos los registros
            print(x)    
        
        """
        input()
        

    elif opcion == "3":
        print("Actualizar un registro")
        idm = input("Ingresar _id a modificar: ")
        from bson.objectid import ObjectId
        filter = {"_id":ObjectId(idm)} 
        mydoc = list(mycol.find(filter))
        print(mydoc)
        
        if mydoc.count == "0":
            
            print("no docs found with _id: ", ID)
            input()
        else:
            ID = input("Digite el nuevo ID del Centro Escolar: ")
            Nombre = input("Digite el nuevo nombre del Centro Escolar: ")
            Departamento = input("Digite el nuevo departamento del Centro Escolar: ")
            Municipio = input("Digite el nuevo municipio del Centro Escolar: ")    
            filter = {"_id": ObjectId(idm) }
            myquery = { "$set": { "ID": ID, "Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio} } #Creamos diccionario 
            x = mycol.update_one(filter,myquery)    
            input()
        
    elif opcion == "4":
        print("Eliminar un registro")
        from bson.objectid import ObjectId
        ID = input("Ingresar ID ")
        myquery = {"_id":ObjectId(ID)}  
        x = mycol.delete_one(myquery)
        print("Registro eliminado: ", mycol.results.DeletedResut)
        input()
    
    elif opcion == "5":
        if mycol.count_documents({}) == 0:
            print("Agregando registros de clase CE.csv")
            #Agregamos data de CE de el salvador
            print("Se ingresan los registros del archivo CE de clases")
            df = pd.read_csv("/Users/raulmartinez/Documents/Python - Data Science/Tarea/cesv.csv")
            data_dict = df.to_dict("records")
            mycol.insert_many(data_dict)
        else:
            ans = input("CE ya existe quieres agregar el dataset igual? (1 si 0 no) ")
            if ans == "1":
                print("Agregando registros de clase CE.csv")
                #Agregamos data de CE de el salvador
                print("Se ingresan los registros del archivo CE de clases")
                df = pd.read_csv("/Users/raulmartinez/Documents/Python - Data Science/Tarea/cesv.csv")
                data_dict = df.to_dict("records")
                mycol.insert_many(data_dict)

            elif ans == "0":
                print("No se agregaron nuevos registros")
                
            else:
                print("Opción incorrecta")
                continue    
                
            
        input()

    elif opcion == "6":
        print("Borrarrando CE con todos sus registros")
        mycol.drop()
        input()

    elif opcion == "7":
        print("Saliendo del Sistema")
        input()
        break  #saliendo del ciclo repetitivo

    else:
        print("Opción incorrecta")
        input()
        continue     #Continuando el ciclo repetitivo


