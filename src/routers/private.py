from fastapi import APIRouter, Depends
from src.auth.utils import oauth2_scheme

router = APIRouter(
    prefix="/private",
    tags=["Private Endpoints"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", dependencies=[Depends(oauth2_scheme)])
async def private_hello_world():
    return {"message": f"Hello World from private endpoint!"}