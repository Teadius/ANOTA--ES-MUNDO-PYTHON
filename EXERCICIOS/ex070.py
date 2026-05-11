print('=='*20)
print('LOJA SUPER BARATÂO')
print('=='*20)
soma = totmil = 0
menorp = float('inf')
nomemp = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = int(input('Preço: '))
    soma = soma + preço
    if preço >= 1000:
        totmil += 1
    if preço < menorp:
        menorp = preço
        nomemp = nome
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nomemp} que custa R${menorp}')
