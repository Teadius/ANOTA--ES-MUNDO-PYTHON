class Produto:
    def __init__(self, nome: str, preco: float = 0.0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({formata_dinheiro(self.preco)})"


class Carrinho:
    def __init__(self, produtos: list = None):
        self.produtos = list(produtos) if produtos else []

    @property
    def total(self) -> float:
        return sum(p.preco for p in self.produtos)

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho.")

    def __str__(self):
        itens = "\n".join(str(p) for p in self.produtos)
        return f"{itens}\n------------------------------\nTotal: {formata_dinheiro(self.total)}"

def formata_dinheiro(valor: float) -> str:
    import locale
    try:
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        return locale.currency(valor, grouping=True)
    except locale.Error:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

