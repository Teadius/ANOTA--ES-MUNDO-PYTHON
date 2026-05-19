num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))  
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*40)
sor = num.sort()
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares e {impares}')
