import pandas as pd

class Preprocessor:
    def __init__(self, caminho):
        """Inicializa o pré-processador com o caminho do arquivo csv"""
        self.caminho = caminho
        self.arquivo = None

    def load_data(self):
        """Carrega o arquivo"""
        self.arquivo = pd.read_csv(self.caminho)
        return self
    
    def trocar_nome(self, nomes):
        """Troca os nomes das colunas. Passe um dicionário {nome_atual: novo_nome}"""
        self.arquivo.rename(columns=nomes, inplace=True)
        return self

    def mudar_tipo_para_datetime(self, coluna_date):
        """Converte a coluna para datetime"""
        self.arquivo[coluna_date] = pd.to_datetime(self.arquivo[coluna_date])
        return self
    
    def mudar_tipo_int(self, coluna_int):
        """Converte a coluna para inteiro"""
        self.arquivo[coluna_int] = self.arquivo[coluna_int].astype(int)
        return self

    def remove_strings_vazias(self, nome_coluna):
        """Remove linhas onde a coluna especificada é string vazia"""
        self.arquivo = self.arquivo[self.arquivo[nome_coluna].str.strip() != '']
        return self
    
    def ordenar_data(self, nome_coluna):
        """Ordena o dataframe pela coluna especificada"""
        self.arquivo = self.arquivo.sort_values(by=nome_coluna, ascending=True).reset_index(drop=True)
        return self
    
    def selecionar_colunas(self, lista):
        self.arquivo = self.arquivo[lista]
        return self
    
    def salvar_arquivo(self, caminho_arquivo):
        """Salva o dataframe no caminho especificado"""
        self.arquivo.to_csv(caminho_arquivo, index=False)
        return self
