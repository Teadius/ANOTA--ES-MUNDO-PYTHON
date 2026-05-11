# como trabalhar com cores no termminal

# e feito com codigo ANSI, e o codigo composto pór style,
# text e back.
# style e o estilo da letra
# text e a cor da letra
# back e a cor do fundo

print('\033[1;30;41mOlá, Mundo!\033[m')


# '\033[0;33;44m   <onde fica o texo>    \033[m'

# style
# 0 none
# 1 bold
# 4 underline
# 7 negative

# text
# 30 branco
# 31 vermelho
# 32 verde
# 33 amarelo
# 34 azul
# 35 roxo
# 36 cyan
# 37 cinza

# back
# 40 branco
# 41 vermelho
# 42 verde
# 43 amarelo
# 44 azul
# 45 roxo
# 46 cyan
# 47 cinza

print('\033[0;30;41m teste \033[m')
print('\033[4;33;44m teste \033[m')
print('\033[1;35;43m teste \033[m')
print('\033[30;42m teste \033[m')
print('\033[m teste \033[m')
print('\033[7;30m teste \033[m')
