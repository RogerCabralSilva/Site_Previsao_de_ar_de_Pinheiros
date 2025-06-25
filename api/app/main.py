from fastapi import FastAPI
from api.app.endpoints.routes import router

from pathlib import Path

app = FastAPI(title="Previsão da Qualidade do Ar")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
