import random
count = 0
while True:
    print('O computador ira escolher um numero para jogar par ou impar')
    jogadorpi = str(input('escolha entre [1]par e [2]inpar: '))
    print('--'*20)
    pc = random.randint(0, 10)
    jogadornum = int(input('escolha um numero de 0 a 10: '))
    print(f'o computador escolheu {pc}')
    if (jogadornum + pc) % 2 == 0:
        if jogadorpi == '1':
            print(f'voce venceu, o valor e par {jogadornum + pc}')
            count += 1
        else:
            print(f'voce perdeu o valor e impar {jogadornum + pc}')
            break
    else:
        if jogadorpi == '1':
            print(f'voce perdeu o valor e impar {jogadornum + pc}')
            break
        else:
            print(f'voce venceu o valor e impar {jogadornum + pc}')
            count += 1
    print('--'*20)
print('--'*20)
print(f'voce venceu {count} vezes')
print('fim de jogo')
print('--'*20)
