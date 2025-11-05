from fastapi import APIRouter, Depends
from src.auth.utils import valid_access_token

router = APIRouter(
    prefix="/private",
    tags=["Private Endpoints"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", dependencies=[Depends(valid_access_token)])
async def private_hello_world():
    return {"message": f"Hello World from private endpoint!"}