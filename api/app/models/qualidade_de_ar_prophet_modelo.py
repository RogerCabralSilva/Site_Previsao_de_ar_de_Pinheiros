import pandas as pd
from prophet import Prophet
import os
import joblib

class QualidadeDeArProphet:
    def __init__(self):
        self.model = Prophet()
        self.fitted = False
    
    def prepare_date(self, data:pd.DataFrame, date_col:str, targer_col:str):
        df = data[[date_col, targer_col]].rename(columns={date_col:'ds', targer_col:'y'})
        return df
    
    def train(self, data:pd.DataFrame, date_col:str, target_col:str):
        df = self.prepare_date(data, date_col, target_col)
        self.model.fit(df)
        self.fitted=True
        return self
    
    def predict(self, periods:int, freq:str="D"):
        if not self.fitted:
            raise Exception("O modelo precisa ser treinado antes de prever.")
        
        future = self.model.make_future_dataframe(periods=periods, freq=freq)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    def save_model(self, path:str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        return self
    
    def load_model(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Modelo não encontrado em: {path}")
        self.model = joblib.load(path)
        self.fitted = True
        return self

    def plot(self, forecast):
        fig = self.model.plot(forecast)
        return fig

    def plot_components(self, forecast):
        fig = self.model.plot_components(forecast)
        return fig