
class Retangulo:
    def __init__(self, base = 1, altura = 1,):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da base deve ser um numero!")
        if valor < 0: 
            raise ValueError("Valor invalido para a base")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da altura deve ser um numero!")
        if valor < 0: 
            raise ValueError("Valor invalido para a base")
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("Area não pode ser configurada!")

    @property
    def medidas(self):
        return f"base = {self.base} \nAltura = {self.altura}"

    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas dentro de um tupla")
        if len(valores) != 2:
            raise SyntaxError("informe um tupla com menos de dois valores numericos")
        self.base = valores[0]
        self.altura = valores[1]
