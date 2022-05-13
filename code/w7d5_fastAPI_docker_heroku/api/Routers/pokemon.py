from fastapi import APIRouter, Header
from database.mongodb import db
from models.pokemon import Pokemon
from bson import json_util
from json import loads

# Solo un archivo puede tener la clase FastAPI (el main). El resto deben
# de tener APIRouter y deben de ser incluidos por el motor de la API (FastAPI)
router = APIRouter()

# La pasamos valores al endpoint a traves de un Header
@router.get("/pokemon/confidencial")
def confidencial(id = Header(None)):
    return {"confidencial":id}

# Le pasamos valores al endpoint a traves del propio endpoint
# Ademas, especificamos que el valor debe de ser de tipo int
@router.get("/pokemon/{id}")
def get_pokemons(id:int):
    res = list(db["pokemon"].find({"id":id}))[0]
    return loads(json_util.dumps(res))
    
    
# Le pasamos valores al endpoint a traves del body
@router.post("/add/pokemon")
def add_pokemon(pokemon: Pokemon):
    resultado = db["pokemon"].insert_one(pokemon.dict())
    return {
        "meesage":"Añadido correctamente",
        "id":f"{resultado.inserted_id}"
    }

# Le pasamos valores al endpoint a traves de los web parameters
@router.get("/types/pokemon")
def add_pokemon(types:str):
    res = list(db["pokemon"].find({"types.type.name":"grass"}, {"name":1, "_id":0}))
    return loads(json_util.dumps(res))