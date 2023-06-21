import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OVER=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+""



#Coleccion?
MONGO_BD="Escuela"
MONGO_COLLECTION="alumnos"

data={
    "nombre":"hola",
    "Edad":20,
}

try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMs=MONGO_TIME_OVER)
    bd=cliente[MONGO_BD]
    collection=bd[MONGO_COLLECTION]
    collection.insert_one(data)
    #cliente.server_info()
    for s in collection.find():
        print(s)



    print("Exitoso")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Time extend: "+ errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Time extend: "+ errorConexion)