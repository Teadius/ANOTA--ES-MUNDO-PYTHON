from classes import Mensagem, Alerta, Erro

def main():
    Mensagem("Esse curso é ótimo para aprender python!").mostrar()
    Alerta("Atenção às configurações do sistema.").mostrar()
    Erro("Ocorreu uma falha na conexão.").mostrar()

if __name__ == "__main__":
    main()