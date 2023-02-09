from fastapi import FastAPI
import router0, router1, router2, router3, router4, router5, router6, router7, router8, router9

app = FastAPI()

app.include_router(router0.router)
app.include_router(router1.router)
app.include_router(router2.router)
app.include_router(router3.router)
app.include_router(router4.router)
app.include_router(router5.router)
app.include_router(router6.router)
app.include_router(router7.router)
app.include_router(router8.router)
app.include_router(router9.router)


@app.get("/")

async def imprimir():
    return "Hola estudiantes"

@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}

