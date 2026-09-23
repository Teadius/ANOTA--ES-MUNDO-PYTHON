from classes import *

def main():
    p1 = Produto(nome="Notebook", preco=8500)
    p2 = Produto(nome="Mouse", preco=250)
    p3 = Produto(nome="Fone de ouvido", preco=450.35)
    c1 = Carrinho()
    c2 = Carrinho()
    c1 = c1 + p1 + p2 + p3
    print(c1)


if __name__ == "__main__":
    main()
