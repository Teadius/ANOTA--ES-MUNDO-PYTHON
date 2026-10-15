from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario 

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_valor):
        raise ValueError("O salario não pode ser alterado!")

    @abstractmethod
    def calcular_bonus(self):
        pass


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return f"Total de salario com bonus de 10%: {self.salario*1.10:,.2f}"


class Gerente(Funcionario):
    def calcular_bonus(self):
        return f"Total de salario com bonus 15%: {self.salario*1.15:,.2f}"


class Dsigner(Funcionario):
    def calcular_bonus(self):
        return f"Total de salario com bonus 8%: {self.salario*1.08:,.2f}"
