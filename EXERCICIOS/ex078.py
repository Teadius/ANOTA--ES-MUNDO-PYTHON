'''
lista = []
maior = 0
menor = float('inf')
for i in range(0, 5):
    numero = int(input(f'Digite um valor para a Posição {i}: '))
    lista.append(numero)
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('=-'*40)
print(f'você digitou os valores [{lista}]')
indmaior = [i for i, v in enumerate(lista) if v == maior]
indmenor = [i for i, v in enumerate(lista) if v == menor]
print(f'O maior valor digitado foi {maior} nas posições {indmaior}')
print(f'O menor valor digitado foi {menor} nas posições {indmenor}')
'''


listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai =listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posiçõse ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
