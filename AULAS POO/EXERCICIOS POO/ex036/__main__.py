from classes import *

def main():
    finalizar_Compra(PIX(), valor=2340.00)
    finalizar_Compra(Boleto(), valor=150.00)
    finalizar_Compra(Credito(), valor=370.00)


if __name__ == "__main__":
    main()