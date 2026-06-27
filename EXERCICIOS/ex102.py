def fatorial(num, show=False):
    '''
    Caucula o fatorial de um numero.
    :param num: O número a ser cauculado.
    :param show: (opcional) Mostra ou não a conta na tela.
    return: O valor do fatorial de num.
    '''
    print('-'*40)
    f = 1
    for c in range(num, 0, -1):
        f *= c 
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


valor = int(input('Digite um valor para ver seu fatorial: '))
while True:
    show = str(input('Deseja ver a conta? [S/N] ')).strip().upper()
    if show in 'SN':
        break
    print('valor invalido')
if show == 'S':
    show = True
if show == 'N':
    show = False
print(fatorial(valor, show))