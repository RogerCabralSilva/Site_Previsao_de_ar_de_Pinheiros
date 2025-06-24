import pandas as pd
from prophet import Prophet
import os
import joblib
import matplotlib.pyplot as plt


class QualidadeDeArProphet:
    def __init__(self):
        print("⚙️  Inicializando modelo Prophet...")
        self.model = Prophet()
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
        forecast = forecast.reset_index(drop=True)
        forecast['ds'] = pd.to_datetime(forecast['ds'])

        fig = self.model.plot(forecast)
        return fig

    def plot_components(self, forecast: pd.DataFrame):
        print("📊 Gerando gráfico dos componentes...")
        fig = self.model.plot_components(forecast)
        plt.show()
        return fig

    def plot_custom(self, forecast: pd.DataFrame):
        
          # Garante que tudo tá no tipo correto
        forecast = forecast.copy()

        forecast['ds'] = pd.to_datetime(forecast['ds'])
        forecast['yhat'] = pd.to_numeric(forecast['yhat'], errors='coerce')
        forecast['yhat_lower'] = pd.to_numeric(forecast['yhat_lower'], errors='coerce')
        forecast['yhat_upper'] = pd.to_numeric(forecast['yhat_upper'], errors='coerce')

        # Verifica se ficou NaN
        if forecast.isnull().sum().sum() > 0:
            raise ValueError("❌ Forecast contém NaN depois da conversão. Verifique os dados.")

        print("🖼️ Gerando gráfico customizado...")
        plt.figure(figsize=(12, 6))
        plt.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='blue')
        plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                         color='lightblue', alpha=0.5, label='Intervalo de confiança')

        plt.title('Previsão de PM2.5')
        plt.xlabel('Data')
        plt.ylabel('PM2.5')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
