num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'ceis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Escolha um numero de 1 a 20: '))
    if 0 <= escolha <= 20:
        break
print(f'voce digitou o numero {num[escolha]}')
