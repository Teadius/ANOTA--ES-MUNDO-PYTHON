import math
from abc import ABC, abstractmethod


# ADICIONE O (ABC) AQUI
class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado):
        super().__init__(4)  # Agora funcionará corretamente
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado**2


class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * (self.raio**2)