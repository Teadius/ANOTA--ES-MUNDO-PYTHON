c = (
    '\033[m',
    '\033[0;30;41m',
    '\033[0;30;42m',
    '\033[0;30;44m',
    '\033[7;30m',
)


def ajuda(com):
    '''Acessa o manual interativo do python aplicando a cor de fundo'''
    titulo(f'Acessando o manual do comando "{com}"', 3)
    print(c[4], end='')
    help(com)
    print(c[0],end='')

def titulo(msg, cor=0):
    '''Cria um vabeçalho personalizdo e colorido'''
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    print()
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'fim':
        break
    else:
        ajuda(comando)
print()
titulo('Até logo!', 1)