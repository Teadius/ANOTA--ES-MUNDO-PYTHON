class Porta:
    def abrir(self):
        print("Girar a maçaneta e empurrar a porta.")

class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ.")

class Ovo:
    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes na frigideira.")

class Pedra:
    pass

# Metodo pythonico polimorfico duck typing

def tentar_abrir(obj):
    try:
        obj.abrir()
    except AttributeError:
        print(f"Encontrei problemas ao abrir {obj.__class__.__name__}.")
