from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractclassmethod
    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: Au au au!")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: auauauauauauauauau!")

class PitBull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: Ruf Ruf Ruf!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: Miau!")


class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: Quack!")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer: Pô pô pô!")

