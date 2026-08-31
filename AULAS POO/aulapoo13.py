# Polimorfismo


# Polimorfismo em Python: Override, Overload e Duck Typing Explicados- Curso Python POO: Aula 13

# O polimorfismo em programação orientada a objetos (POO) com Python é a capacidade de diferentes objetos responderem ao mesmo nome de método de maneiras específicas para cada tipo.

# Exemplo do Cachorro e do gato
class Cachorro:
    def falar(self):
        return "Au au!"


class Gato:
    def falar(self):
        return "Miau!"


def emitir_som(objeto_animal):
    print(objeto_animal.falar())


# Usando o polimorfismo
c = Cachorro()
g = Gato()

emitir_som(c)  # Saída: Au au!
emitir_som(g)  # Saída: Miau!

# O python e uma linguagem que permite o polimorfismo pode ser feito sem herança, mas no geral herança e ecenssial para polimorfismo na programação no geral.
# Pilimorfismo vem do grego que significa polýs(vários) e morphé(forma), ou seja, varias formas.
# Polimorfismo: Propriedade ou estado que se apresenta e/ou se comporta de várias formas diferentes.
# "um unico nome, mas comportamentos diferentes".
# Pro exemplo a maioria dos animais e especies podem se comunicaer mesmo que de formas distintas.


# Exemplo do pato e do peixe
class Pato:
    def locomocao(self, tipo_locomocao):
        if tipo_locomocao == "agua":
            return "O pato está nadando na água."
        elif tipo_locomocao == "solo":
            return "O pato está andando no solo."
        elif tipo_locomocao == "ar":
            return "O pato está voando no ar."
        else:
            return "Tipo de locomoção desconhecido."


class Peixe:
    def locomocao(self, tipo_locomocao):
        if tipo_locomocao == "agua":
            return "O peixe está nadando na água."
        else:
            return "O peixe não consegue se mover aqui."


def mover_animal(animal, meio):
    print(animal.locomocao(meio))


pato = Pato()
mover_animal(pato, "agua")  # Saída: O pato está nadando na água.
mover_animal(pato, "ar")    # Saída: O pato está voando no ar.
mover_animal(pato, "solo")    # Saída: O pato está andando no solo.

peixe = Peixe()
mover_animal(peixe, "agua")
mover_animal(peixe, "solo")



# Funcion Overload
print(len("gustavo"))
print(len(["Sandy","Junio"]))
print(len({"a":"x", "b":"y"}))

# Operator Overload
print(f"5 positivo e = a {+5}")
print(f"2 + 3 = {2+3}")
print("poli + morfismo = ","Poli"+"morfismo")
print([3,5]+[2,4])


# Polimorfismo de Inclusão ou Overrride/Subtyping
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


a = Cachorro("Bandit")
b = Gato("Frajola")
e = Spitz("Luluzinha")
f = PitBull("Guerreiro")
a.emitir_som()
b.emitir_som()
e.emitir_som()
f.emitir_som()



# Tambem existem outros tipos de poliomorfismo mas no fim se trata do conceito de varias formas.
# Polimorfismo de Inclusão(Override /Subtyping), Polimorfismo de Sobrecarga(Ad-Hoc Overloading), Polimorfismo de Coerção(Ad-Hoc Coercion) e por fim Polimorfismo de Paramétrico(Templete/Generic)
# Somente sera tratado no curso os dois primeiros ate o momento.



# Sera tratado o polimorfismo "Duck Typing" ou inclusão de sobrecarga/Overload

class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz Pudim com leite condensado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no oleo de soja")


class Filho(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite em po e chocolate com avela")


p1 = Mae("Jaciara")
p2 = Filho("Matheus")
p1.fazer_pudim()
p1.fritar_coxinha()
print()
p2.fazer_pudim()           # O  override sobrescreve basicamente
p2.fritar_coxinha()



# sera tratado tambem o polimorfismo de inclusão.


