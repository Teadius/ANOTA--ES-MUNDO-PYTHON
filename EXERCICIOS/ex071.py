print('=='*30)
print('{:^30}'.format('Banco CEV'))
print('=='*30)
saque = int(input('Que valor voce que sacar? R$'))

total = saque
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!') 

'''
r50 = saque // 50
resto = saque % 50

r20 = resto // 20
resto %= 20
r10 = resto // 10
resto %= 10
r1 = resto // 1

print(f'Total de {r50} cedulas de R$50')
print(f'Total de {r20} cedulas de R$20')
print(f'Total de {r10} cedulas de R$10')
print(f'Total de {r1} cedulas de R$1')
print('=='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
