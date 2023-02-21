from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import incisoA, incisoB, incisoC, incisoD, incisoE

app = FastAPI()
 
app.include_router(incisoA.router)
app.include_router(incisoB.router)
app.include_router(incisoC.router)
app.include_router(incisoD.router)
app.include_router(incisoE.router)

from incisoE import CountryAttributes, CountryAttributes_list

@app.get("/continent/region/{code}/", status_code = status.HTTP_200_OK)
async def usersclass(code:str):
    users=filter (lambda user: user.Code == code, CountryAttributes_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region no encontrada")


@app.get("/")

async def imprimir():
    return "Hola estudiantes"

@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}


