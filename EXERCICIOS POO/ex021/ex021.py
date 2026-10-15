from rich import print


class Caneta:

    def __init__(self, cor="azul"):
        # Limpa espaços e deixa em minúsculo
        cor_limpa = cor.strip().lower()

        # Mapeia números e nomes para a cor em inglês (para usar no rich)
        mapeamento = {
            "1": "blue",
            "azul": "blue",
            "2": "red",
            "vermelha": "red",
            "vermelho": "red",
            "3": "green",
            "verde": "green",
        }

        # Se não encontrar, define 'white' (ou 'default') como padrão
        self.cor = mapeamento.get(cor_limpa, "white")

    def escrever(self, frase):
        # Formatação nativa do rich, muito mais limpa e legível!
        print(f"[{self.cor}]{frase}[/]")


# --- Execução ---
cor_input = input(
    "Escolha a cor da caneta (1 - Azul, 2 - Vermelha, 3 - Verde): "
)
frase_input = input("Frase: ")

cx = Caneta(cor_input)
cx.escrever(frase_input)