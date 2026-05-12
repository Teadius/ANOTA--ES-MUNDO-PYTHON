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
