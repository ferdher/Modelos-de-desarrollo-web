from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    costo:int
    Img2:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=1047840356,	costo=509.15,	Img2="1047840356.jpg",	),
User(	PassengerID=1057083111,	costo=6868,	    Img2="1057083111.jpg"	),
User(	PassengerID=1080772889,	costo=1869.15,	Img2="1080772889.jpg"	),
User(	PassengerID=1078552359,	costo=5091.5,	Img2="1078552359.jpg"	),
User(	PassengerID=1048534747,	costo=16991.5,	Img2="1048534747.jpg"	),
User(	PassengerID=1064191043,	costo=2379.15,	Img2="1064191043.jpg"	),
User(	PassengerID=1030301419,	costo=11118,	Img2="1030301419.jpg"	),
User(	PassengerID=1079985879,	costo=4666.5,	Img2="1079985879.jpg"	),
User(	PassengerID=1066633124,	costo=4990,	    Img2="1066633124.jpg"	),
User(	PassengerID=1073101308,	costo=3646.5,	Img2="1073101308.jpg"	),
User(	PassengerID=1061943176,	costo=4271.2,	Img2="1061943176.jpg"	),
User(	PassengerID=1072552128,	costo=24900,	Img2="1072552128.jpg"	),
User(	PassengerID=1063732636,	costo=2845.5,	Img2="1063732636.jpg"	),
User(	PassengerID=1032365058,	costo=5133.15,	Img2="1032365058.jpg"	),
User(	PassengerID=1057700986,	costo=2659.65,	Img2="1057700986.jpg"	),
User(	PassengerID=1051169928,	costo=679.15,	Img2="1051169928.jpg"	),
User(	PassengerID=1078192514,	costo=14025,	Img2="1078192514.jpg"	),
User(	PassengerID=1058763493,	costo=3144.15,	Img2="1058763493.jpg"	),
User(	PassengerID=1050228092,	costo=85500,	Img2="7562256.jpg"	    ),
User(	PassengerID=1078658858,	costo=2796.5,	Img2="1078658858.jpg"	)]



@router.get("/rou2/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou2/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou2/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou2/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou2/{id}", status_code= status.HTTP_200_OK)
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