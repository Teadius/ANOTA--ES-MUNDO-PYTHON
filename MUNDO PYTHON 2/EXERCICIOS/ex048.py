soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        soma = soma + i
print('A soma de todos os valores e = {}'.format(soma))
