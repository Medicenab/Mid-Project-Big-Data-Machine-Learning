from fastapi import APIRouter
from database.mongodb import db
from bson import json_util
from json import loads
router= APIRouter()

@router.get("/all/data")
def get_all():
    res = list(db["INM.NATION"].find({}))
    return loads(json_util.dumps(res))

@router.get("/year")
def get_year():
    res=list(db["INM.NATION"].find({}).distinct("Year"))
    return loads(json_util.dumps(res))

@router.get("/district")
def get_district():
    res=list(db["INM.NATION"].find({}).distinct("District Name"))
    return loads(json_util.dumps(res))

@router.get("/district-year/{district}/{year}")
def get_district_name(district:str,year:str):
    res = list(db["INM.NATION"].find({"Year":year}).find({"District Name":district}))
    return loads(json_util.dumps(res))

    
