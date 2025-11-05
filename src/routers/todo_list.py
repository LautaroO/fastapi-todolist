from fastapi import APIRouter

router = APIRouter(
    prefix="/todo-lists",
    tags=["Todo Lists"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_todo_lists():
    todo_lists = []
    return {"todo_lists": todo_lists}