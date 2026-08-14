from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    salario_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome=None, salario_bruto=0):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_liquido = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        qtd_salarios_minimos = (
            self.salario_liquido / Funcionario.salario_minimo
        )
        mensagem =(
            f"Funcionário: {self.nome}"
            f"Salário Bruto: R$ {self.salario_bruto:.2f}"
            f"Salário Líquido: R$ {self.salario_liquido:.2f}"
            f"Equivale a aproximadamente {qtd_salarios_minimos:.1f} salários mínimos."
        )
        painel = Panel(
            renderable=mensagem, title="Análise de Salário", width=50
        )
        print(painel)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora=7.37, qtd_horas=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        desconto = self.salario_bruto * (Funcionario.desconto_inss / 100)
        self.salario_liquido = self.salario_bruto - desconto
        return self.salario_liquido


class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto)

    def calcular_salario(self):
        desconto = self.salario_bruto * (Funcionario.desconto_inss / 100)
        self.salario_liquido = self.salario_bruto - desconto
        return self.salario_liquido