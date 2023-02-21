from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class CountryTable(BaseModel):
    Id:int
    Continent:str
    Region:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
africa_list=    [CountryTable(Id=1 ,Continent="Africa"  	     ,   Region="Central Africa"),
                 CountryTable(Id=2, Continent="Africa"  	     ,       Region="Eastern Africa"),
                 CountryTable(Id=3 ,Continent="Africa"  	     ,   Region="Northern Africa"),
                 CountryTable(Id=4 ,Continent="Africa"  	     ,   Region="Southern Africa"),
                 CountryTable(Id=5 ,Continent="Africa"  	     ,   Region="Western Africa")]
    
antarctica_list=[CountryTable(Id=1 ,Continent="Antarctica"	     ,   Region="Antarctica")]

asia_list=      [CountryTable(Id=1 ,Continent="Asia"	         ,   Region="Eastern Asia"),
                 CountryTable(Id=2 ,Continent="Asia"	         ,   Region="Middle Asia"),
                 CountryTable(Id=3 ,Continent="Asia"	         ,   Region="Southeast Asia"),
                 CountryTable(Id=4 ,Continent="Asia"	         ,   Region="Southern and Central Asia")]

europe_list=    [CountryTable(Id=1 ,Continent="Europe"	         ,   Region="Baltic Countries"),
                 CountryTable(Id=2 ,Continent="Europe"	         ,   Region="British Islands"),
                 CountryTable(Id=3 ,Continent="Europe"	         ,   Region="Eastern Europe"),
                 CountryTable(Id=4 ,Continent="Europe"	         ,   Region="Nordic Countries"),
                 CountryTable(Id=5 ,Continent="Europe"	         ,   Region="Southern Europe"),
                 CountryTable(Id=6 ,Continent="Europe"	         ,   Region="Western Europe")]

northAmerica_list=[CountryTable(Id=1 ,Continent="North America"	 ,   Region="Caribbean"),
                 CountryTable(Id=2 ,Continent="North America"	 ,   Region="Central America"),
                 CountryTable(Id=3 ,Continent="North America"	 ,   Region="North America")]

oceania_list=   [CountryTable(Id=1 ,Continent="Oceania"	         ,   Region="Australia and New Zealand"),
                 CountryTable(Id=2 ,Continent="Oceania"	         ,   Region="Melanesia"),
                 CountryTable(Id=3 ,Continent="Oceania"	         ,   Region="Micronesia"),
                 CountryTable(Id=4 ,Continent="Oceania"	         ,   Region="Micronesia/Caribbean"),
                 CountryTable(Id=5 ,Continent="Oceania"	         ,   Region="Polynesia")]

southAmerica_list=[CountryTable(Id=1 ,Continent="South America"	 ,   Region="South America")]


###################################################         Africa             ###########################################################################
@router.get("/Africa/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (africa_list)
  
#***Get con Filtro Path
@router.get("/Africa/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, africa_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/Africa/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(africa_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        africa_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/Africa/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(africa_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           africa_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/Africa/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(africa_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del africa_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    
############################################################            Antarctica              #####################################################################



@router.get("/Antarctic/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (antarctica_list)
  
#***Get con Filtro Path
@router.get("/Antarctic/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, antarctica_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/Antarctic/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(antarctica_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        antarctica_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/Antarctic/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(antarctica_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           antarctica_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/Antarctic/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(antarctica_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del antarctica_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    


##############################################          Asia            ##############################################################
@router.get("/Asia/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (asia_list)
  
#***Get con Filtro Path
@router.get("/Asia/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, asia_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/Asia/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(asia_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        asia_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/Asia/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(asia_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           asia_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/Asia/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(asia_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del asia_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    





########################################################            Europa          #####################################################################################



@router.get("/Europe/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (europe_list)
  
#***Get con Filtro Path
@router.get("/Europe/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, europe_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/Europe/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(europe_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        europe_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/Europe/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(europe_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           europe_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/Europe/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(europe_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del europe_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    




########################################################            norte america           ############################################

@router.get("/NorthAmerica/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (northAmerica_list)
  
#***Get con Filtro Path
@router.get("/NorthAmerica/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, northAmerica_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/NorthAmerica/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(northAmerica_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        northAmerica_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/NorthAmerica/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(northAmerica_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           northAmerica_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/NorthAmerica/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(northAmerica_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del northAmerica_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    


#######################################         oceania         ###########################################################################

@router.get("/Oceania/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (oceania_list)
  
#***Get con Filtro Path
@router.get("/Africa/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, oceania_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/Oceania/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        oceania_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/Oceania/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           oceania_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/Oceania/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del oceania_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    

###########################################3            sudamerica          ################################################################


@router.get("/SouthAmerica/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (southAmerica_list)
  
#***Get con Filtro Path
@router.get("/SouthAmerica/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, oceania_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region continental no encontrada")


@router.post("/SouthAmerica/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        oceania_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/SouthAmerica/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           oceania_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/SouthAmerica/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(oceania_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del oceania_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    
