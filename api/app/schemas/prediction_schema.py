from pydantic import BaseModel
from typing import List

class FutureRequest(BaseModel):
  period: int # Quantidade (ex 7)
  unit: str # days ou months

class ForecastOutput(BaseModel):
  ds: str
  yhat: float
  yhat_lower: float
  yhat_upper: float