class Numero:
    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o numero {self.valor} dentro do numero."


class Texto:
    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do texto."


class Lista:
    def __init__(self, lst: list | None = None):
        self.valores = lst if lst is not None else []

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da minha lista."


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está dobrado? {'novo' if not self.dobrado else 'dobrado'}."


class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return "Era uma casa muito engraçada."


def tente_dobrar(obj):
    try:
        obj.dobrar()
    except AttributeError:
        print(f"Tive dificuldades para dobrar o objeto do tipo {obj.__class__.__name__}.")