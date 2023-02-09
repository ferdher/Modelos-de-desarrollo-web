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
users_list= [User(	PassengerID=9, 	    Survived=1, 	Pclass=3, 	Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",   	Sex="female",  	Age="27",  	SibSp=0, 	Parch=2, 	Ticket="347742",  	        Fare="11.1333",   	Cabin="",  	    Embarked="S"),
             User(	PassengerID=10, 	Survived=1, 	Pclass=2, 	Name="Nasser, Mrs. Nicholas (Adele Achem)",                 	Sex="female",  	Age="14",  	SibSp=1, 	Parch=0, 	Ticket="237736",  	        Fare="30.0708",   	Cabin="",  	    Embarked="C"),
             User(	PassengerID=11, 	Survived=1, 	Pclass=3, 	Name="Sandstrom, Miss. Marguerite Rut",  	                    Sex="female",  	Age="4",  	SibSp=1, 	Parch=1, 	Ticket="PP 9549",  	        Fare="16.7",  	    Cabin="G6",  	Embarked="S"),
             User(	PassengerID=12, 	Survived=1, 	Pclass=1, 	Name="Bonnell, Miss. Elizabeth",                            	Sex="female",  	Age="58",  	SibSp=0, 	Parch=0, 	Ticket="113783",  	        Fare="26.55",   	Cabin="C103",  	Embarked="S"),
             User(	PassengerID=13, 	Survived=0, 	Pclass=3, 	Name="Saundercock, Mr. William Henry",  	                    Sex="male",  	Age="20",  	SibSp=0, 	Parch=0, 	Ticket="A/5. 2151",  	    Fare="8.05",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=14, 	Survived=0, 	Pclass=3, 	Name="Andersson, Mr. Anders Johan",  	                        Sex="male",  	Age="39",  	SibSp=1, 	Parch=5, 	Ticket="347082",  	        Fare="31.275",  	Cabin="",  	    Embarked="S"),
             User(	PassengerID=15, 	Survived=0, 	Pclass=3, 	Name="Vestrom, Miss. Hulda Amanda Adolfina",                	Sex="female",  	Age="14",  	SibSp=0, 	Parch=0, 	Ticket="350406",  	        Fare="7.8542",  	Cabin="",  	    Embarked="S"),
             User(	PassengerID=16, 	Survived=1, 	Pclass=2, 	Name="Hewlett, Mrs. (Mary D Kingcome)",                     	Sex="female",  	Age="55",  	SibSp=0, 	Parch=0, 	Ticket="248706",  	        Fare="16",  	    Cabin="",  	    Embarked="S")]



@router.get("/rou8/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou8/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou8/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou8/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou8/{id}", status_code= status.HTTP_200_OK)
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