i = int(input('Digite um número para ser dividido: '))
n = int(input('Digite um número para ser divisor: '))
try:
    print(f'O resultado de {i} dividido por {n} é {i/n}')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
