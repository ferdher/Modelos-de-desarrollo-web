from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    Name:str
    Sex:str 
    Age:str
    
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=1, 	    Name="Braund, Mr. Owen Harris",  	                            Sex="male",  	Age="22",  	),
             User(	PassengerID=2, 	    Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)",  	Sex="female",  	Age="38",  	),
             User(	PassengerID=3, 	    Name="Heikkinen, Miss. Laina",  	                            Sex="female",  	Age="26",  	),
             User(	PassengerID=4, 	    Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)",  	        Sex="female",  	Age="35",  	),
             User(	PassengerID=5, 	    Name="Allen, Mr. William Henry",  	                            Sex="male",  	Age="35",  	),
             User(	PassengerID=6, 	    Name="Moran, Mr. James",                                    	Sex="male",  	Age="",  	),
             User(	PassengerID=7, 	    Name="McCarthy, Mr. Timothy J",  	                            Sex="male",  	Age="54",  	),
             User(	PassengerID=8, 	    Name="Palsson, Master. Gosta Leonard",  	                    Sex="male",  	Age="2",  	),
             User(	PassengerID=9, 	    Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",   	Sex="female",  	Age="27",  	),
             User(	PassengerID=10,     Name="Nasser, Mrs. Nicholas (Adele Achem)",                 	Sex="female",  	Age="14",  	),
             User(	PassengerID=11,     Name="Sandstrom, Miss. Marguerite Rut",  	                    Sex="female",  	Age="4",  	),
             User(	PassengerID=12,     Name="Bonnell, Miss. Elizabeth",                            	Sex="female",  	Age="58",  	),
             User(	PassengerID=13,     Name="Saundercock, Mr. William Henry",  	                    Sex="male",  	Age="20",  	),
             User(	PassengerID=14,     Name="Andersson, Mr. Anders Johan",  	                        Sex="male",  	Age="39",  	),
             User(	PassengerID=15,     Name="Vestrom, Miss. Hulda Amanda Adolfina",                	Sex="female",  	Age="14",  	),
             User(	PassengerID=16,     Name="Hewlett, Mrs. (Mary D Kingcome)",                     	Sex="female",  	Age="55",  	),
             User(	PassengerID=17,     Name="Rice, Master. Eugene",                                	Sex="male",  	Age="2",  	),
             User(	PassengerID=18,     Name="Williams, Mr. Charles Eugene",  	                        Sex="male",  	Age="",  	),
             User(	PassengerID=19,     Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Sex="female",  	Age="31",  	),
             User(	PassengerID=20,     Name="Masselmani, Mrs. Fatima",                             	Sex="female",  	Age="",  	),
             User(	PassengerID=21,     Name="Fynney, Mr. Joseph J",                                	Sex="male",  	Age="35",  	),
             User(	PassengerID=22,     Name="Beesley, Mr. Lawrence",                               	Sex="male",  	Age="34",  	),
             User(	PassengerID=23,     Name="McGowan, Miss. Anna 'Annie'",  	                        Sex="female",  	Age="15",  	),
             User(	PassengerID=24,     Name="Sloper, Mr. William Thompson",  	                        Sex="male",  	Age="28",  	),
             User(	PassengerID=25,     Name="Palsson, Miss. Torborg Danira",                       	Sex="female",  	Age="8",  	)]



@router.get("/rou4/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou4/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou4/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou4/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou4/{id}", status_code= status.HTTP_200_OK)
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