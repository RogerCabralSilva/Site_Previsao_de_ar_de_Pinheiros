from fastapi import FastAPI
from api.app.endpoints.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Previsão da Qualidade do Ar")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# 👇 Isso inclui todas as rotas com prefixo /api
app.include_router(router, prefix="/api")
