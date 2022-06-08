from fastapi import APIRouter

router = APIRouter()

@router.get("/persona/confidencial")
def confidencial(id):
    return {"confidencial":id}