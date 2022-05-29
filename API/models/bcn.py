from pydantic import BaseModel
class Nat(BaseModel):
    District_Name:str
    Neighborhood_Name:str
    Nationality:str
    Number:int
    id:int
