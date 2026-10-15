from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)
    c1 += 50
    c2 += 50
    print(c1)
    print(c2)
    print(c1 == c2)

if __name__ == "__main__":
    main()


# Metodos magicos para operadores

# equal to                 | p1 == p2 | p1.__eq__(p2)
# not equal to             | p1 != p2 | p1.__ne__(p2)
# less than                | p1 < p2  | p1.__lt__(p2)
# less than or equal to    | p1 <= p2 | p1.__le__(p2)
# greater than             | p1 > p2  | p1.__gt__(p2)
# greater than or equal to | p1 >= p2 | p1.__ge__(p2)
# in-place addition        | p1 += p2 | p1.__iadd__(p2)
# in-place subtract        | p1 -= p2 | p1.__isub__(p2)