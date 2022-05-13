from fastapi import FastAPI
from Routers import pokemon, persona

app = FastAPI()

# Incluimos los endpoints de los ficheros pokemon y persona
app.include_router(pokemon.router)
app.include_router(persona.router)

@app.get("/")
def raiz():
    return {
        "message":"Bienvenido a mi API"
    }

@app.get("/info")
def info():
    return {
        "message":1
    }


# Para ejecutar la api: uvicorn <nombre_archivo>:<nombre_variable> 
# uvicorn main:app

# En modo desarrollador:
# uvicorn main:app --reload