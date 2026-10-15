from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg: str = "", tipo: str = "Aviso", icone: str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(
            self._mensagem, 
            title=f"{self._icone} {self._tipo.upper()}", 
            style="#ffffff on #000000", 
            width=50
        )
        print(msg)


class Erro(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, "Erro", ":x:")

    def mostrar(self):
        msg = Panel(
            self._mensagem, 
            title=f"{self._icone} {self._tipo.upper()}", 
            style="#ffffff on #880000", 
            width=50
        )
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, "Alerta", ":warning:")

    def mostrar(self):
        msg = Panel(
            self._mensagem, 
            title=f"{self._icone} {self._tipo.upper()}", 
            style="#000000 on #fffc1b", 
            width=50
        )
        print(msg)