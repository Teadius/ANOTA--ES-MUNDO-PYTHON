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

a1 = Aluno(nome="João", idade=20, curso="Engenharia", turma="A")
a1.fazer_aniversario()
a1.fazer_matricula()
print(a1)
p1 = Professor(nome="Maria", idade=35, especialidade="Matemática", nivel="Doutorado")
p1.fazer_aniversario()
p1.dar_aula()
print(p1)
f1 = Funcionario(nome="Carlos", idade=40, cargo="Gerente", setor="Financeiro")
f1.fazer_aniversario()
f1.bater_ponto()
print(f1)



inspect(a1, methods=True, private=True, all=True)
inspect(p1, methods=True, private=True, all=True)
inspect(f1, methods=True, private=True, all=True)