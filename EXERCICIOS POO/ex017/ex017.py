# Crie a classe produto, onde podemos cadastrar nome e o preço.
# Crie tambem um metodo que mostre uma etiquera de preço do procuto.

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"{self.nome} custa R{self.preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}\n"
        conteudo += f"{'-'*30}\n"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)


p1 = Produto(nome="iPhone 17 Pro Max", preco=25000.85)
p2 = Produto(nome="Notebook Gamer", preco=8000)

p1.etiqueta()
p2.etiqueta()
