# Funções ou encapsulamento de código
# Em python funções são blocos de codigo que podem ser 
# reutilizados a qualquer momento.

# E podem ser chamndo em apenas uma linha com uma sintaxe simples
# por ecemplo a função print() é uma função que imprime na tela 
# o que for passado como parametro.

# E recomendavel por estetica deixar duas linhas em branco abaixo 
# da função.



# Funções sem parametros
def lin():
    print('-='*30)


lin()
print(f'{"CURSO EM VIDEO":>30}')
lin()



# Funções com parametros
def titulo(txt):
    print('-='*30)
    print(f'{txt:^30}')
    print('-='*30)


titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')



# O *args é usado para passar uma quantidade indeterminada de 
# parametros para uma função.
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 2)
contador(4, 4, 7, 9, 6)