from CaucularFrete import *
from rich import print, inspect
from rich.table import Table


def main():
    dist = int(input("Digite a distancia da viagem: "))
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    tabela = Table(title="Tabela de fretes")
    tabela.add_column("distancia")
    tabela.add_column("tipo")
    tabela.add_column("frete")
    for item in viagem:
        tabela.add_row(f"{dist}KM", f"{type(item).__name__}", f"{item.calcular_frete()}")
    print(tabela)

if __name__ == "__main__":
    main()