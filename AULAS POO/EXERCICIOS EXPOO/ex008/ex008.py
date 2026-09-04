class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self._saldo = max(0, saldo)  # Evita saldo inicial negativo

    @property
    def saldo(self):
        """Retorna o saldo atual (apenas leitura)."""
        return self._saldo

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito NEGADO: O valor deve ser maior que zero.")
            return
        
        self._saldo += valor
        print(f'Depósito: R${valor:,.2f}')

    def sacar(self, valor):
        if valor <= 0:
            print("Saque NEGADO: O valor deve ser maior que zero.")
            return

        if valor > self._saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id} (Saldo insuficiente)')
        else:
            self._saldo -= valor
            print(f'Saque: -R${valor:,.2f}')
