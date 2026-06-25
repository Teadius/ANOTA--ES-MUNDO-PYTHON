from random import choice, randint
from time import sleep


def sorteando(num):
    lista = list()
    print(f'Sorteando {len(num)} valores da lista: ', end='', flush=True)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        lista.append(valor)
    print('Pronto!')
    sorte = choice(lista)
    print(f'Sorteando os valores pares de {lista}, temos {sorte}')


valores = list()
for cont in range(0, 5):
    valores.append(randint(1,10))
sorteando(valores)