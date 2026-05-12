# Listas 
# Diferente das tuplas, as listas são mutáveis
# Em python listas são escritas entre colchetes []

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(f'lista sem alterações:\n{lanche}')
lanche[1] = 'refrigerante'
print(f'lista com o indice 1 alterado:\n{lanche}')
print()

# Adicionar elementos novos a uma lista
lanche.append('cookie')
lanche.insert(0, 'cachorro quente')
print(f'lista com elementos adicionados(um ao final e um no indice 0):\n{lanche}')
print()

# Remover elementos de uma lista
del lanche[4]  # Remove o elemento no índice 4 (cookie)
print(f'lista após remoção de elemento no indice 4:\n{lanche}')
lanche.pop(3) # Remove o elemento no indice 3
print(f'lista após remoção de elemento no indice 3:\n{lanche}')
lanche.remove('cachorro quente') # Remove o elemento 'cachorro quente'
print(f'lista após remoção do elemento "cachorro quente":\n{lanche}')
if 'pizza' in lanche:
    lanche.remove('pizza') # Remove o elemento 'pizza' se ele existir na lista
print()

# Ordenar uma lista
valores = [8, 2, 5, 4, 9, 3, 0, 1, 7, 6]
print(f'lista de valores sem ordenação:\n{valores}')
valores = list(range(4, 11))
print(f'lista de valores sem ordenação:\n{valores}')
valores.sort()
print(f'lista de valores ordenada:\n{valores}')
print()
print(f'lista de lanche ordenada:\n{sorted(lanche)}')
print(f'len dos valores {len(valores)}')

# Enumerate 

fruta = ['maçã', 'banana', 'laranja', 'morango']

for indice, fruta in enumerate(fruta):
    print(f'{indice} - {fruta}')
    #infice 0   fruta (0)maçã
    #indice 1   fruta (1)banana
    #indice 2   fruta (2)laranja
    #indice 3   fruta (3)morango

# A função enumerate() em Python é uma ferramenta construída 
# (built-in) que permite percorrer uma sequência (como listas, 
# tuplas ou strings) e, simultaneamente, obter o índice (posição) 
# e o valor de cada elemento.

# A lógica principal é eliminar a necessidade de criar contadores 
# manuais (como i = 0 e i += 1) dentro de um loop for, tornando o 
# código mais limpo, legível e seguro (idiomático).
