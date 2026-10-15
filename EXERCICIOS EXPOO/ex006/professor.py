from pessoa import Pessoa
from rich import print
from rich import inspect

class Professor(Pessoa):
    def __init__(self, nome ="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = ""
        self.nivel = ""

    def dar_aula(self):
        print(f"{self.nome} começou a dar aula")