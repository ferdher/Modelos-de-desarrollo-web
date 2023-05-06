#Acciones
#1 cambiamos path de "usersclass" a "userdb"
#Movemos basemodel
#vaciamos user list

#-uvicorn main:app --reload-

#Path:  http://127.0.0.1:8000/userdb

#POST-body-JSON
#{"username":"Alfredo", "email":"alfredo.garcia@buap.mx"}

#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Invocamos la entidad que hemos creado ****nEw
from db.models.user import User
#Importamos la instancia que devolvera al usuario en formato user ***new
from db.schemas.user import user_schema
#Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from db.Client_9 import db_client



#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn 4_codigos_HTTP:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user




#***Get
@router.get("/userdb/get/{username}", status_code=201)
async def usersclass(username:str):
    
     #2Transformo mi entidad user en un diccionario. Transformo User en diccionario
   # user_dict= dict (username)
    #Elimino id del diccionario
   # del user_dict["id"]
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección
    if db_client.ModelosWeb.ModelosJWT.find_one({"username":username}):
        id= user_schema(db_client.ModelosWeb.ModelosJWT.find_one({"username":username}))
        return User(**id)
    else:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")
    
    #Consultamos el user insertado en la bd con todo y id asignado automaticamente
    #Me devuelve un JSON hay que convertirlo a un objeto tipo User (user.py en schemas)
   
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    
    

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/

 
#***Post
@router.post("/userdb/post",response_model=User, status_code=201)
async def usersclass(user:User):
    
    #found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    #for index, saved_user in enumerate(users_list):
    #    if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
    #       raise HTTPException(status_code=204,detail="el usuario ya existe")
    #else:
    
    #2Transformo mi entidad user en un diccionario. Transformo User en diccionario
    user_dict= dict (user)
    #Elimino id del diccionario
    del user_dict["id"]
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección
    id= db_client.ModelosWeb.ModelosJWT.insert_one(user_dict).inserted_id
    
    #Consultamos el user insertado en la bd con todo y id asignado automaticamente
    #Me devuelve un JSON hay que convertirlo a un objeto tipo User (user.py en schemas)
    new_user=  user_schema(db_client.ModelosWeb.ModelosJWT.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return User(**new_user)
    

    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@router.put("/userdb/put/",response_model=User, status_code=201)
async def usersclass(user:User):

    filtro= {'username':user.username}

            ###full_name
    newvalue= {"$set":{'full_name':user.full_name}}
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección
    db_client.ModelosWeb.ModelosJWT.update_one(filtro, newvalue)
            ###email
    newvalue= {"$set":{'email':user.email}}
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección
    db_client.ModelosWeb.ModelosJWT.update_one(filtro, newvalue)


    id = user_schema(db_client.ModelosWeb.ModelosJWT.find_one({"username":user.username}))
    
    return (id)
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/userdb/delete/{username}", status_code=201)
async def usersclass(username:str):
    
        if db_client.ModelosWeb.ModelosJWT.delete_many({"username":username}):
             db_client.ModelosWeb.ModelosJWT.delete_many({"username":username})
             
             return ("Usuario Eliminado")
        else:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="El usuario no se pudo eliminar")
    
    
    #http://127.0.0.1:8000/usersclass/1