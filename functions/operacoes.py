# FUNÇÃO PARA INSERIR DADOS NO ARQUIVO CSV
def inserir(df):
    """
    Recebe o DataFrame, coleta os dados do usuário,
    cria um novo registro e retorna o DataFrame atualizado.
    """
    # Gera matrícula automaticamente
    if df.empty:
        matricula = 1
    else:
        matricula = df["matricula"].max() + 1

    # Recolhe dados do usuário
    nome = input("Nome: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    # Cria registro do novo usuário
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

    # Inseri no DataFrame
    df.loc[len(df)] = aluno_novo

    print(f"\nAluno cadastrado com sucesso! Matrícula: {matricula}")

    return df


def pesquisar(df):
    """
    Pesquisa o aluno por nome ou matrícula.
    Após encontrar, permite editar ou remover.
    Depois retorna o DataFrame atualizado.
    """

    print("\n=== PESQUISAR ALUNO ===")
    print("1 - Pesquisar por matrícula")
    print("2 - Pesquisar por nome")
    opcao = input("Escolha: ")

    if opcao == "1":
        try:
            mat = int(input("Digite a matrícula: "))
        except:
            print("Matrícula inválida")
            return df

        resultado = df[df["matricula"] == mat]

    elif opcao == "2":
        nome = input("Digite o nome: ").strip().lower()
        resultado = df[df["nome"].str.lower() == nome]

    else:
        print("Opção inválida.")
        return df

    # Se não houver resultado
    if resultado.empty:
        print("\nAluno não encontrado.")
        return df

    # Mostra o aluno encontrado
    aluno = resultado.iloc[0]
    print("\n=== ALUNO ENCONTRADO ===")
    print(aluno)

    # Escolha pra fazer a ação
    acao = input("\n(E) Editar | (R) Remover | (V) Voltar : ").strip().upper()

    if acao == "E":
        df = editar(df, aluno["matricula"])

    elif acao == "R":
        df = remover(df, aluno["matricula"])

    return df


def editar(df, matricula):
    """
    Edita o campo selecionado de um aluno cadastrado
    """

    print("\n=== EDITAR ALUNO ===")

    print("1 - Nome")
    print("2 - Rua")
    print("3 - Número")
    print("4 - Bairro")
    print("5 - Cidade")
    print("6 - UF")
    print("7 - Telefone")
    print("8 - Email")

    opcao = input("Escolha o campo que deseja editar: ")

    campos = {
        "1": "nome",
        "2": "rua",
        "3": "numero",
        "4": "bairro",
        "5": "cidade",
        "6": "uf",
        "7": "telefone",
        "8": "email"
    }

    if opcao not in campos:
        print("Opção inválida.")
        return df

    campo = campos[opcao]
    novo_valor = input(f"Digite o novo valor para {campo}: ")

    df.loc[df["matricula"] == matricula, campo] = novo_valor

    print("\nDado atrualizado com sucesso!")

    return df


def remover(df, matricula):
    """
    Remove o aluno pela matrícula, apos a confirmação.
    """

    print("\n=== REMOVER ALUNO ===")
    confirma = input("Tem certeza que deseja remover? (S/N): ").strip().upper()

    if confirma != "S":
        print("Remoção cancelada.")
        return df

    df = df[df["matricula"] != matricula]

    print("\nAluno removido com sucesso!")

    return df
