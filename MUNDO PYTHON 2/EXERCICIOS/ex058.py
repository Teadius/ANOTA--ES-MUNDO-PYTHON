import random

valor = random.randint(1, 100)
count = 0

while True:
    escolha = int(input('adivinhe o numero de 1 a 100: '))
    count += 1
    if escolha == valor:
        print('voce acertou o valor e {}'.format(valor))
        print('voce tentou {} vezes'.format(count))
        break
    else:
        if escolha < valor:
            print('Errado o valor e maior')
        else:
            print('Errado o valor e menor')
