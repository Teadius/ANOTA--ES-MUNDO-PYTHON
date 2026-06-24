from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    if len(num) > 0:
        mai = 0
        for i in range(0, len(num)):
            print(f'{num[i]} ',end='', flush=True)
            sleep(0.5)
            if num[i] > mai:
                mai = num[i]
        print()
        print(f'Forma informados {len(num)} valores ao todo.')
        print(f'O maior valor e {mai}. ')
    else:
        print('Nenhum valor foi informado')
    print('-='*30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()