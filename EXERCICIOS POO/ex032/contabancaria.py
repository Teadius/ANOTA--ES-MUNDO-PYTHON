from hashlib import sha256

class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id:int, nome:str, saldo:float=0, chave:str=None):
        self._id = id
        self._titular = nome
        self.__saldo = max(0, saldo) 
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self) -> str:

        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha

    def validar_senha(self, chave):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo."
        #return f"Estado atual da conta: {self.__dict__}"

    @property
    def saldo(self):
        """Retorna o saldo atual (apenas leitura)."""
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito NEGADO: O valor deve ser maior que zero.")
            return
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito: R${valor:,.2f}')

    def sacar(self, valor:float, chave:str=None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque NEGADO de R${valor:,.2f} na conta {self._id} (Saldo insuficiente)')
            else:
                self.__saldo -= valor
                print(f'Saque: -R${valor:,.2f}')
        else:
            print(f"Senha não confere saque não autorizado!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str=None):
        chave= self.pede_senha()
        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
            else:
                print("Senha não confere. Não posso alterar o nome!")
