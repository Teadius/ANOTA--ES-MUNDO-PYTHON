lista = []

while True:
    valor = (int(input('Digite um valor numerico: ')))
    if valor in lista:
        print('valor ja existe na lista')
    elif valor not in lista:
        lista.append(valor)
        print('valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
lista.sort()
print(f'lista:\n {lista}')
print('programa finalizado')
