ValorI = int(input('digite um valor para ver seu fatorial: '))
Valor = ValorI
count = Valor

while count != 1:
    print('{} x {} = {}'.format(Valor, count, Valor * (count - 1)))
    Valor = Valor * (count - 1)
    count -= 1
print('{}! = {}'.format(ValorI, Valor))

'''
Simplificação de 4 linhas com math.factorial

from math import factorial
n = int(input('Digite um valor numerico para caucular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} e {}'format(n, f))
'''
