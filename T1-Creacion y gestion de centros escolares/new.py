import conexion as net
import numpy as np
import pandas as pd

db = net.client.test

mydb = net.client["Evaluacion01"]
mycol = mydb["CE"]


print(mycol, "\n")

x = mycol.find_one() 
print(x)
print("Primer registro","\n")
#Ver el primer registro que aparezca

"""
for x in mycol.find(): 
  print(x)
#Mostrará todos los documentos del Cluster
"""

mongo_docs = mycol.find()
# create an empty dictionary for the MongoDB documents' fields
CE = {}

# go through list of MongoDB documents
for doc in mongo_docs:

    # iterate key-value pairs of each MongoDB document
    # use iteritems() for Python 2
    for key, val in doc.items():

        # attempt to add field's value to dict
        try:
            # append the MongoDB field value to the NumPy object
            CE[key] = np.append(CE[key], val)
        except KeyError:
            # create a new dict key will new NP array
            CE[key] = np.array([val])

# print out the fields dictionary
print("print dict","\n")

data = pd.DataFrame(list(mycol.find()))
print(data)