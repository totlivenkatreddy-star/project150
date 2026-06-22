from fastapi import FastAPI
from app.routers import users_router


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Task Manager API running"}
    

app.include_router(
    users_router.router
)