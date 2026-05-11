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
