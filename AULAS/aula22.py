# Modulos e pacotes.

# Modularização: modularizar e o ato de construir modulos.
# Teve inicio na decada de 60 com o objetivo de tornar um 
# programa mais organizado e conciso. Ou seja dividir um 
# programa grande.

# foco em: dividir um programa grande 
#          auemnta a legibilidade
#          facilita a manutenção


# As funcionaldiades do codigo estão em uteis.py
import uteis


num = int(input('Digite um valor:  '))
print(f'O fatorial de {num} e {uteis.fatorial(num)}')
print(f'O dobro de {num} e {uteis.dobro(num)}')
print(f'O triplo de {num} e {uteis.triplo(num)}')


# pacotes: são conjunbtos de funções especificas dentero 
# de um inportação.

# EX: pacote uteis
# import uteis              = todo o pacote
# from uteis import datas   = importa so uma parte de uteis
# from uteis import cores   = importa somente as cores

from uteis import dobro


print(f'Dobro de {5} e igual a {dobro(5)}')


'''
Estrutura de Pastas: Módulos vs. Pacotes:

meu_projeto/
│
├── main.py                  # Programa principal que executa o código
│
├── uteis.py                 # EXEMPLO DE MÓDULO (Apenas um arquivo .py com várias funções)
│
└── pacote_uteis/            # EXEMPLO DE PACOTE (Diretório que agrupa vários módulos)
    ├── __init__.py          # Arquivo obrigatório para o Python reconhecer a pasta como pacote
    │
    ├── numeros.py           # Submódulo com funções de matemática (fatorial, dobro, triplo)
    ├── datas.py             # Submódulo com funções de data e hora
    └── cores.py             # Submódulo com códigos ou funções de cores para o terminal
'''


# num todo modulso são utilizados para tornar um codigo mais 
# organizado e menor, pacotes são para separar o codigo em outros 
# programas para importalos posteriormente sem ter que ocupar um 
# grande espaço com muitas funções.

# Ou seja modulos são basicamente funções para codigos 
# consideravelemte grandes, proem pacotes ja são para codigos 
# muito grandes que necessitam de muitas funções para estarem 
# funcioando.