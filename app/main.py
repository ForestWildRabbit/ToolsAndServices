from fastapi import FastAPI, APIRouter
from app.routers import users_router

app = FastAPI()

base_router = APIRouter(prefix="/api")

base_router.include_router(users_router)

app.include_router(base_router)
