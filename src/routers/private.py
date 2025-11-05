from fastapi import APIRouter, Depends
from src.auth.utils import valid_access_token, require_roles

router = APIRouter(
    prefix="/private",
    tags=["Private Endpoints"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", dependencies=[Depends(valid_access_token)])
async def private_hello_world():
    return {"message": f"Hello World from private endpoint!"}


@router.get("/role-only", dependencies=[Depends(require_roles(["admin2"]))])
async def role_only_endpoint():
    return {"message": "Hello World from role-only endpoint!"}