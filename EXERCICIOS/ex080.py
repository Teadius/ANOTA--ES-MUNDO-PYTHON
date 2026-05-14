'''lista = []

for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    lista.append(valor)

n = len(lista)

for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f'Lista ordenada: {lista}')
'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
