from rich import inspect, print
from Avaliacao import *


def main():
    av1 = Avaliacao(nome="Pedro", disciplina="Matematica")

    # Para alterar a nota utilize o set_nota
    av1.set_nota(10)

    # Para visualizar a nota utilize o get_nota
    print(f"Nota atual: {av1.get_nota()}")

    inspect(av1)


if __name__ == "__main__":
    main()