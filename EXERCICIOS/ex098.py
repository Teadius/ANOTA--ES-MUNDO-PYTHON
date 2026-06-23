from time import sleep


def linha():
    print('-='*30)


def contagem(inicio, fim, passos):
    linha()
    if passos == 0:
        passos = 1
    if passos < 0:
        passos = abs(passos)
    print(f'Contagem de {inicio} até {fim} de {passos} em {passos}')
    sleep(0.5)
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count} ',end='', flush=True)
            sleep(0.5)
            count += passos
        print("FIM!")
    else:
        count = inicio
        while count >= fim:
            print(f'{count} ',end='', flush=True)
            sleep(0.5)
            count -= passos
        print('FIM!')
    linha()


contagem(1, 10, 1)
contagem(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('inicio: '))
f = int(input('Final: '))
p = int(input('Passos: '))
contagem(inicio=i,fim=f,passos=p)
