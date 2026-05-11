maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}'.format(maior))
print('O menor peso lido foi de {}'.format(menor))
