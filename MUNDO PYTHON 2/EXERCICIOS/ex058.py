from random import randint
valor = randint(1, 100)
print('Sou seu computador... Acabei de pensar em um numero de 1 a 100... \n Sera que voce consegue adivinhar?')
count = 0
loop = False
while not loop:
    escolha = int(input('adivinhe o numero de 1 a 100: '))
    count += 1
    if escolha == valor:
        print('voce acertou o valor e {}'.format(valor))
        print('voce tentou {} vezes'.format(count))
        loop = True
    else:
        if escolha < valor:
            print('Errado o valor e maior')
        else:
            print('Errado o valor e menor')

# i = False   while not i:   i = True 
# ou 
# while true:   break
