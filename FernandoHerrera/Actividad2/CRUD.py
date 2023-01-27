#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn 3_crud:app --reload-
#{"id"="3","Name":"Alfredo", "LastName":"Garcia", "Age":"30"}
#Definimos nuestra entidad: user

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
             User(	PassengerID=5, 	    Survived=0, 	Pclass=3, 	Name="Allen, Mr. William Henry",  	                            Sex="male",  	Age="35",  	SibSp=0, 	Parch=0, 	Ticket="373450",  	        Fare="8.05",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=6, 	    Survived=0, 	Pclass=3, 	Name="Moran, Mr. James",                                    	Sex="male",  	Age="",  	SibSp=0, 	Parch=0, 	Ticket="330877",  	        Fare="8.4583",   	Cabin="",  	    Embarked="Q"),
             User(	PassengerID=7, 	    Survived=0, 	Pclass=1, 	Name="McCarthy, Mr. Timothy J",  	                            Sex="male",  	Age="54",  	SibSp=0, 	Parch=0, 	Ticket="17463",  	        Fare="51.8625",   	Cabin="E46",  	Embarked="S"),
             User(	PassengerID=8, 	    Survived=0, 	Pclass=3, 	Name="Palsson, Master. Gosta Leonard",  	                    Sex="male",  	Age="2",  	SibSp=3, 	Parch=1, 	Ticket="349909",  	        Fare="21.075",   	Cabin="",  	    Embarked="S"),
             User(	PassengerID=9, 	    Survived=1, 	Pclass=3, 	Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",   	Sex="female",  	Age="27",  	SibSp=0, 	Parch=2, 	Ticket="347742",  	        Fare="11.1333",   	Cabin="",  	    Embarked="S"),
             User(	PassengerID=10, 	Survived=1, 	Pclass=2, 	Name="Nasser, Mrs. Nicholas (Adele Achem)",                 	Sex="female",  	Age="14",  	SibSp=1, 	Parch=0, 	Ticket="237736",  	        Fare="30.0708",   	Cabin="",  	    Embarked="C"),
             User(	PassengerID=11, 	Survived=1, 	Pclass=3, 	Name="Sandstrom, Miss. Marguerite Rut",  	                    Sex="female",  	Age="4",  	SibSp=1, 	Parch=1, 	Ticket="PP 9549",  	        Fare="16.7",  	    Cabin="G6",  	Embarked="S"),
             User(	PassengerID=12, 	Survived=1, 	Pclass=1, 	Name="Bonnell, Miss. Elizabeth",                            	Sex="female",  	Age="58",  	SibSp=0, 	Parch=0, 	Ticket="113783",  	        Fare="26.55",   	Cabin="C103",  	Embarked="S"),
             User(	PassengerID=13, 	Survived=0, 	Pclass=3, 	Name="Saundercock, Mr. William Henry",  	                    Sex="male",  	Age="20",  	SibSp=0, 	Parch=0, 	Ticket="A/5. 2151",  	    Fare="8.05",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=14, 	Survived=0, 	Pclass=3, 	Name="Andersson, Mr. Anders Johan",  	                        Sex="male",  	Age="39",  	SibSp=1, 	Parch=5, 	Ticket="347082",  	        Fare="31.275",  	Cabin="",  	    Embarked="S"),
             User(	PassengerID=15, 	Survived=0, 	Pclass=3, 	Name="Vestrom, Miss. Hulda Amanda Adolfina",                	Sex="female",  	Age="14",  	SibSp=0, 	Parch=0, 	Ticket="350406",  	        Fare="7.8542",  	Cabin="",  	    Embarked="S"),
             User(	PassengerID=16, 	Survived=1, 	Pclass=2, 	Name="Hewlett, Mrs. (Mary D Kingcome)",                     	Sex="female",  	Age="55",  	SibSp=0, 	Parch=0, 	Ticket="248706",  	        Fare="16",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=17, 	Survived=0, 	Pclass=3, 	Name="Rice, Master. Eugene",                                	Sex="male",  	Age="2",  	SibSp=4, 	Parch=1, 	Ticket="382652",  	        Fare="29.125",     	Cabin="",  	    Embarked="Q"),
             User(	PassengerID=18, 	Survived=1, 	Pclass=2, 	Name="Williams, Mr. Charles Eugene",  	                        Sex="male",  	Age="",  	SibSp=0, 	Parch=0, 	Ticket="244373",  	        Fare="13",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=19, 	Survived=0, 	Pclass=3, 	Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Sex="female",  	Age="31",  	SibSp=1, 	Parch=0, 	Ticket="345763",  	        Fare="18",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=20, 	Survived=1, 	Pclass=3, 	Name="Masselmani, Mrs. Fatima",                             	Sex="female",  	Age="",  	SibSp=0, 	Parch=0, 	Ticket="2649",  	        Fare="7.225",  	    Cabin="",  	    Embarked="C"),
             User(	PassengerID=21, 	Survived=0, 	Pclass=2, 	Name="Fynney, Mr. Joseph J",                                	Sex="male",  	Age="35",  	SibSp=0, 	Parch=0, 	Ticket="239865",  	        Fare="26",  	    Cabin="",  	    Embarked="S"),
             User(	PassengerID=22, 	Survived=1, 	Pclass=2, 	Name="Beesley, Mr. Lawrence",                               	Sex="male",  	Age="34",  	SibSp=0, 	Parch=0, 	Ticket="248698",  	        Fare="13",  	    Cabin="D56",  	Embarked="S"),
             User(	PassengerID=23, 	Survived=1, 	Pclass=3, 	Name="McGowan, Miss. Anna 'Annie'",  	                        Sex="female",  	Age="15",  	SibSp=0, 	Parch=0, 	Ticket="330923",  	        Fare="8.0292",     	Cabin="",  	    Embarked="Q"),
             User(	PassengerID=24, 	Survived=1, 	Pclass=1, 	Name="Sloper, Mr. William Thompson",  	                        Sex="male",  	Age="28",  	SibSp=0, 	Parch=0, 	Ticket="113788",  	        Fare="35.5",  	    Cabin="A6",  	Embarked="S"),
             User(	PassengerID=25, 	Survived=0, 	Pclass=3, 	Name="Palsson, Miss. Torborg Danira",                       	Sex="female",  	Age="8",  	SibSp=3, 	Parch=1, 	Ticket="349909",  	        Fare="21.075",  	Cabin="",  	    Embarked="S")]

#***Get
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
#@app.get("/usersclass/{id}")
#async def usersclass(id:int):
#    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
#    try:
#        return list(users)[0]
#    except:
#        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1
 
 
#***Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@app.put("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID   == user.PassengerID:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@app.delete("/usersclass/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerID == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1