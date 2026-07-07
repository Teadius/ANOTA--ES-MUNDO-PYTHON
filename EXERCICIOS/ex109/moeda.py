def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)

def dobro(preco=0, formato=False):
    return preco * 2 if not formato else moeda(preco * 2)

def metade(preco=0, formato=False):
    return preco / 2 if not formato else moeda(preco / 2)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>0.2f}'.replace('.', ',')