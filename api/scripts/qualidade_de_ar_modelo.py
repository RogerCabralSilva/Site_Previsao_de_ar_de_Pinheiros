import sys
import os
import pandas as pd
from datetime import datetime

# Permitir importar a classe do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.qualidade_de_ar_prophet_modelo import QualidadeDeArProphet


# ===========================
# 📁 Configurações de Caminhos
# ===========================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

CAMINHO_DADOS = os.path.join(BASE_DIR, 'data', 'processed', 'qualidade_ar_processado.csv')
CAMINHO_MODELO = os.path.join(BASE_DIR, 'app', 'models', 'prophet_model.pkl')
CAMINHO_FORECAST = os.path.join(
    BASE_DIR, 'data', 'processed', f'forecast_{datetime.now().strftime("%Y%m%d%H%M")}.csv'
)

# ===========================
# 🚀 Pipeline de Execução
# ===========================
if __name__ == "__main__":
    try:
        print("🚀 Carregando dados...")
        df = pd.read_csv(CAMINHO_DADOS, parse_dates=["date"])

        print("✅ Dados carregados com sucesso!")

        print("🏗️ Instanciando o modelo Prophet...")
        model = QualidadeDeArProphet()

        print("🏋️‍♂️ Treinando o modelo...")
        model.train(df, date_col="date", target_col="pm25")

        print("💾 Salvando o modelo treinado...")
        model.save_model(CAMINHO_MODELO)
        print(f"✅ Modelo salvo em: {CAMINHO_MODELO}")

        print("🔮 Fazendo previsão para os próximos 30 dias...")
        forecast = model.predict(periods=30)

        print("💾 Salvando a previsão...")
        forecast.to_csv(CAMINHO_FORECAST, index=False)
        print(f"✅ Previsão salva em: {CAMINHO_FORECAST}")

        print("📊 Gerando gráfico da previsão...")
        model.plot_custom(forecast)

        print("🧠 Gerando gráfico dos componentes (Tendência, Sazonalidade)...")


        print("🎉 Pipeline finalizado com sucesso!")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
