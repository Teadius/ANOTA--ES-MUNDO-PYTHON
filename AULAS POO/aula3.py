# Python Orientado a Objetos: Criando Classes e Objetos na Prática - Curso Python POO: Aula 04
# "Objetos são variaveis evoluidas"
# O conceito de objeto se basea em estar juntando dados+funções.
# Objeto
# Assim, um objeto e uma variavel que alem de guardar dados, pode executar funcionalidades.
# Em outras palavras, objetos são variaveis que, alem de gaurdar dados, podem fazer coisas com esses dados.

#Declaração da classe:
class MinhaClasse:
    """area de Atributos"""
    """area de Metodos"""


# Declaração da clsse:
obj = MinhaClasse("instancia")  # Instancia > Metodo construtor > def__init__(self):


# Declaração de classe
class Gafanhoto:
    def __init__(self): # Metodo construtor
        # Atributo de instancia
        self.nome = ""
        self.idade = 0

    # Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        if self.nome == "":
            self.nome = "Nome não definido"
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 18
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())