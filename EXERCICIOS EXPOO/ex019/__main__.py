from crud import *


def exibir_menu():
    print("\n" + "=" * 30)
    print("      SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoa")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)


def main():
    cadastro_em_massa()
    if criar_banco():
        print("Algum problema aconteceu ao criar o banco")
        raise SystemExit
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        match opcao:
            case "1":
                if not cadastrar_pessoa():
                    print("\n[ERRO] não foi possivel cadastrar a pessoa")
            case "2":
                if not listar_pessoa():
                    print("\n[ERRO] não foi possivel listar a pessoa")
            case "3":
                if not atualizar_pessoa():
                    print("\n[ERRO] não foi possivel atualiar a pessoa")
            case "4":
                if not excluir_pessoa():
                    print("\n[ERRO] não foi possivel excluir a pessoa")
            case "5":
                if not buscar_pessoa():
                    print("\n[ERRO] não foi possivel buscar a pessoa")
            case "0":
                print("Encerrando o sistema...")
                break
            case _:
                print("[ERRO] Opção inválida! Escolha um valor entre 0 e 5!")
        input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
