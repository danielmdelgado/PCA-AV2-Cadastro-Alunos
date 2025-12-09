import pandas as pd
import os

# FUNÇÃO PARA CARREGAR OS ARQUIVOS
def carregar_csv():
    """
    Lê o arquivo alunos.csv e retorna um DataFrame.
    Se o arquivo não existir, cria um DataFrame vazio.
    """
    if os.path.exists("alunos.csv"):
        df = pd.read_csv("alunos.csv")
    else:
        df = pd.DataFrame(columns=["matricula", "nome", "rua", "numero", "bairro", "cidade", "uf", "telefone", "email"])
    return df

# FUNÇÃO PARA SALVAR O DATAFRAME NO ARQUIVO CSV
def salvar_csv(df):
    df.to_csv("alunos.csv", index=False)
