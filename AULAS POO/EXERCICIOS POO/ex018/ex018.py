# Crie a classe Churrasco, onde seja possivel informar quantas pessaos vão participar e mostre quanto de carne deve ser comprado, o csuto total do churrasco e o preço por pessao.

from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_por_pessoa = 0.4
    preco_kg = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def calcular_qtd_carne(self) -> float:
        return self.quant * Churrasco.consumo_por_pessoa

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quant

    def analisar(self):
        # Chamada dos métodos para obter os valores
        valorec = self.calcular_qtd_carne()
        custot = self.calcular_custo_total()
        racha = self.calcular_custo_individual()

        conteudo = (
            f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n"
            f"Cada participante comerá {Churrasco.consumo_por_pessoa}kg e cada Kg custa R${Churrasco.preco_kg:,.2f}\n"
            f"Recomendo [blue]comprar {valorec:,.3f}Kg[/] de carne\n"
            f"O custo total sera de [green]R${custot:,.2f}[/]\n"
            f"Cada pessoa pagara [yellow]R${racha:,.2f}[/] para participar."
        )
        analise = Panel(conteudo, title=self.titulo, width=104)
        print(analise)


c1 = Churrasco(titulo="Churras dos Amigos", quant=15)
c1.analisar()