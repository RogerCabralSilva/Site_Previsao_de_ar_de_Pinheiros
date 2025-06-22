import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.preprocessing.preprocessor import Preprocessor

# Pegando a raiz do projeto dinamicamente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Montando caminhos seguros
caminho_entrada = os.path.join(BASE_DIR, 'data', 'raw', 'qualidade_ar.csv')
caminho_saida = os.path.join(BASE_DIR, 'data', 'processed', 'qualidade_ar_processado.csv')

if __name__ == "__main__":

  pre = Preprocessor(caminho_entrada)

  pre.load_data()\
    .trocar_nome({' pm25' : 'pm25'})\
    .remove_strings_vazias("pm25")\
    .ordenar_data('date')\
    .mudar_tipo_para_datetime('date')\
    .selecionar_colunas(["date", "pm25"])\
    .salvar_arquivo(caminho_saida)

    
    

