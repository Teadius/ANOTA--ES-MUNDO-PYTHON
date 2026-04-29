tuples = (int(input('digite um numero: ')),
        int(input('digite um numero: ')),
        int(input('digite um numero: ')),
        int(input('digite um numero: ')),)

print(tuples)
print(f'o numero 9 aparece {tuples.count(9)}')
if 3 in tuples:
    print(f'o numero 3 aparece pela primeir vez na posicao {tuples.index(3)+1}')
else:
    print('o valor 3 nao foi digitado em nenhuma posicao')
print(f'os numero pares foram: {[n for n in tuples if n % 2 == 0]}')
