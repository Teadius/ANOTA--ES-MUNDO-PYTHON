# Crie a classe funcionarios, onde podemos cadastrar nome, setro e cargo.
# Crie tambem um metodo que permita ao funcinario se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    # O atributo de classe e definido em todos os objetos
    empresa = "Cruso em video" # Cada objeto ganha o atributo em epresa.
    def __init__(self, nome, setor, cargo):
        # O atributo de instancia e definido de acordo com o definido.
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentação(self):
        print(f":handshake:Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}.")


c1 = Funcionario(nome="Maria", setor="Administrativo", cargo="TI")
print(c1.apresentação())
c1.empresa = "nome empresa teste"
print(c1.apresentação())
c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programação")
print(c2.apresentação())
# inspect(c1, all=True) # para ver os detalhes da classe