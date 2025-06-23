from fastapi import FastAPI
from app.routes.v1 import auth

app = FastAPI()
app.include_router(auth.router)