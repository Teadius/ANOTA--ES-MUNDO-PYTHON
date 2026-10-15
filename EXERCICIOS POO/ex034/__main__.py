from classes import *

def main():
    f1 = Desenvolvedor("João", 8000)
    f2 = Gerente("Carla", 10000)
    f3 = Dsigner("Pedro", 5000)
    try:
        f1.salario = 15000
        f2.salario = 15000
        f3.salario = 15000
    except ValueError as e:
        print(f"Erro captura: {e}")
    print(f1.calcular_bonus())
    print(f2.calcular_bonus())
    print(f3.calcular_bonus())


if __name__ == "__main__":
    main()
