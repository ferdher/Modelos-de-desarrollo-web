from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    Sex:str 
    Ticket:str
    Embarked:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	      Sex="male",  	    Ticket="A/5 21171",  	        Embarked="S"),
             User(	      Sex="female",    	Ticket="PC 17599",  	     	Embarked="C"),
             User(	      Sex="female",     Ticket="STON/O2. 3101282",      Embarked="S"),
             User(	      Sex="female",     Ticket="113803",  	          	Embarked="S"),
             User(	      Sex="male",  	    Ticket="373450",  	            Embarked="S"),
             User(	      Sex="male",  	    Ticket="330877",  	            Embarked="Q"),
             User(	      Sex="male",  	    Ticket="17463",  	         	Embarked="S"),
             User(	      Sex="male",  	    Ticket="349909",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="347742",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="237736",  	            Embarked="C"),
             User(	      Sex="female",     Ticket="PP 9549",  	        	Embarked="S"),
             User(	      Sex="female",     Ticket="113783",  	        	Embarked="S"),
             User(	      Sex="male",  	    Ticket="A/5. 2151",  	        Embarked="S"),
             User(	      Sex="male",  	    Ticket="347082",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="350406",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="248706",  	            Embarked="S"),
             User(	      Sex="male",  	    Ticket="382652",  	            Embarked="Q"),
             User(        Sex="male",  	    Ticket="244373",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="345763",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="2649",  	            Embarked="C"),
             User(	      Sex="male",  	    Ticket="239865",  	            Embarked="S"),
             User(	      Sex="male",  	    Ticket="248698",  	            Embarked="S"),
             User(	      Sex="female",     Ticket="330923",  	            Embarked="Q"),
             User(	      Sex="male",  	    Ticket="113788",  	        	Embarked="S"),
             User(	      Sex="female",     Ticket="349909",  	            Embarked="S")]



@router.get("/rou6/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou6/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou6/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou6/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou6/{id}", status_code= status.HTTP_200_OK)
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