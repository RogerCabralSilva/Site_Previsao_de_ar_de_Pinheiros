from fastapi import APIRouter
from api.app.schemas.prediction_schema import FutureRequest, ForecastOutput
from api.app.services.predction_service import predict_future
from api.app.usuarios.routes import router as usuarios_router

router = APIRouter()

# 👇 Isso inclui /api/usuarios/cadastro
router.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])

@router.post("/predict_next", response_model=list[ForecastOutput])
def predict_next(request: FutureRequest):
    return predict_future(request.period, request.unit)
