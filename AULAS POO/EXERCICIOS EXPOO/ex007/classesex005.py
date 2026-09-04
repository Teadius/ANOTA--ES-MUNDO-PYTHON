from rich import print
from rich import inspect
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade, )
        self.curso = ""
        self.turma = ""

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")

    def estudar(self):
            pass

class Professor(Pessoa):
    def __init__(self, nome ="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = ""
        self.nivel = ""

    def dar_aula(self):
        print(f"{self.nome} começou a dar aula")

    def estudar(self):
            pass

class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = ""
        self.setor = ""

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto")

    def estudar(self):
            pass
