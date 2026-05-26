'''
nome_pessoas = []
peso_pessoas = []
totpessoas = 0
maiorp = 0
menorp = float('inf')
lmaip = []
lmenp = []
while True:
    n = str(input('Nome: ')).strip()
    p = float(input('Peso: '))
    nome_pessoas.append(n)
    peso_pessoas.append(p)
    totpessoas += 1
    if p > maiorp:
        maiorp = p
        lmaip = [n]
    elif p == maiorp:
        lmaip.append(n)
    if p < menorp:
        menorp = p 
        lmenp = [n]
    elif p == menorp:
        lmenp.append(n)
    while True:
        loop = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if loop in ('S', 'N'):
            break
        print('Valor invalido! Digite apenas S ou N.')
    if loop == 'N':
        break
print('-='*40)
print(f'Ao todo você cadastou {totpessoas} pessoas.')
print(f'O maior peso foi de {maiorp} peso de {lmaip}')
print(f'O menor peso foi de {menorp} peso de {lmenp}')
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp in ('S', 'N'): # Uso correto do 'in' para checar a tupla
            break
        print('Valor inválido! Digite apenas S ou N.')
        
    if resp == 'N':
        break
print('-='*40)
print(f'Ao todo, você cadastrou {len(princ)} pessaos.')
print(f'O maior peso foi de {mai}Kg. peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
