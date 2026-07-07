from ex109 import moeda


p = float(input('Digite o preço: R$'))
formato = str(input('Quer formatar o preço? [S/N]: ')).strip().upper()
if formato == 'S':
    print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
    print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
    print(f'Aumentado 10% temos {moeda.aumentar(p, 10, True)}')
    print(f'Diminuindo em 10% temos {moeda.diminuir(p, 10, True)}')
else:
    print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p)}')
    print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p)}')
    print(f'Aumentado 10% temos {moeda.aumentar(p, 10)}')
    print(f'Diminuindo em 10% temos {moeda.diminuir(p, 10)}')