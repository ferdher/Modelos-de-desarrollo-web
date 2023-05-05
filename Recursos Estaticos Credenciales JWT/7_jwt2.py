#Instalamos libreria de criptografía para encriptar token
# pip install "python-jose[cryptography]"

#Instalamos libreria que contiene el algoritmo de encriptación
# pip install "passlib[bcrypt]"

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, Depends, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel


from fastapi.responses import FileResponse

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#Importamos librería jwt
from jose import jwt, JWTError
#Importamos libreria passlib (algoritmo de encriptación)
from passlib.context import CryptContext
#Importamos libreria de fechas para la expiración del token
from datetime import datetime, timedelta
#Importamos la clase staticfiles para recursos estáticos****
from fastapi.staticfiles import StaticFiles

#Implementamos algoritmo de haseo para encriptar contraseña
ALGORITHM = "HS256"
#Duración de autenticación 
ACCESS_TOKEN_DURATION= 1
#Creamos un secret
SECRET="123456789"

#Creamos un objeto o instancia a partir de la clase FastAPI
app= FastAPI()


#Creamos una app para acceder al directorio de recursos estaticos***
app.mount("/static", StaticFiles(directory="static"), name="static")

#Autenticación por contraseña para eso:
#Creamos un endpoint llamado "login"
oauth2=OAuth2PasswordBearer(tokenUrl="login")

#Creamos contexto de encriptación para eso importamos libreria passlib y elegimos algoritmo de incriptación "bcrypt"
#Utilizamos bcrypt generator para encriptar nuestras contraseñas
crypt= CryptContext(schemes="bcrypt")

# generamos la contraseña encriptada para guardarla en base de datos
#https://bcrypt-generator.com/4

class User(BaseModel):
    username: str 
    full_name: str 
    email: str 
    disabled:bool 
#Definimos la clase para el usuario de base de datos 
class UserDB(User):
    password:str


users_db ={
    "Freddy":{ 
        "username":"Freddy",
        "full_name":"Freddy Garcia",
        "email":"alfredo.garcia@alumno.buap.mx",
        "disabled" :False,
        "password":"$2a$12$b0XvdTmqRXwmWkDjlThFE./cEr0gKbg8c9blKfS6tJ62MnHGjmMGq"#1234
             },
    "Ferdher":{ ###
        "username":"Ferdher",
        "full_name":"Fernando Herrera",
        "email":"edgar.herrerar@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$13$wuWXYKdV44Dix9XaEsGEIO9vSUQUfW0OYDioZffWUXTUl4WMOs1j6"#52890
    
            },
    "Blas":{  ###
        "username":"Blas",
        "full_name":"BLAS BRAVO DAVID",
        "email":"david.blasb@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$12$1TezNsU2Q3vuZSGSg0N9..BJbM3V9wuZUEhposFV675C3AsvvRhOG"#123456
    
            },
    
    "Javier":{   ###
        "username":"Javier",
        "full_name":"CORDERO TEAPILA ALDO JAVIER",
        "email":"aldo.cordero@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$Mkd3zE87rVQjAAFFXRTSdOC9Weye9/KM57MskF5B/NKCJ4R8jR6eO"#1234567
    
            },

    "Gerardo":{   ###
        "username":"Gerardo",
        "full_name":"CRUZ SOSA LUIS GERARDO",
        "email":"luis.cruzso@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$ZiCIIQDVL/9GUFeOI.FQjOn4K7yEdR6oKG5.HS3n/JiTwzXEjYTYy"#12345678
    
            },
    
    "David":{   
        "username":"David",
        "full_name":"FERNANDEZ PEREZ DAVID",
        "email":"david.fernandezp@alumno.buap.mx",
        "disabled":True,
        "password":"$2a$12$mvOrMjAR2DKM2fdrAgNeF.GU8AUv/iVUbvyep8baGCqZj5rHnGary"#123456789
    
            },

    "Karime":{   ###
        "username":"Karime",
        "full_name":"GOMEZ CHAVEZ KARYME SUSANA",
        "email":"karyme.gomez@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$12$IRCMeeIXDvKhWfhxbuwIcuF//EQGTXqfdzl4FjEqqrjWivOFJT1HO"#101112
    
            },

    "Luis":{   ###
        "username":"Luis",
        "full_name":"GONZALEZ AVENDANO LUIS DAVID",
        "email":"luis.gonzalezav@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$bjlG7/5tdpc8gPcU9kndee4v5M78Mqf9sbny2aCXGE7JPW/BSNpum"#10111213
    
            },

    "Hugo":{   ###
        "username":"Hugo",
        "full_name":"GORGONIO HERNANDEZ HUGO",
        "email":"hugo.gorgonio@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$12$TyVHfte7mtqqlN9OLvvMq.ytVpSTRS5f.M.x0fAXTecjTNqv.DEGu"#1011121314
    
            },

    "Diego":{   ###
        "username":"Diego",
        "full_name":"GUTIERREZ BARRANCO LUIS DIEGO",
        "email":"luis.gutierrezba@alumno.buap.mx",
        "disabled":True,
        "password":"$2a$12$3AnNdJjlS34M8uShDRmoX.sBkGd67RROB8pskDniFCKbnYr2x.CXq"#101112131415
    
            },

    "Manuel":{   ###
        "username":"Manuel",
        "full_name":"GUTIERREZ FLORES VICTOR MANUEL",
        "email":"victor.gutierrezf@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$12$LBOrlFyTzGuLI7PwkbUyv.NAJmG/rxQI3gBNb52nspVlOJ.HSBrWK"#10111213141516
    
            },


    "Armando":{   ###
        "username":"Armando",
        "full_name":"LANDA ARGUELLO ARMANDO YASSER",
        "email":"armando.landa@alumno.buap.mx",
        "disabled":True,
        "password":"$2a$12$XBmghLLQXMfsSKNjPV5RzezBK/IJRo7vVw6nVYGB8QmlqSZyKWSWm"#2021
    
            },

    "Norma":{   ###
        "username":"Norma",
        "full_name":"LANDETA CALVARIO NORMA ANGELICA",
        "email":"norma.landeta@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$4F9MZEus9dH2hvrpp9RokeyDafvXTNnuXSPgedkna.QTSrIyUfKvy"#202122
    
            },

    "Maria":{   ###
        "username":"Maria",
        "full_name":"LIMON GARCIA MARIA DEL CARMEN",
        "email":"maria.limongar@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$FZnPl9Xlgr4d7PoBsRU7w.WthbYDPQbHl3u3KtN9onfMarhBKjhkW"#2021223
    
            },

    "Jafet":{
        "username":"Jafet",
        "full_name":"MARAVILLA LOPEZ JAFET",
        "email":"jafet.maravilla@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$O/yu0hXJLr3f5NZ7HfXVkO7BGGZIZdudkxjj0Hh91ThEha0DGHzIS"#20212236
    
            },

    "Marie":{
        "username":"Marie",
        "full_name":"MARIE SANCHEZ MIGUEL ANGEL",
        "email":"miguel.marie@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$FK/zZTDVE4STjs0P5nJXTOpiHClGA/HuKdLph5lDSfRYyPDHEiOV6"#202122368
    
            },

    "Arturo":{   ###
        "username":"Arturo",
        "full_name":"MARRUFO POLANCO RICARDO ARTURO",
        "email":"ricardo.marrufop@alumno.buap.mx",
        "disabled":False,
        "password":"$2a$12$0Kg5lBdy5ab.vGn.l.ESBeEd.OZJU4r5gwefG0S9FCBFEUiGprVkC"#2021223680
    
            },

    "Eunice":{   ###
        "username":"Eunice",
        "full_name":"MARTINEZ BARRALES EUNICE",
        "email":"eunice.martinezb@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$JRs3KXNX8Ug2ZWYdwabfaOL2R73.3fQEatKRUX/AvVjz.73JA2GOS"#20212236805
    
            },

    "Abdiel":{   ###
        "username":"Abdiel",
        "full_name":"PEREZ BALCON ABDIEL JONATHAN",
        "email":"abdiel.perezb@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$S8go6msplPLZiQ/AqEc1mO45sBz9R6YDiqPTrHwOMG4ThRuNY/LOi"#202122368058
    
            },

    "Jordy":{   ###
        "username":"Jordy",
        "full_name":"RAMIREZ HERNANDEZ JORDY",
        "email":"jordy.ramirez@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$cHTUlvbTtPGOEHfhA0974OjGKdAJvKuqlHdS3Soc6J.LmJ0IAH.02"#2021223680581
    
            },

    "Jesus":{   ###
        "username":"Jesus",
        "full_name":"SANTOS DE JESUS RODRIGO",
        "email":"rodrigo.santosdej@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$/CZCi50E8Fq22fpncl6Et.4jD9fYltEqKLiQNyWKuL8eSnjTCGfqu"#20212236805810
    
            },

    "Leonardo":{   ###
        "username":"Leonardo",
        "full_name":"SEDANO JIMENEZ LEONARDO NOE",
        "email":"leonardo.sedanoji@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$5z7MhArD5/gz6wYY45FMFOQ7VEnMHHJ0NjPINLPwMhb4ktp360czu"#202122368058102
    
            },

    "Tania":{   ###
        "username":"Tania",
        "full_name":"SEVILLA JIMENEZ TANIA",
        "email":"tania.sevilla@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$EZIwDKdWjeVg/jMkA2.uc.weG6vBoRwyTlw9HJfFiF50WFEdCd6.K"#3031
    
            },

    "Ivan":{   ###
        "username":"Ivan",
        "full_name":"SOLANO CARRERA IVAN",
        "email":"ivan.solano@alumno.buap.mx",
        "disabled": True,
        "password":"$2a$12$7/n4rI4Sw1Vth4snhYqJAe2nx7.oaH1sP.Xm/ZZuvM00N4FInkHS."#303123
    
            },

    "Angel":{   
        "username":"Angel",
        "full_name":"SUAREZ SALVATIERRA ANGEL EDUARDO",
        "email":"angel.suarezsa@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$lBK5eiBWGisQuxgmg.BnfO6pO5BSHpOWDO2qjnmg5Nj8G.DBXyVLu"#3031236
    
            },
    
    "Tlamani":{   ###
        "username":"Tlamani",
        "full_name":"TLAMANI XOCHIMITL JESUS",
        "email":"jesus.tlamani@alumno.buap.mx",
        "disabled": False,
        "password":"$2a$12$N4G1qyCzmFi/yOG.rHkIsO7eCJjA..3q4jXrBqJH7DFGMTv2fb0km"#303123689
    
            }

       
}


#1 Función para regresar el usuario completo de la base de datos (users_db), con contraseña encriptada
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username]) #** devuelve todos los parámetros del usuario que coincida con username

#4 Función final para devolver usuario a la solicitud del backend   
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
# Funcion para devolver recurso estatico dependiendo del usuario


    #3 Esta es la dependencia para buscar al usuario
async def auth_user(token:str=Depends(oauth2)):
    try:
        username= jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    
   # if username in user_equipo:
    #return search_user_static(username)
    #else:
    return search_user(username) #Esta es la entrega final, usuario sin password

#2 Función para determinar si usuario esta inactivo 
async def current_user(user:User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user
        
####################################################################################3
        
@app.post("/login/")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    #Busca en la base de datos "users_db" el username que se ingreso en la forma 
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    # Se obtienen los atributos incluyendo password del usuario que coincida el username de la forma 
    user= search_user_db(form.username)     
    
    #user.password es la contraseña encriptada en la base de datos
    #form.password es la contraseña original que viene en formulario
    if not crypt.verify(form.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    #Creamos expiración de 1 min a partir de la hora actual
    access_token_expiration=timedelta(minutes=ACCESS_TOKEN_DURATION)
    #Tiempo de expiración: hora actual mas 1 minuto
    expire=datetime.utcnow()+access_token_expiration
    
    access_token={"sub": user.username,"exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM), "token_type":"bearer"}


@app.get("/users/me/")
async def me(user:User= Depends (current_user)): #Crea un user de tipo User que depende de la función (current_user)
    username=user.username
    
    url="static/"+username+".jpg"

    try:
        open(url)
        return FileResponse(url)
    except FileNotFoundError:
       return user

#http://127.0.0.1:8000/login/

#username:Freddy
#password:1234

#http://127.0.0.1:8000/users/me/

#-uvicorn 7_jwt_auth_users:app --reload
