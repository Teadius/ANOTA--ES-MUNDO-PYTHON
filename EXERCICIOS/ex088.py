from random import randint
from time import sleep

print('--'*20)
print(f'{"Jogar na mega sena":^40}')
print('--'*20)

numjogos = int(input('quantos jogos voce que sortear? '))
print(f'\n{" Sorteando os jogos... ":=^40}\n')

for jogo in range(1, numjogos + 1):
    lista_numeros = []

    while len(lista_numeros) < 6:
        rand = randint(1, 60)
        if rand not in lista_numeros:
            lista_numeros.append(rand)

    lista_numeros.sort()

    sleep(0.5)
    print(f'jogos {jogo}: {lista_numeros}')

print('\n' + '--' * 20)
print(f'{"Boa sorte!":^40}')
print('--' * 20)
