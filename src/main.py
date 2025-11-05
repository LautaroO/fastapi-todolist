from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from src.routers import private, todo_list

app = FastAPI()

app.include_router(todo_list.router)
app.include_router(private.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World!!"}