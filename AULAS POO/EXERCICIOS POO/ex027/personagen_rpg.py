from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = random.choice(self.golpes)
            print(f"[green]{self.nome}[/] ({self.vida} HP) atacou [red]{alvo.nome}[/] ({alvo.vida} HP) com um [blue]{golpe}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu [red]{fator}[/] de dano')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Corte frontal", "Investida", "Contra-ataque"]

    def curar(self):
        fator = random.randint(10, 100)
        self.vida += fator
        print(f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {fator} de vida (Vida total: {self.vida})")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Flecha mágica", "Raio de luz"]

    def curar(self):
        fator = random.randint(10, 100)
        self.vida += fator
        print(f"{self.nome} usou uma magia de cura e recuperou {fator} de vida (Vida total: {self.vida})")
