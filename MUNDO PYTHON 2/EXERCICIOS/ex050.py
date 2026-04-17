soma = 0 

for i in range(1, 7):
    num = int(input('digite o {} valor: '.format(i)))
    if num % 2 == 0:
        soma += num
print('a soma dos pares e {}'.format(soma))
