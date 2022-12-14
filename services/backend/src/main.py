from fastapi import FastAPI
#add corsmiddleware
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")  # NEW

from src.routes import users, notes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8080", "http://localhost:5000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, World!"