from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 10% temos {moeda.moeda(moeda.diminuir(p, 10))}')