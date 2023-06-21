import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OVER=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMs=MONGO_TIME_OVER)
    cliente.server_info()
    print("Exitoso")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Time extend: "+ errorTiempo)
except pymongo.errors.ConectionFailure as errorConexion:
    print("Time extend: "+ errorConexion)