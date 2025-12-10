from functions.file_manager import carregar_csv, salvar_csv
from functions.menu import mostrar_menu
from functions.operacoes import inserir, pesquisar


def main():
    #Carregar o CSV no início do programa
    df = carregar_csv()

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            df = inserir(df)
            salvar_csv(df)

        elif opcao == "2":
            df = pesquisar(df)
            salvar_csv(df)

        elif opcao == "3":
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
            