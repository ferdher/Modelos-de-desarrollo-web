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
users_list= [User(	PassengerID=1, 	    Survived=0, 	Pclass=3, 	Name="Braund, Mr. Owen Harris",  	                            Sex="male",  	Age="22",  	SibSp=1, 	Parch=0, 	Ticket="A/5 21171",  	    Fare="7.25",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=2, 	    Survived=1, 	Pclass=1, 	Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)",  	Sex="female",  	Age="38",  	SibSp=1, 	Parch=0, 	Ticket="PC 17599",  	    Fare="71.2833",   	Cabin="C85",  	Embarked="C"),
             User(	PassengerID=3, 	    Survived=1, 	Pclass=3, 	Name="Heikkinen, Miss. Laina",  	                            Sex="female",  	Age="26",  	SibSp=0, 	Parch=0, 	Ticket="STON/O2. 3101282",  Fare="7.925",   	Cabin="",  	    Embarked="S"),
             User(	PassengerID=4, 	    Survived=1, 	Pclass=1, 	Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)",  	        Sex="female",  	Age="35",  	SibSp=1, 	Parch=0, 	Ticket="113803",  	        Fare="53.1",  	    Cabin="C123",  	Embarked="S"),
             User(	PassengerID=5, 	    Survived=0, 	Pclass=3, 	Name="Allen, Mr. William Henry",  	                            Sex="male",  	Age="35",  	SibSp=0, 	Parch=0, 	Ticket="373450",  	        Fare="8.05",  	    Cabin="",  	    Embarked="S")]



@router.get("/rou9/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou9/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou9/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou9/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou9/{id}", status_code= status.HTTP_200_OK)
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