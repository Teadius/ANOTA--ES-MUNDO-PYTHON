from pessoa import Pessoa
from rich import print
from rich import inspect


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = ""
        self.setor = ""

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto")