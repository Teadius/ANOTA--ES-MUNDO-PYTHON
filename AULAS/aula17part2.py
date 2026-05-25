
# Listas em Python
dados = list() # list() e [] são formas de criar listas python
dados.append('pedro')
dados.append(25)
print(dados[0])
print(dados[1])

print('-='*40)

pessoas = list()
pessoas.append(dados[:])
print(f'{pessoas}')
# copia dados para pessoas, então pessoas recebe uma copia 

print('-='*40)

# listas compostas
# ou seja listas dentro de listas
pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
print(pessoas[0][0], end='  ') # pedro
print(pessoas[0][1]) # 25
print(pessoas[1][0], end='  ') # maria
print(pessoas[1][1]) # 19   
print(pessoas[2][0], end='  ') # joao
print(pessoas[2][1]) # 32

print(pessoas[1]) # ['maria', 19]
