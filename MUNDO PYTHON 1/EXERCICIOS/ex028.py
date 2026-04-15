import random

while True:
    random_numero = int(random.randint(1, 5))

    desvio = int(input('qual numero de 1 a 5 voce acha que foi sortiado? '))

    if desvio == random_numero:
        print('voce acertou o numero e {}'.format(random_numero))
        print()
    else:
        print('voce errou o numero e {}'.format(random_numero))
        print()
