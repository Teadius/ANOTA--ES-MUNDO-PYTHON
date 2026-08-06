from rich import print
from rich import inspect


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade, )
        self.curso = ""
        self.turma = ""

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")

class Professor(Pessoa):
    def __init__(self, nome ="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = ""
        self.nivel = ""

    def dar_aula(self):
        print(f"{self.nome} começou a dar aula")

class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = ""
        self.setor = ""

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto")