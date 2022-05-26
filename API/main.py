
from fastapi import FastAPI
from Routers import BCN

app=FastAPI()
app.include_router(BCN.router)
@app.get("/")
def raiz():
    return{
        "message":"bienvenido"
    }

