# Variave simples
lanche = 'hamburguer'

# variaveis compostas 
# (tuplas) [listas] {dicionarios}
# tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# Regra: "Tuplas são imutaveis"
# EX: lanche[1] = 'refrigerante'
# Saida: Erro
# cada elemento e identificado por indices
# (0, 1, 2, 3, 4, 5, 6)
print(lanche[0])
print(lanche[1])
print(lanche[0:2])
print(lanche[-1])
print(len(lanche))
print(f'tuple em ordem: {sorted(lanche)}')
print('')

for c in lanche:
    print(f'Eu vou comer {c}')

print('')

for cout in range(0, len(lanche)):
    print(f'eu vou vomer {lanche[cout]} na posicao {cout}')

print('')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posicao {pos}')

print('')

a = (2, 5, 4)
b = (5, 8 , 1, 2)
c = b + a
print(c)
print('numero de termos em c',len(c))
print(f'numero de 5 escritos {c.count(5)}')
print(f'o 8 esta na posicao {c.index(8)}')

# del c 
# tupla deletada 
# obs: nao da para deletar um termo, mas da para deletar 
# a tupla inteira
