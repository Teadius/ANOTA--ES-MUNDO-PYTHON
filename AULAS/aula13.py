# Exxtruturas de repetição for

# laços de repetição sao condiçoes que rodam um bloco de codigo emquanto
# houverem condiçoes para cumprir.
n = 1
# for significa para
# i e uma variavel de controle
# in range() significa dentro de range de 0 a 10

# para variavel de controle dentro de area(de 0, a 10, lendo de 1 em 1)
#             (começo, fim, passos)
for i in range(0,10, 1):
    if n == 1 or n == 3:
        print('frase {} legal'.format(n))
        n += 1
    elif n == 10:
        print('frase final {}'.format(n))
    else:
        print('frase {}'.format(n))
        n += 1