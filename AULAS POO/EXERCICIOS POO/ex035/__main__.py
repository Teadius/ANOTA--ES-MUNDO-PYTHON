from classes import *
from rich import print, inspect

def main():
    a1 = DOC(nome="Prova", tam=550000)
    a2 = PDF(nome="Contrato", tam=1200000)
    inspect(a1)
    a1.abrir_arquivo()
    inspect(a2)
    a2.abrir_arquivo()


if __name__ == "__main__":
    main()
