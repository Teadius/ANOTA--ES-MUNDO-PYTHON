from time import sleep
from random import choice

def sorteando(*num):
    lista = list()
    print(f'Sorteando {len(num)} valores da lista: ', end='', flush=True)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        lista.append(valor)
    print('Pronto!')
    sorte = choice(lista)
    print(f'Sorteando os valores pares de {lista}, temos {sorte}')

sorteando(5, 7, 9, 2, 4)