# Encapsulamento: Getters, Setters e @Property (Parte2) - Curso Python POO: Aula 11

# O encapsulamento visa manter a integridade do sistema, protegendo o estado interno do objeto contra interferência externa não regulamentada.

# Acesso aos dados:
# Existem duas maneiras de permitir acesso aos dados encapsulados:
# > Uso de getters e setters
# > Uso de decorador @Property

# Metodo getter e setter

# metodo

class Avaliacao:

    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota  # Atributo protegido/encapsulado

    def get_nota(self):  # Métodos acessores (Getter)
        return self._nota

    def set_nota(self, valor):  # Métodos modificadores (Setter)
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida")

# main

from rich import inspect, print

av1 = Avaliacao(nome="Pedro", disciplina="Matematica")
# Para alterar a nota utilize o set_nota
av1.set_nota(10)
# Para visualizar a nota utilize o get_nota
print(f"Nota atual: {av1.get_nota()}")
inspect(av1)


# Metodo Decorado @property

