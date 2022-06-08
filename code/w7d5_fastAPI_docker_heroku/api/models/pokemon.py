from pydantic import BaseModel
from typing import Optional

# Estructura que debe de tener el body.
class Pokemon(BaseModel):
    name:str
    id:Optional[int]