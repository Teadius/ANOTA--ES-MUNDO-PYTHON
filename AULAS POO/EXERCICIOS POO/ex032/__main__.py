from contabancaria import ContaBancaria

def main():
    cc = ContaBancaria(id=123, nome="Marcelo", saldo=1000)
    print("Valor depositado na conta")
    cc.depositar(1000)
    print("Valor para sacar. E necessario informar senha!")
    cc.sacar(500)
    print("Atualizar nome do titular")
    cc.nome = "Maricota"
    print(cc)

if __name__ == "__main__":
    main()