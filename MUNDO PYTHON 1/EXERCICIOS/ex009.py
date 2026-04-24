numero = int(input('digite um numero para ver a tabuada: '))

for i in range(1, 11):
    print('{} X {} = {}'.format(numero, i, numero*i))
