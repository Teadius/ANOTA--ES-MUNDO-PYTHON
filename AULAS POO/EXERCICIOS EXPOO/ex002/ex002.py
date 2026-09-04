# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que e um pessoa que tem nome e idade.

    Para criar uma pessoa, use
    variavel = Gaganhoto(nome, idade)
    """
    def __init__(self, n="Sem nome", i=0): # Metodo construtor
        # Atributo de instancia
        self.nome = n
        self.idade = i
    # Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade-1} anos de idade e fara {self.idade} em seu aniversario!"
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"


# Declaração de objetos
g1 = Gafanhoto(n="Maria", i=17) # define a variavel como um objeto com dois atributos
g1.aniversario() # Adiciona um para o aniversario
print(g1) # Chama o __str__() que retorna a mensagem 

print(g1.__doc__) # DEUNDER ATTRIBUTE descreve a documentação presente no codigo

print(g1.__dict__) # Atributo pois não tem parenteses
print(g1.__getstate__()) # Metodo pois possui parentesis no final
print(g1.__class__) # Mostra o nome da classe
"""
Classe: É a "planta" ou o modelo que define a estrutura de um objeto. Ela descreve quais características (atributos) e comportamentos (métodos) um objeto terá (23:44).

Objeto: É a instância concreta da classe. Se a classe é o projeto de uma casa, o objeto é a casa construída fisicamente (23:57).

Atributo: São as variáveis que definem as características de um objeto (ex: nome, idade, saldo). Eles armazenam os dados específicos daquela instância (24:02).

Estado: É o conjunto dos valores atuais dos atributos de um objeto em um dado momento. O estado diz "quem" ou "como" aquele objeto está (ex: uma conta bancária com saldo de R$ 3.500) 
(24:04).

Método: São as funções definidas dentro da classe que representam o comportamento do objeto. Eles permitem que o objeto execute ações ou altere seu próprio estado (ex: depositar(), 
sacar()) (1:48, 33:47).
"""
