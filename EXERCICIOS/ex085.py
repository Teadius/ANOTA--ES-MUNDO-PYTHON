from math import *
valores = [[], []]
for i in range(1, 8):
    num = int(input('Digite o valor numero {i}: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print('-='*40)
print(f'Os valores pares foram: {valores[0]}')
print(f'Os valores inpares foram: {valores[1]}')
