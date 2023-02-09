from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    Sex:str 
    Age:str
    Ticket:str
    Cabin:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=1, 	    Sex="male",  	Age="22",  	Ticket="A/5 21171",  	        Cabin="",  	    ),
             User(	PassengerID=2, 	    Sex="female",  	Age="38",  	Ticket="PC 17599",  	       	Cabin="C85",  	),
             User(	PassengerID=3, 	    Sex="female",  	Age="26",  	Ticket="STON/O2. 3101282",   	Cabin="",  	    ),
             User(	PassengerID=4, 	    Sex="female",  	Age="35",  	Ticket="113803",  	            Cabin="C123",  	),
             User(	PassengerID=5, 	    Sex="male",  	Age="35",  	Ticket="373450",  	            Cabin="",  	    ),
             User(	PassengerID=6, 	    Sex="male",  	Age="",  	Ticket="330877",  	          	Cabin="",  	    ),
             User(	PassengerID=7, 	    Sex="male",  	Age="54",  	Ticket="17463",  	           	Cabin="E46",  	),
             User(	PassengerID=8, 	    Sex="male",  	Age="2",  	Ticket="349909",  	          	Cabin="",  	    ),
             User(	PassengerID=9, 	    Sex="female",  	Age="27",  	Ticket="347742",  	           	Cabin="",  	    ),
             User(	PassengerID=10, 	Sex="female",  	Age="14",  	Ticket="237736",  	           	Cabin="",  	    ),
             User(	PassengerID=11, 	Sex="female",  	Age="4",  	Ticket="PP 9549",  	            Cabin="G6",  	),
             User(	PassengerID=12, 	Sex="female",  	Age="58",  	Ticket="113783",  	         	Cabin="C103",  	),
             User(	PassengerID=13, 	Sex="male",  	Age="20",  	Ticket="A/5. 2151",  	        Cabin="",  	    ),
             User(	PassengerID=14,     Sex="male",  	Age="39",  	Ticket="347082",  	         	Cabin="",  	    ),
             User(	PassengerID=15, 	Sex="female",  	Age="14",  	Ticket="350406",  	         	Cabin="",  	    ),
             User(	PassengerID=16, 	Sex="female",  	Age="55",  	Ticket="248706",  	            Cabin="",  	    ),
             User(	PassengerID=17, 	Sex="male",  	Age="2",  	Ticket="382652",  	           	Cabin="",  	    ),
             User(	PassengerID=18, 	Sex="male",  	Age="",  	Ticket="244373",  	            Cabin="",  	    ),
             User(	PassengerID=19, 	Sex="female",  	Age="31",  	Ticket="345763",  	            Cabin="",  	    ),
             User(	PassengerID=20, 	Sex="female",  	Age="",  	Ticket="2649",  	            Cabin="",  	    ),
             User(	PassengerID=21, 	Sex="male",  	Age="35",  	Ticket="239865",  	            Cabin="",  	    ),
             User(	PassengerID=22, 	Sex="male",  	Age="34",  	Ticket="248698",  	            Cabin="D56",  	),
             User(	PassengerID=23, 	Sex="female",  	Age="15",  	Ticket="330923",  	           	Cabin="",  	    ),
             User(	PassengerID=24, 	Sex="male",  	Age="28",  	Ticket="113788",  	            Cabin="A6",  	),
             User(	PassengerID=25, 	Sex="female",  	Age="8",  	Ticket="349909",  	         	Cabin="",  	    )]



@router.get("/rou5/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou5/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou5/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou5/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou5/{id}", status_code= status.HTTP_200_OK)
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