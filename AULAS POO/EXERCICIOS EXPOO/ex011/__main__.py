
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
print(len("Gustavo Guanabara"))
print(len(["Sandy","Junio"]))
print(len({"a":"x", "b":"y"}))

# Operator Overload
print(f"5 positivo e = a {+5}")
print(f"2 + 3 = {2+3}")
print("poli + morfismo = ","Poli"+"morfismo")
print([3,5]+[2,4])

