matriz = [[0,0,0],[0,0,0],[0,0,0]]
#      = [[0] * 3 for x in range(3)]
for linha in range(3):
    for coluna in range(3): 
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}], [{coluna}]: '))
print('-='*40)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
