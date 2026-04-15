numero1 = int(input('digite o numero 1: '))
numero2 = int(input('digite o numero 2: '))

if numero1 == numero2:
    print('{} e {}, sao iguais'.format(numero1, numero2))
elif numero1 > numero2:
    print('O {} é maior que {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('o {} é maior que {}'.format(numero2, numero1))
else:
    print('valores invalidos')
