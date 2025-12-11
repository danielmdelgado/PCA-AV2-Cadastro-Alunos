# FUNÇÃO PARA MOSTRAR O MENU DO PROGRAMA

def mostrar_menu():
    """
    Mostra o menu principal e retorna a escolha do usuário.
    """
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Inserir aluno")
    print("2 - Pesquisar aluno")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    return opcao
