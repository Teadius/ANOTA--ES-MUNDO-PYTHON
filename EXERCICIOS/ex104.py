def leiaInt(msg):
    while True:
        dado = str(input(msg)).strip()
        if dado.isnumeric():
            return int(dado)
        else:
            print('\033[1;30;41mErro! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o númeor {n}')
