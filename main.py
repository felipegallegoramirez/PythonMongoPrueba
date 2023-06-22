import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OVER=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+""



#Coleccion?
MONGO_BD="Escuela"
MONGO_COLLECTION="alumnos"
def add():
    print("Agregando")
    name = input("Digite el nombre: ")
    old = int(input("Digite La edad: "))
    data={
    "nombre":name,
    "Edad":old,
    }
    collection.insert_one(data)

def show():
    print("usuarios: ")
    for s in collection.find():
        print(s)

def showOne():
    print("Un usuario: ")
    a= input("Digite el nombre: ")
    s=collection.find_one({"nombre":a})
    print(s)

def edit():
    print("Un usuario: ")
    namee = input("Nombre a editar: ")
    name = input("Digite el nombre: ")
    old = int(input("Digite La edad: "))
    data={
    "nombre":name,
    "Edad":old,
    }
    s=collection.find_one_and_replace({"nombre":namee},data)
    print(s)

def delete():
    print("Un usuario: ")
    a= input("Digite el nombre: ")
    s=collection.find_one_and_delete({"nombre":a})
    print(s)


try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMs=MONGO_TIME_OVER)
    bd=cliente[MONGO_BD]
    collection=bd[MONGO_COLLECTION]
    op=0
    while(op!=6):
        op = int(input("1. Agregar \n2. Mostrar \n3. Mostrar Uno \n4. Editar \n5. Eliminar \n6. Salir\n"))
        switch={
            1:add,
            2:show,
            3:showOne,
            4:edit,
            5:delete,
        }
        switch.get(op)()

    #cliente.server_info()




    print("Exitoso")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Time extend: "+ errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Time extend: "+ errorConexion)

