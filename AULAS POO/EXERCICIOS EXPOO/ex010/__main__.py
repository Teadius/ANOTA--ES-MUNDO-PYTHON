from rich import inspect, print
from Avaliacao import *


def main():
    av1 = Avaliacao(nome="Pedro", disciplina="Matematica")
    av1.nota = 3.5
    print(f"Nota atual: {av1.nota}")
    inspect(av1, private=True)


if __name__ == "__main__":
    main()