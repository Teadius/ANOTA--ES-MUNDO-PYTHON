soma = count = 0
while True:
    numero = int(input('Digite um valor(999 para parar): '))
    if numero == 999:
        break
    soma = soma + numero
    count += 1
print('--'*20)
print(f'A soma dos {count} valores e igual a {soma}')
