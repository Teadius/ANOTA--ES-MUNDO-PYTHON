# Funções part 2

# interactive help,  
#help(): descreve o que a  função faz.
# O help() tambem pode ser usado no terminal pyhton, digitando  
# help() e depois o nome da função que deseja saber mais sobre
# incluindo extenções como math e depois exit para sair.
help(print)
print('')


# docstrings, 
# ex:
def contador(i, f, p):
    #docstring abaixo:
    """
    -> Faz uma contagem e mostra na tela. 
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do curso em video.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='', flush=True)
        c += p
    print('FIM!')
contador(2, 10, 2)

help(contador) # não ira especificar sem a docstring.
print('')


# Argumentos opcionais,
def  somar(a=0, b=0, c=0): # ao definir uma parametro como a=0 ele se torna opcional.
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4) # a variavel c não recebera valor
somar() # O valor e definido pelo que  esta no parametro
# O parametro pode ser definido com qualquer valor, inclusive string, lista, tupla, dicionario, etc.
# O valor opcional e usado quando não e informado nenhum valor.
print('')


# Escopo de variáveis,
# Escopo e o local onde uma variavel vai existir.
def  teste(b):
    a = 8 # variavel local, so existe dentro da função teste.
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5 # variavel global, existe em todo o programa.
teste(a)
print(f'A fora vale {a}')
print('')


def  teste(b):
    global a # variavel global, existe em todo o programa.
    a = 8 # variavel local, so existe dentro da função teste.
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5 # variavel global, existe em todo o programa.
teste(a)
print(f'A fora vale {a}')
print('')

# Retorno de resultados
#  return e usado para retornar valores de uma  função.
def somar(a=0, b=0, c=0): # ao definir uma parametro como a=0 ele se torna opcional.
    s = a + b + c
    return s # retorna o valor da soma que e uma variavel local.
print(f'A soma vale {somar(3, 2, 5)}')

