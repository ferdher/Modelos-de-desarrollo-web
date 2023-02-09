from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    Survived:int
    Pclass:int
    Name:str
    Sex:str 
    Age:str
    SibSp:int 
    Parch:int 
    Ticket:str
    Fare:str
    Cabin:str
    Embarked:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=19, 	Survived=0, 	Pclass=3, 	Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Sex="female",  	Age="31",  	SibSp=1, 	Parch=0, 	Ticket="345763",  	        Fare="18",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=20, 	Survived=1, 	Pclass=3, 	Name="Masselmani, Mrs. Fatima",                             	Sex="female",  	Age="",  	SibSp=0, 	Parch=0, 	Ticket="2649",  	        Fare="7.225",  	    Cabin="",  	    Embarked="C"),
             User(	PassengerID=21, 	Survived=0, 	Pclass=2, 	Name="Fynney, Mr. Joseph J",                                	Sex="male",  	Age="35",  	SibSp=0, 	Parch=0, 	Ticket="239865",  	        Fare="26",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=22, 	Survived=1, 	Pclass=2, 	Name="Beesley, Mr. Lawrence",                               	Sex="male",  	Age="34",  	SibSp=0, 	Parch=0, 	Ticket="248698",  	        Fare="13",  	    Cabin="D56",  	Embarked="S"),
             User(	PassengerID=23, 	Survived=1, 	Pclass=3, 	Name="McGowan, Miss. Anna 'Annie'",  	                        Sex="female",  	Age="15",  	SibSp=0, 	Parch=0, 	Ticket="330923",  	        Fare="8.0292",     	Cabin="",  	    Embarked="Q"),
             User(	PassengerID=24, 	Survived=1, 	Pclass=1, 	Name="Sloper, Mr. William Thompson",  	                        Sex="male",  	Age="28",  	SibSp=0, 	Parch=0, 	Ticket="113788",  	        Fare="35.5",  	    Cabin="A6",  	Embarked="S"),
             User(	PassengerID=25, 	Survived=0, 	Pclass=3, 	Name="Palsson, Miss. Torborg Danira",                       	Sex="female",  	Age="8",  	SibSp=3, 	Parch=1, 	Ticket="349909",  	        Fare="21.075",  	Cabin="",  	    Embarked="S")]



@router.get("/rou7/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou7/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou7/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou7/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou7/{id}", status_code= status.HTTP_200_OK)
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