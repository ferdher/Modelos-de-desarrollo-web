from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
 
router = APIRouter()
class CountryTable(BaseModel):
    Id:int
    Region:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
region_list= [   CountryTable(	Id=1,	    Region="Antarctica"	                ),
                 CountryTable(	Id=2,	    Region="Australia and New Zealand"	),
                 CountryTable(	Id=3,	    Region="Baltic Countries"	        ),
                 CountryTable(	Id=4,	    Region="British Islands"	        ),
                 CountryTable(	Id=5,	    Region="Caribbean"	                ),
                 CountryTable(	Id=6,	    Region="Central Africa"	            ),
                 CountryTable(	Id=7,	    Region="Central America"	        ),
                 CountryTable(	Id=8,	    Region="Eastern Africa"	            ),
                 CountryTable(	Id=9,	    Region="Eastern Asia"	            ),
                 CountryTable(	Id=10,	    Region="Eastern Europe"	            ),
                 CountryTable(	Id=11,	    Region="Melanesia"	                ),
                 CountryTable(	Id=12,	    Region="Micronesia"	                ),
                 CountryTable(	Id=13,	    Region="Micronesia/Caribbean"	    ),
                 CountryTable(	Id=14,	    Region="Middle East"	            ),
                 CountryTable(	Id=15,	    Region="Nordic Countries"	        ),
                 CountryTable(	Id=16,	    Region="North America"	            ),
                 CountryTable(	Id=17,	    Region="Northern Africa"	        ),
                 CountryTable(	Id=18,	    Region="Polynesia"	                ),
                 CountryTable(	Id=19,	    Region="South America"	            ),
                 CountryTable(	Id=20,	    Region="Southeast Asia"	            ),
                 CountryTable(	Id=21,	    Region="Southern Africa"	        ),
                 CountryTable(	Id=22,	    Region="Southern and Central Asia"	),
                 CountryTable(	Id=23,	    Region="Southern Europe"	        ),
                 CountryTable(	Id=24,	    Region="Western Africa"	            ),
                 CountryTable(	Id=25,	    Region="Western Europe"	            )]






@router.get("/continent/region/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (region_list)
   
#***Get con Filtro Path
@router.get("/continent/region/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, region_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region no encontrada")


@router.post("/continent/region/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        region_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/continent/region/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           region_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/continent/region/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del region_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    
    #http://127.0.0.1:8000/usersclass/1