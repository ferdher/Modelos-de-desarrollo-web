from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    PassengerID:int
    Nombre:str
    Tipo:str
    Costo:float
    Imagen:str
    
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(	PassengerID=1,	 Nombre="Reloj para caballero Skechers Ruhland SR1019 negro",	                Tipo="reloj",	Costo=509.15,	Imagen="http://serviciosdigitalesplus.com/fotos/1047840356.jpg"),
             User(	PassengerID=2,	 Nombre="Reloj para caballero Citizen Super Titanium/Ti+Ip 60917 acero",	    Tipo="reloj",	Costo=6868,	    Imagen="https://ss376.liverpool.com.mx/lg/1057083111.jpg"),
             User(	PassengerID=3,	 Nombre="Reloj para caballero Tommy Hilfiger Mens Diver azul marino",	        Tipo="reloj",	Costo=1869.15,	Imagen="https://ss376.liverpool.com.mx/lg/1080772889.jpg"),
             User(	PassengerID=4,	 Nombre="Reloj para caballero Alexandre Christie Sport 6492mcbssbarg-set",	    Tipo="reloj",	Costo=5091.5,	Imagen="https://ss376.liverpool.com.mx/lg/1078552359.jpg"),
             User(	PassengerID=5,	 Nombre="Reloj para caballero Hamilton Khaki Aviation X-Wind H77912335 negro",	Tipo="reloj",	Costo=16991.5,	Imagen="https://ss375.liverpool.com.mx/lg/1048534747.jpg"),
             User(	PassengerID=6,	 Nombre="Reloj para caballero G By Guess Mens Gold Intent G99071G1",	        Tipo="reloj",	Costo=2379.15,	Imagen="https://ss376.liverpool.com.mx/lg/1064191043.jpg"),
             User(	PassengerID=7,	 Nombre="Luminox Land A.1105 Reloj Fino para Caballero Color Negro",	        Tipo="reloj",	Costo=11118,	Imagen="https://ss375.liverpool.com.mx/lg/1030301419.jpg"),
             User(	PassengerID=8,	 Nombre="Reloj para caballero Alexandre Christie Sport 6484MCLSSBA",	        Tipo="reloj",	Costo=4666.5,	Imagen="https://ss376.liverpool.com.mx/lg/1079985879.jpg"),
             User(	PassengerID=9,	 Nombre="Reloj unisex Calvin Klein Minimal K3M2T621",	                        Tipo="reloj",	Costo=4990,	    Imagen="https://ss376.liverpool.com.mx/lg/1066633124.jpg"),
             User(	PassengerID=10,	 Nombre="Reloj para caballero Alexandre Christie Elegant 8562MDBSSSL",	        Tipo="reloj",	Costo=3646.5,	Imagen="https://ss376.liverpool.com.mx/lg/1073101308.jpg"),
             User(	PassengerID=11,	 Nombre="Reloj para caballero Citizen CTO 60979 azul rey",	                    Tipo="reloj",	Costo=4271.2,	Imagen="https://ss376.liverpool.com.mx/lg/1061943176.jpg"),
             User(	PassengerID=12,	 Nombre="Reloj para caballero Bomberg Bolt 68 BS4SKP5",	                        Tipo="reloj",	Costo=24900,	Imagen="https://ss375.liverpool.com.mx/lg/1072552128.jpg"),
             User(	PassengerID=13,	 Nombre="Reloj para caballero Tommy Hilfiger TH.171.036.0 café obscuro",	    Tipo="reloj",	Costo=2845.5,	Imagen="https://ss376.liverpool.com.mx/lg/1063732636.jpg"),
             User(	PassengerID=14,	 Nombre="Diesel Mega Chief DZ4338 Reloj para Caballero Color Negro",	        Tipo="reloj",	Costo=5133.15,	Imagen="https://ss376.liverpool.com.mx/lg/1032365058.jpg"),
             User(	PassengerID=15,	 Nombre="Reloj para caballero Casio G-Shock GA-710-1A2CR negro",	            Tipo="reloj",	Costo=2659.65,	Imagen="https://ss376.liverpool.com.mx/lg/1057700986.jpg"),
             User(	PassengerID=16,	 Nombre="Skechers Color Bezel Ana-Di SR1073 Reloj para Caballero Color Negro",	Tipo="reloj",	Costo=679.15,	Imagen="https://ss376.liverpool.com.mx/lg/1051169928.jpg"),
             User(	PassengerID=17,	 Nombre="Reloj para caballero Bulova Champlain Deportivo 98b332",	            Tipo="reloj",	Costo=14025,	Imagen="https://ss376.liverpool.com.mx/lg/1078192514.jpg"),
             User(	PassengerID=18,	 Nombre="Reloj para caballero Guess Escrow W0990G1",	                        Tipo="reloj",	Costo=3144.15,	Imagen="https://ss376.liverpool.com.mx/lg/1058763493.jpg"),
             User(	PassengerID=19,	 Nombre="Reloj para caballero Oris Prodiver 77477277154-SET",	                Tipo="reloj",	Costo=85500,	Imagen="https://ss375.liverpool.com.mx/lg/7562256.jpg"),
             User(	PassengerID=20,	 Nombre="Reloj para caballero Alexandre Christie Elegant 8572MSLRGSL café",	    Tipo="reloj",	Costo=2796.5,	Imagen="https://ss376.liverpool.com.mx/lg/1078658858.jpg")]



@router.get("/rou1/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (users_list)
   
#***Get con Filtro Path
@router.get("/rou1/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.PassengerID == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")


@router.post("/rou1/",  response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/rou1/", status_code= status.HTTP_202_ACCEPTED)
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
@router.delete("/rou1/{id}", status_code= status.HTTP_200_OK)
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