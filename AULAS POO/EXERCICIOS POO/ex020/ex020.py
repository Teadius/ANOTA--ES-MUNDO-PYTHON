# Crie a classe Gamer, onde pedemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie tambem um metodo que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []


    def add_favoritos(self, game):
        self.jogos.append(game)


    def ficha(self):
        jogos_str = "\n".join(f"- {jogo}" for jogo in self.jogos)
        conteudo = (
            f"**Nome real** {self.nome}\n"
            f"**Nick:** {self.nick}\n\n"
            f"**Jogos favoritos:**\n{jogos_str}"
        )
        print(Panel(conteudo, title=f"Ficha Gamer: {self.nick}", expand=False))


g1 = Gamer(nome="Gabriel", nick="Teadius Gaos")
g1.add_favoritos("Dark souls Remastered")
g1.add_favoritos("Batman arkham knight")
g1.add_favoritos("DOOM Eternal")
g1.add_favoritos("Elden ring")
g1.ficha()
