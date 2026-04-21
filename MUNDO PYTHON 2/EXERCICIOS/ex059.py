n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))


while True:
    print('''Opções
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    print('')
    escolha = str(input('sua escolha: '))
    print('')
    if escolha == '1':
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif escolha == '2':
        print('{} X {} = {}'.format(n1, n2, n1 * n2))
    elif escolha == '3':
        if n1 > n2:
            print('{} e maior que {}'.format(n1, n2))
        else:
            print('{} e maior que {}'.format(n2, n1))
    elif escolha == '4':
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif escolha == '5':
        print('programa encerrado ')
        break
    else:
        print('valor invalido')
    print('')
