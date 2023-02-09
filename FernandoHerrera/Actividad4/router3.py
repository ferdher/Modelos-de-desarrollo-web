from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    Nombre:str
    Apellido:str
    Edad:int
    Correo:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=1,	Nombre="MIGUEL ANGEL",	    Apellido="GOMEZ",	    Edad=25,	Correo="miguel.angel.gomez.garcia@gmail.com"    	),
             User(	PassengerID=2,	Nombre="JOSE FRANCISCO",	Apellido="CURIEL",	    Edad=27,	Correo="jose.francisco.curiel.franco@gmail.com"	    ),
             User(	PassengerID=3,	Nombre="JESUS ANTONIO",	    Apellido="VERDUZCO",	Edad=26,	Correo="jesus.antonio.verduzco.saldaña@gmail.com"	),
             User(	PassengerID=4,	Nombre="ALEJANDRA",	        Apellido="VARELA",	    Edad=29,	Correo="alejandra.varela.gutierrez@gmail.com"	    ),
             User(	PassengerID=5,	Nombre="RICARDO",	        Apellido="ROSAS",	    Edad=25,	Correo="ricardo.rosas.melendez@gmail.com"	        ),
             User(	PassengerID=6,	Nombre="DANIEL",	        Apellido="VALDeS",	    Edad=28,	Correo="daniel.valdes.villa@gmail.com"	            ),
             User(	PassengerID=7,	Nombre="JORGE", 	        Apellido="VANEGAS",	    Edad=26,	Correo="jorge.vanegas.acevedo@gmail.com"	        ),
             User(	PassengerID=8,	Nombre="CAMILA",	        Apellido="VIVEROS",	    Edad=29,	Correo="camila.viveros.fauser@gmail.com"	        ),
             User(	PassengerID=9,	Nombre="JAVIER",	        Apellido="ARANDA",	    Edad=25,	Correo="javier.aranda.barajas@gmail.com"	        ),
             User(	PassengerID=10,	Nombre="RAUL",	            Apellido="ESPINOSA",	Edad=28,	Correo="raul.espinosa.cisneros@gmail.com"	        )]



@router.get("/rou3/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou3/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou3/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou3/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID   == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha actualizado el usuario")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/rou3/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="El registro se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha eliminado el usuario")
    
    #http://127.0.0.1:8000/usersclass/1