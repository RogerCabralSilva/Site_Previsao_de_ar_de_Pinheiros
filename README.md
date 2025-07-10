# 🌬️ Previsão da Qualidade do Ar - Pinheiros/SP

Este projeto fornece uma **previsão interativa da qualidade do ar** na região de Pinheiros, São Paulo. A aplicação consome dados históricos, realiza modelagem preditiva e apresenta gráficos informativos para auxiliar a população e gestores ambientais.

## 📌 Objetivo

Desenvolver uma aplicação acessível para prever a qualidade do ar (em especial o material particulado **MP10**) com base em dados meteorológicos e históricos, permitindo ao usuário escolher o número de dias ou meses para prever.

---

## 📊 Funcionalidades

- 📈 **Previsão de MP10** para 7, 15 ou 30 dias
- 📅 Opção de previsão mensal (até 12 meses)
- 📍 Foco na região de **Pinheiros - São Paulo**
- 🧠 Modelo de machine learning treinado com dados reais
- 📉 Gráficos intuitivos com plotagem automatizada
- 🌐 Interface web leve e responsiva

---

## 🧪 Tecnologias Utilizadas

| Componente | Tecnologia |
|-----------|------------|
| Backend   | Python, Pandas, Scikit-Learn, Joblib |
| Modelagem | Regressão Linear / Random Forest |
| Frontend  | Streamlit / Plotly |
| Dados     | CETESB, INMET, APIs públicas |
| Gráficos  | Matplotlib, Seaborn, Plotly |
| Outros    | Docker (opcional), Git, VSCode |

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.10+
- Pip
- (opcional) Ambiente virtual

### Passos

```bash
# Clone o repositório
git clone https://github.com/seuusuario/qualidade-ar-pinheiros.git
cd qualidade-ar-pinheiros

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate.bat  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
