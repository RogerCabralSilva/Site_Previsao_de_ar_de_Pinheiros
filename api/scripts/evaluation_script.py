import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.evaluation.evaluate_model import evaluate_model

# Pegando a raiz do projeto dinamicamente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Montando caminhos seguros
caminho_dados = os.path.join(BASE_DIR, 'data', 'processed', 'qualidade_ar_processado.csv')

caminho_forescast = os.path.join(BASE_DIR, 'data', 'processed', 'novo_teste.csv')

real = pd.read_csv(caminho_dados, parse_dates=["date"])

real.rename(columns={"date":"ds", "pm25":"y"}, inplace=True)

forecast = pd.read_csv(caminho_forescast, parse_dates=["ds"])

results = evaluate_model(real, forecast)

print(results)
