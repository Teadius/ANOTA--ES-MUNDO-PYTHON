from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self, valor: float = 0.0):
        self._valor = 0.0
        if valor > 0:
            self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O pagamento só pode ser realizado com valores positivos.")

    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL, locale="pt_BR.UTF-8")
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} via {self.__class__.__name__}"
        except Exception as e:
            return f"Falha no pagamento de R$ {valor} via {self.__class__.__name__}: {e}"


class PIX(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} via {self.__class__.__name__}"
        except Exception as e:
            return f"Falha no pagamento de R$ {valor} via {self.__class__.__name__}: {e}"


class Credito(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} via {self.__class__.__name__}"
        except Exception as e:
            return f"Falha no pagamento de R$ {valor} via {self.__class__.__name__}: {e}"


def finalizar_Compra(tipo_pag: Pagamento, valor: float):
    print(tipo_pag.pagar(valor))