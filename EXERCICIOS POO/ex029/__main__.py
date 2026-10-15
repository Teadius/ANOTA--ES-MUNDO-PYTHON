from diario import Diario
from rich import inspect, print

def main():
    d = Diario()
    d.escrever("Consegui fazer o exercicio")
    d.escrever("Eu sou Brasileiro")
    d.escrever("Tenho 2963 anos.")
    try:
        d.ler('1234')
    except Exception as e:
        print(f"[red]Erro: {e}[/]")
    try:
        d.ler("4002")
    except Exception as e:
        print(f"[red]Erro: {e}[/]")
    inspect(d, private=True)

if __name__ == "__main__":
    main()
