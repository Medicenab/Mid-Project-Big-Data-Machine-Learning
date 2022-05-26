from fastapi import APIRouter
from database.mongodb import db
from bson import json_util
from json import loads
router= APIRouter()


@router.get("/BCN/{Nationality}")
def get_nat(Nationality):
    res = list(db["Nacionalidades"].find({}).distinct("Nationality"))
    return res

@router.get("/BCN/id/{id}")
def get_bcn(id):
    res=list(db["id"].find({"id":id}))[0]
    return loads(json_util.dumps(res))