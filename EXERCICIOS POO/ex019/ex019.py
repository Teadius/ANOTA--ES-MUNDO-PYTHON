# Crie uma classe livro, que vai simular a passagem de pagina de uma livro.]
# Considerando tambem se o usuario chegou ao fum da leitura.
from time import sleep
from rich import print


class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1  
        print(
            f":book: [blue]Você acabou de abrir o livro[/] "
            f"[red]'{self.titulo}'[/] [blue]que tem[/] "
            f"[green]{self.paginas} páginas[/] [blue]no total.[/]"
        )
        print(
            f"[blue]Você agora está na página[/] [yellow]{self.pagina_atual}[/]\n"
            )


    def avancar_paginas(self, van):
        if self.pagina_atual >= self.paginas:
            print(
                f":closed_book: [red]Você já chegou ao fim do livro '{self.titulo}'![/]\n"
                )
            return
        paginas_avancadas = 0
        for _ in range(van):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                paginas_avancadas += 1
                print(
                    f"pág{self.pagina_atual} :arrow_forward: "
                    f"[blue]Você avançou[/] [green]{paginas_avancadas} páginas[/] "
                    f"[blue]e agora está na página[/] [yellow]{self.pagina_atual}[/]", end=" "
                    )
                sleep(0.2)
            else:
                break
            print()
            if self.pagina_atual == self.paginas:
                print(f":closed_book: [red]Você chegou ao fim do livro '{self.titulo}'![/]")
            print()


l1 = Livro(titulo="10 coisas que aprendi", paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)