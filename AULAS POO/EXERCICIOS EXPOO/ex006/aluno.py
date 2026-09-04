from pessoa import Pessoa
from rich import print
from rich import inspect

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade, )
        self.curso = ""
        self.turma = ""

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")
