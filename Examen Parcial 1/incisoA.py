from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class CountryTable(BaseModel):
    Id:int
    Continent:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
continent_list= [CountryTable(Id=1, Continent="Africa"  	    ),
                 CountryTable(Id=2, Continent="Antarctica"	    ),
                 CountryTable(Id=3, Continent="Asia"	        ),
                 CountryTable(Id=4, Continent="Europe"	        ),
                 CountryTable(Id=5, Continent="North America"	),
                 CountryTable(Id=6, Continent="Oceania"	        ),
                 CountryTable(Id=7, Continent="South America"	)]



@router.get("/continent/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (continent_list)
   
#***Get con Filtro Path
@router.get("/continent/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, continent_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Continente no encontrado")


@router.post("/continent/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El continente ya existe")
    else:
        continent_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/continent/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           continent_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe el continente que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/continent/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del continent_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="El continente se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar el continente")
    
    #http://127.0.0.1:8000/usersclass/1