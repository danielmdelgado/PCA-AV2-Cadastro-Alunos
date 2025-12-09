# FUNÇÃO PARA INSERIR DADOS NO ARQUIVO CSV
def inserir(df):
    """
    Recebe o DataFrame, coleta os dados do usuário,
    cria um novo registro e retorna o DataFrame atualizado.
    """
    #Gera matrícula automaticamente
    if df.empty:
            matricula = 1
    else:
        matricula = df["matricula"].max() + 1

    #Recolhe dados do usuário
    nome = input("Nome: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    #Cria registro do novo usuário
    aluno_novo = {
         "matricula": matricula,
         "nome": nome,
         "rua": rua,
         "numero": numero,
         "bairro": bairro,
         "cidade": cidade,
         "uf": uf,
         "telefone": telefone,
         "email": email,
    }

    #Inseri no DataFrame
    df.loc[len(df)] = aluno_novo

    print(f"\nAluno cadastrado com sucesso! Matrícula: {matricula}")

    return df
        