from rich import print
from rich.panel import Panel

caixa = Panel(renderable="[white]Esse aqui é um painel de exemplo[/]", title="Mensagem", style="red")
print(caixa)
