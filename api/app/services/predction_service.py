import pandas as pd
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import joblib
import os
from pathlib import Path
import joblib


def generate_future_dates(period: int, unit: str):
    today = pd.Timestamp.today().normalize()

    if unit == "days":
        return [today + timedelta(days=i) for i in range(1, period + 1)]
    elif unit == "months":
        return [today + relativedelta(months=i) for i in range(1, period + 1)]
    else:
        raise ValueError("unit precisa ser 'days' ou 'months'")

def predict_future(period: int, unit: str):
    future_dates = generate_future_dates(period, unit)
    BASE_DIR = Path(__file__).resolve().parent
    model_path = BASE_DIR / ".." / "models" / "prophet_model.pkl"
    model_path = model_path.resolve()

    model = joblib.load(model_path)

    future_df = pd.DataFrame({"ds": pd.to_datetime(future_dates)})
    forecast = model.predict(future_df)

    result = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
    # Converter datetime para string (formato ISO ou só data)
    result["ds"] = result["ds"].dt.strftime("%Y-%m-%d")

    return result.to_dict(orient="records")

