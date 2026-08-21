from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(id=111, nome="Maria", saldo=5000)
    print(c1)
    c1.depositar(500)
    print(c1)
    c1.sacar(1000)
    print(c1)
    c1.sacar(2000000)
    print(c1)
    c1.sacar(-100)
    print(c1)
    c1.depositar(-500)
    print(c1)


if __name__ == "__main__":
    main()
