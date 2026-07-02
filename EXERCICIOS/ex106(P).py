def sistema():
    while True:
        print('\033[0;30;42m-\033[m'*40)
        print(f'{"\033[0;30;42m SISTEMA DE AJUDA PYHELP\033 ]m":^40}')
        print('\033[0;30;42m-\033[m'*40)
        # '\033[0;30;42m   x    \033[m'
        fun = str(input('Função ou blibioteca > ')).strip()
        if fun == 'fim':
            print(f'{"Ate logo":^40}')
            break
        help(fun)


sistema()
# '\033[0;33;44m   <onde fica o texo>    \033[m' 
