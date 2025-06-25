from fastapi.testclient import TestClient

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from main import app

client = TestClient(app)

def test_root_status():
    # Se quiser testar um endpoint raiz (se tiver)
    response = client.get("/")
    assert response.status_code == 404  # ou 200 se existir

def test_predict_next_success():
    # Teste POST no endpoint de previsão, simulando uma requisição válida
    payload = {"period": 3, "unit": "days"}

    response = client.post("/api/predict_next", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    for item in data:
        assert "ds" in item
        assert "yhat" in item
        assert "yhat_lower" in item
        assert "yhat_upper" in item

def test_predict_next_invalid_unit():
    # Teste com unidade inválida pra garantir que a API trata erro
    payload = {"period": 3, "unit": "anos"}

    response = client.post("/api/predict_next", json=payload)
    # Seu código pode retornar 422 (erro de validação) ou 400
    assert response.status_code == 422 or response.status_code == 400

def test_predict_next_missing_period():
    # Teste com dado faltando para ver se a API valida bem
    payload = {"unit": "days"}

    response = client.post("/api/predict_next", json=payload)
    assert response.status_code == 422  # erro de validação do pydantic
