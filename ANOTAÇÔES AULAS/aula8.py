import math # importação na primeira linha do código

# Em python e possivel importar bibliotecas
# para isso usamos a palavra reservada import
# import math
# para importar apenas uma função da biblioteca usamos from
# from math import sqrt
# para importar todas as funções da biblioteca usamos o *
# from math import *

# na biblioteca math tem a varias função como:
# ceil que arredonda o numero para cima
# floor arredonda para baixo
# trunc arredonda para baixo, mas sem arredondar o numero
# pow para calcular a potencia de um numero
# sqrt para calcular a raiz quadrada de um numero
# factorial para calcular o fatorial de um numero
# hypot caucula a hipotenusa

num = float(input('digite um numero: '))

raiz = math.sqrt(num)
raiz_semmath = num ** (1/2)

print('o numero arredondado para cima é: {}'.format(math.ceil(num)))
print('o numero arredondado para baixo é: {}'.format(math.floor(num)))
print('a raiz de {} e igual a {}'.format(num, raiz))
print('a raiz de {} e igual a {}'.format(num, raiz_semmath))

# variavel
variavel = 1

# vetor
vetor = [1,0,2,4,5,6,7,7]

# matriz
matriz = {
    [1,2,3],
    [4,5,6]
    [7,8,9]
    }
