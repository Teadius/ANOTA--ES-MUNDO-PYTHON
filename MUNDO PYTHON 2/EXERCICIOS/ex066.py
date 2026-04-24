soma = count = 0
while True:
    numero = int(input('digite um valor: '))
    soma = soma + numero
    count += 1
    if numero == 999:
        break
print('--'*20)
print('programa encerrado')
print(f'A soma dos valores e {soma-999}.')
print(f'Voce digitou {count-1} valores.')
