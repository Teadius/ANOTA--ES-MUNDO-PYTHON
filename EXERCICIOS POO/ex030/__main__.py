from credencial import Credencial

def main():
    c = Credencial()
    c.senha = str(input("Digite a senha: "))
    print(c.senha)
    c.validar("4002")


if __name__ == "__main__":
    main()
