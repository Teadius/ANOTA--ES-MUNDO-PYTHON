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



# Operator Overloading em Python: Personalizando Operadores na Prática - Curso Python POO: Aula 14

from functools import singledispatchmethod

class Analisar:
    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possivel analisar o valor {valor}")

    @analisar.register 
    def _(self, valor:int):
        print(f"{valor} é um número inteiro.")

    @analisar.register
    def _(self, valor:float):
        print(f"{valor} é um numero real.")

    @analisar.register
    def _(self, valor:str):
        print(f"{valor} é um cadeia de caracteres.")

    @analisar.register
    def _(self, valor: tuple | list | dict):
        print(f"{valor} é uma coleção de dados.")


x = Analisar()
x.analisar([3,4,5,3])


# Metodos magicos para operadores

# equal to                 | p1 == p2 | p1.__eq__(p2)
# not equal to             | p1 != p2 | p1.__ne__(p2)
# less than                | p1 < p2  | p1.__lt__(p2)
# less than or equal to    | p1 <= p2 | p1.__le__(p2)
# greater than             | p1 > p2  | p1.__gt__(p2)
# greater than or equal to | p1 >= p2 | p1.__ge__(p2)
# in-place addition        | p1 += p2 | p1.__iadd__(p2)
# in-place subtract        | p1 -= p2 | p1.__isub__(p2)

class Carteira:
    def __init__(self,valor:int|float=0):
        self.__saldo = valor

    def __str__(self):
        return f"Voce tem R${self.saldo:,.2f} na carteira."

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Voce não tema altorização para alterar o saldo desse jeito.")

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor:int|float):
        self.__saldo = self.__saldo + valor
        return self

    def __isub(self, valor:int|float):
        self.__saldo = self.__saldo - valor
        return self


c1 = Carteira(100)
c2 = Carteira(200)
c1 += 50
c2 += 50
print(c1)
print(c2)
print(c1 == c2)





# Polimorfismo "Duck typing"
# "Se parece com um pato, nada como um pato, voa como um pato e faz 'quack', então provavelmente é um pato."
# Esse e o jeito pythonico de se fazer polimorfismo: Não inporta o tipo do objeto, o que inporta e se ele pode fazer alguma coisa.

class Porta:
    def abrir(self):
        print("Girar a maçaneta e empurrar a porta.")

class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ.")

class Ovo:
    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes na frigideira.")

class Pedra:
    pass

# Metodo pythonico polimorfico duck typing

def tentar_abrir(obj):
    try:
        obj.abrir()
    except AttributeError:
        print(f"Encontrei problemas ao abrir {obj.__class__.__name__}.")



a = Porta()
b = Empresa()
c = Ovo()
d = Pedra()

tentar_abrir(a)
tentar_abrir(b)
tentar_abrir(c)
tentar_abrir(d)

# o uso pratico do duck typing cada coisa e feita de uma forma diferente mas isso não interessa o que inporta e o que o objeto faz.



class Numero:
    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o numero {self.valor} dentro do numero."


class Texto:
    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do texto."


class Lista:
    def __init__(self, lst: list | None = None):
        self.valores = lst if lst is not None else []

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da minha lista."


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está dobrado? {'novo' if not self.dobrado else 'dobrado'}."


class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return "Era uma casa muito engraçada."


def tente_dobrar(obj):
    try:
        obj.dobrar()
    except AttributeError:
        print(f"Tive dificuldades para dobrar o objeto do tipo {obj.__class__.__name__}.")

a = Numero(200)
b = Texto("Gafanhoto")
c = Lista([1,2,3])
d = Papel()
e = Casa()

tente_dobrar(a)
tente_dobrar(b)
tente_dobrar(c)
#tente_dobrar(d)
tente_dobrar(e)

print(a)
print(b)
print(c)
print(d)
print(e)
