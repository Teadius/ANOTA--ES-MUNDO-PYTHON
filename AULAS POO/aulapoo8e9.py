# Abstração


# aula sobre o pilar da abstração

# A abstraçãio e a arte de ignorar o irrelevante e se focar estritamente no essencial.
# EX: Voce não precisa saber como um carro funciona para poder dirigir, você só precisa saber como usar o volante, os pedais e a alavanca de câmbio.
# Existe a abstração de dados que e quando ignoramos informações desnecessarias para o escopo do projeto.
# Exisre a abstração de processos, que e quando não sabemos como um metodo faz seu trabalho, apenas sabe que ele existe pela interface.

# Classe abstrata e uma classe que nao pode ser instanciada, ou seja, nao podemos criar objetos dela. Ela serve apenas como modelo para outras classes.
# EX: ControleGenerido() e uma base para todos os controles que forma classes filho.
# Não tem codigo em metodos abstratos, pois quem define e o metodo e a clsse filho.

# Classe abstrata
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def fazer_aniversario(self):
        self.idade += 1

# Classe filho
class aluno:
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

a = aluno("João", 20, "12345")
print(a.nome, a.idade, a.matricula)

# Uma classe abstrata numca sera instanciada, ja que ela sera usada apenas como base para as subclasses.
# Ao definir um conjunto de metodos abstratos, dizemos que estamos criando a interface publica da classe.
# Uma classe abstrata pode ter metodos abstratos que devem ser obrigatoriamente implementados nas subclasses.
# Mas uma classe abstrata pode ter metodos concretos se eles funcionatem da mesma maneira para todos os subclasses(DRY).

# Metodo ABC (abstract base class)
# O metodo ABC e um metodo para utilizar classes abstratas em pyrthon.
