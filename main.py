from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from DBAccess.dbAccess import engine,Base
from Models import *
from routers import FitnessClassRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


# Below line will create models(tables) in DB
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(FitnessClassRouter.router)    
