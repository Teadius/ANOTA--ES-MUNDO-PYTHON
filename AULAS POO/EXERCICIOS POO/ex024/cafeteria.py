from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        print("---Iniciando o preparo---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("---Bebida Pronta---")

    def ferver_agua(self):
        print("Ferver agua em 100°C")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("Passando a agua pressurizada pelo po de cafe moido.")

    def servir(self):
        print("Servindo em xicara pequena")


class Cha(BebidaQuente):
    def misturar(self):
        print("Mergulhando o sache de ervas na agua.")

    def servir(self):
        print("Servindo na caneca de porcelana com limao")


class Leite(BebidaQuente):
    def misturar(self):
        print("Passando agua pressurizada pelo bico do leite")

    def servir(self):
        print("Servindo na caneca grande, ja com cafe")