# Herança


# Herança em Python explicada como nunca fizeram - Curso Python POO: Aula 7

# Essa aula ira trabalahr os 4 pilares da poo, abstração, encapsulamento, herança e polimorfismo.

# Herança:
# é um relacionamento entre intes gerais(ancestrais) e tipos especificos(descendentes).
# itens, que herdam atributos e metodos dos nuveis superiores.
    # Vantagens:
    # - Reaproveitamento de código
    # - Organização de codigo
    # - Facilita a manutenção do código
    # - extensibilidade
    # - Suporte a polimorfismo
# Ex: uma classe superior chamada Animal, e uma classe inferior chamada Cachorro, que herda os atributos e métodos da classe Animal.

# Super classe ou classe base, ancestral ou classe mãe
#  ^^^^^   Herança / generalização / relação tipo "é um"
# Subclasse ou classe derivada, descendente ou classe filha

"""
===============================================================================
HERANÇA EM PYTHON — PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
===============================================================================
Aula 07: Curso de Python POO — Professor Gustavo Guanabara

A herança é um dos quatro pilares da POO (junto com Abstração, Encapsulamento 
e Polimorfismo). Trata-se de um relacionamento do tipo "É UM" (is-a), onde 
classes derivadas (subclasses) herdam atributos e métodos de classes 
ancestrais (superclasses), promovendo o reuso e a organização de código.
===============================================================================
"""


# -----------------------------------------------------------------------------
# 1. SUPERCLASSE (GENERALIZAÇÃO / CLASSE MÃE)
# -----------------------------------------------------------------------------
class Pessoa:
    """Representa a entidade genérica Pessoa.
    
    Contém os atributos e métodos comuns a todos os seres humanos do sistema.
    """

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self) -> None:
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")


# -----------------------------------------------------------------------------
# 2. SUBCLASSES (ESPECIALIZAÇÃO / CLASSES FILHAS)
# -----------------------------------------------------------------------------
class Aluno(Pessoa):
    """Subclasse que herda de Pessoa (Aluno É UMA Pessoa).
    
    Reutiliza nome e idade, adicionando atributos e métodos específicos do aluno.
    """

    def __init__(self, nome: str, idade: int, matricula: str, curso: str):
        # O comando super() executa o construtor __init__ da superclasse Pessoa
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def cancelar_matricula(self) -> None:
        """Método exclusivo da classe Aluno."""
        print(f"A matrícula {self.matricula} do aluno {self.nome} foi cancelada.")


class Professor(Pessoa):
    """Subclasse que herda de Pessoa (Professor É UMA Pessoa).
    
    Reutiliza nome e idade, adicionando especialidade e salário.
    """

    def __init__(self, nome: str, idade: int, especialidade: str, salario: float):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.salario = salario

    def receber_aumento(self, valor: float) -> None:
        """Método exclusivo da classe Professor."""
        self.salario += valor
        print(f"O professor {self.nome} recebeu R${valor:.2f} de aumento. Novo salário: R${self.salario:.2f}")


class Funcionario(Pessoa):
    """Subclasse que herda de Pessoa (Funcionario É UMA Pessoa)."""

    def __init__(self, nome: str, idade: int, setor: str, trabalhando: bool = True):
        super().__init__(nome, idade)
        self.setor = setor
        self.trabalhando = trabalhando

    def mudar_trabalho(self) -> None:
        """Alterna o status de trabalho do funcionário."""
        self.trabalhando = not self.trabalhando
        status = "trabalhando" if self.trabalhando else "de folga/desligado"
        print(f"O funcionário {self.nome} agora está {status}.")


# -----------------------------------------------------------------------------
# 3. DEMONSTRAÇÃO PRÁTICA E VANTAGENS
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # VANTAGENS DA HERANÇA:
    # 1. Reaproveitamento de Código (DRY - Don't Repeat Yourself)
    # 2. Organização Hierárquica e Manutenção Facilitada
    # 3. Extensibilidade do Sistema (Fácil adição de novas subclasses)
    # 4. Suporte para Polimorfismo

    # Instanciando objetos das subclasses
    aluno1 = Aluno(nome="Maria", idade=20, matricula="12345", curso="Informática")
    prof1 = Professor(nome="Gustavo Guanabara", idade=40, especialidade="Python POO", salario=5000.00)
    func1 = Funcionario(nome="Carlos", idade=35, setor="Estoque")

    # Acesso a atributos herdados (Pessoa)
    print(f"Aluno: {aluno1.nome}, Idade: {aluno1.idade}")
    print(f"Professor: {prof1.nome}, Especialidade: {prof1.especialidade}")

    # Execução de métodos herdados da superclasse
    aluno1.fazer_aniversario()  # Atributo 'idade' herdado sofre alteração
    prof1.fazer_aniversario()

    # Execução de métodos específicos de cada subclasse
    aluno1.cancelar_matricula()
    prof1.receber_aumento(1200.00)
    func1.mudar_trabalho()