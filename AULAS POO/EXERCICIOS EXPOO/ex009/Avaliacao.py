from rich import print


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