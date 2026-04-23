num = 0
numcont = 0
numsum = num 
while num != 999:
    numsum += num 
    numcont += 1
    num = int(input('digite um valor que nao seja 999: '))
    if num == 999:
        print('fim do programa, voce digitou 999')
        break
    print('voce digitou o valor: {}'.format(num))
    print('a soma de todos os numeros e {}'.format(numsum))
    print('{} numeros foram digitados'.format(numcont))
