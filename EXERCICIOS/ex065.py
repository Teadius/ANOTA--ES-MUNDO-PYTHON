soma = maior = count = 0
menor = None
while True:
    opcao = str(input('[1]iniciar  [2]sair    '))
    if opcao == '1':
        print('programa iniciado digite um numero')
        while True:
            num = float(input('digite um valor ou [0] para sair: '))
            if num == 0:
                break
            count += 1
            soma += num
            if menor is None or num < menor:
                menor = num
            if num > maior:
                maior = num
            media = soma / count
            print('A media ate agora e {}'.format(media))
            print('O maior numero ate agora e {}'.format(maior))
            print('O menor numero ate agora e {}'.format(menor))
    elif opcao == '2':
        print('programa finalizado')
    else:
        print('valor invalido')
