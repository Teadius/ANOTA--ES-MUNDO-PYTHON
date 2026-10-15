

class Termostato:
    def __init__(self, temperatura=24):
        # Define a temperatura inicial usando o setter para aplicar as validações
        self.temperatura = temperatura

    @property
    def temperatura(self):
        """Getter: retorna o valor do atributo privado __temperatura."""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        """Setter: valida e limita o valor entre 16°C e 30°C."""
        if valor % 0.5 != 0:
            raise ValueError(f"temperatura de {valor} e invalida")
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        """Propriedade formatada para exibir a temperatura com a unidade."""
        return f"{self.__temperatura} °C"