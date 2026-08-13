from abc import ABC, abstractclassmethod

class Transaporte:
    def __init__(self, distancia, frete=0):
        self.distancia = distancia
        self.frete = frete

    @abstractclassmethod
    def calcular_frete(self):
        pass


class Moto(Transaporte):
    fator = 0.50
    def __init__(self, distancia, frete=0):
        super().__init__(distancia, frete)


    def calcular_frete(self):
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transaporte):
    fator = 1.2
    def __init__(self, distancia, frete=0):
        super().__init__(distancia, frete)


    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Raio minimo de 50"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"


class Drone(Transaporte):
    fator = 9.50
    def __init__(self, distancia, frete=0):
        super().__init__(distancia, frete)


    def calcular_frete(self):
        if self.distancia > 10:
            self.frete = 0 
            return "Raio maximo de 10KM"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"