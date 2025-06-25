import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def calculate_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def evaluate_model(real_df: pd.DataFrame, forecast_df: pd.DataFrame):
    """
    real_df: DataFrame com dados reais -> ['ds', 'y']
    forecast_df: DataFrame com previsão -> ['ds', 'yhat']
    """

    merged = pd.merge(real_df, forecast_df[['ds', 'yhat']], on='ds', how='inner')

    mae = mean_absolute_error(merged['y'], merged['yhat'])
    rmse = np.sqrt(mean_squared_error(merged['y'], merged['yhat']))
    mape = calculate_mape(merged['y'], merged['yhat'])

    results = {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE (%)': mape
    }

    return results 