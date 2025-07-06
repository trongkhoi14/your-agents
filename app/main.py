from fastapi import FastAPI
from app.routes.v1 import auth
from app.routes.v1 import agent

app = FastAPI()
app.include_router(auth.router)
app.include_router(agent.router)