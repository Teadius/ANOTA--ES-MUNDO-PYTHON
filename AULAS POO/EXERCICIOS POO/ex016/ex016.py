# Crie a classe funcionarios, onde podemos cadastrar nome, setro e cargo.
# Crie tambem um metodo que permita ao funcinario se apresentar.
from rich import print


class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentação(self):
        print(f"Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa Curso em Video.")


    def __str__(self):
        pass


c1 = Funcionario(nome="Maria", setor="Administrativo", cargo="TI")
print(c1.apresentação())

c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programação")
print(c1.apresentação())