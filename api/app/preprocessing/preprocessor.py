import pandas as pd

class Preprocessor:
    def __init__(self, caminho):
        """
        Inicializa o pré-processador com o caminho do arquivo csv
        """
        self.caminho = caminho
        self.arquivo = None

    def load_data(self):
        self.arquivo = pd.read_csv(self.caminho)
        return self
    
    def trocar_nome(self, ):
        self.arquivo.rename(columns={})
        
        