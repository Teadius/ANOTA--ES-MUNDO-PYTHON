from personagen_rpg import *

def main():
    p1 = Guerreiro(nome='Megaman', vida=1000)
    p2 = Mago(nome='Merlin', vida=5000)
    p3 = Guerreiro(nome='Kratos', vida=1500)

    p1.atacar(p2)
    p3.atacar(p1)
    p2.atacar(p3)

    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()