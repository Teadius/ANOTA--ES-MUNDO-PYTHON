lista = [[], [], []]
while True:
    esc = int(input('escolha um slot [0, 1, 2, (-1 sair)]: '))
    if esc == 0:
        n = int(input('Digite o valor a ser guardado: '))
        lista[0].append(n)
    elif esc == 1:
        n = int(input('Digite o valor a ser guardado: '))
        lista[1].append(n)
    elif esc == 2:
        n = int(input('Digite o valor a ser guardado: '))
        lista[2].append(n)
    elif esc == -1:
        print('Programa finalizado')
        break
    else:
        print('valor invalido, tente novamente')
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('Resposta invalida, tente novamente')
print(f'Os valores guardados foram: \n{lista}')
