import pymongo


uri = "mongodb+srv://cluster0.i2gon.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='Tarea/X509-cert-7111748312794612461.pem')

db = client.Evaluacion01
#Usuario con privilegios de lectura y escritura
#Este páso es importante desde Atlas para poder usar comandos de Manipulación de la información 
#mydb = client["Evaluacion01"]
#mycol = mydb["CE"]
#for x in mycol.find():
 #print(x)


 