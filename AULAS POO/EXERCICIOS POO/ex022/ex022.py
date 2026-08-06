# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 10

    def __init__(self, canal=1, volume=2):
        self.__canal = canal
        self.__volume = volume
        self.__ligado = False

    def liga_desliga(self):
        self.__ligado = not self.__ligado

    def aumentar_volume(self):
        if self.__ligado and self.__volume < ControleRemoto.volume_max:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__ligado and self.__volume > ControleRemoto.volume_min:
            self.__volume -= 1

    def aumentar_canal(self):
        if self.__ligado and self.__canal < ControleRemoto.canal_max:
            self.__canal += 1

    def diminuir_canal(self):
        if self.__ligado and self.__canal > ControleRemoto.canal_min:
            self.__canal -= 1

    def mostrar_tv(self):
        conteudo = ""
        if not self.__ligado:
            conteudo = ":prohibited: [red]A TV está desligada[/red]"
        else:
            conteudo = "[bold]Canais:[/bold]\n"
            for canal in range(
                ControleRemoto.canal_min, ControleRemoto.canal_max + 1
            ):
                if canal == self.__canal:
                    conteudo += f" -> [green]Canal {canal}[/green]\n"
                else:
                    conteudo += f"    Canal {canal}\n"

            conteudo += f"\n[bold]Volume: {self.__volume}[/bold]\n"
            for volume in range(
                ControleRemoto.volume_min, ControleRemoto.volume_max + 1
            ):
                if volume <= self.__volume:
                    conteudo += "[blue]█[/blue]"
                else:
                    conteudo += "[grey39]█[/grey39]"

        tv = Panel(conteudo, title="[ TV ]", width=40)
        print(tv)


# Exemplo de teste interativo:
c = ControleRemoto()

while True:
    c.mostrar_tv()
    comando = input(
        "\nDigite um comando (l on/off 0, + VOL -  < CH >"
    ).strip().lower()
    match comando:
        case "0":
            break
        case "1":
            c.liga_desliga()
        case "+":
            c.aumentar_volume()
        case "-":
            c.diminuir_volume()
        case ">":
            c.aumentar_canal()
        case "<":
            c.diminuir_canal()
