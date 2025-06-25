import pandas as pd
from prophet import Prophet
import os
import joblib
import matplotlib.pyplot as plt


class QualidadeDeArProphet:
    def __init__(self):
        print("⚙️  Inicializando modelo Prophet...")
        self.model = Prophet(changepoint_prior_scale=0.05,
                             seasonality_mode='multiplicative')
        self.fitted = False

    def prepare_date(self, data: pd.DataFrame, date_col: str, target_col: str):
        print("🧹 Preparando os dados...")
        df = data[[date_col, target_col]].rename(columns={date_col: 'ds', target_col: 'y'}).copy()
        df['ds'] = pd.to_datetime(df['ds'])

        if df.isnull().sum().sum() > 0:
            raise ValueError("❌ Dados possuem valores nulos. Trate antes de treinar.")

        return df

    def train(self, data: pd.DataFrame, date_col: str, target_col: str):
        df = self.prepare_date(data, date_col, target_col)
        print("🏋️‍♂️ Treinando o modelo...")
        self.model.add_seasonality(name=' monthly', period=30.5, fourier_order=5)
        self.model.fit(df)
        self.fitted = True
        return self

    def predict(self, periods: int, freq: str = "D"):
        if not self.fitted:
            raise Exception("❌ O modelo precisa ser treinado antes de prever.")

        print(f"🔮 Gerando previsão para {periods} períodos futuros...")
        future = self.model.make_future_dataframe(periods=periods, freq=freq)
        forecast = self.model.predict(future)

        forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
        forecast['ds'] = pd.to_datetime(forecast['ds'])
        return forecast

    def save_model(self, path: str):
        print(f"💾 Salvando modelo em {path}")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        return self

    def load_model(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ Modelo não encontrado em: {path}")

        print(f"📦 Carregando modelo de {path}")
        self.model = joblib.load(path)
        self.fitted = True
        return self

    def plot(self, forecast: pd.DataFrame):
        print("📊 Gerando gráfico da previsão...")
        # Python
        
        from prophet.plot import plot_plotly

        return print(plot_plotly(self.model, forecast))

    def plot_components(self, forecast: pd.DataFrame):
        print("📊 Gerando gráfico dos componentes...")
        fig = self.model.plot_components(forecast)
        plt.show()
        return fig
