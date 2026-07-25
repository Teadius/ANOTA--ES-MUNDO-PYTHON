
# Metodo 1 para ler uma funcionalidade
print(int.__dict__)

# Metodo 2 para ler uma funcionalidade
from rich import print

print(int.__dict__)

# Metodo 3 para ler uma funcionalidade
from rich import print
from rich import inspect
inspect(int, all=True)


# Exemplo com exercicio
class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem {self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Deposito R${valor:,.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}')
        else:
            self.saldo = self.saldo - valor
            print(f'Saque -R${valor:,.2f}')

c1 = ContaBancaria(id=112, nome="Gustavo", saldo=3000)
print(c1)
c1.depositar(500)
c1.sacar(1000)
c1.sacar(2000000)
print(c1)

inspect(c1, all=True)