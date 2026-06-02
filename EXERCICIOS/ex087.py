matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somaterceira = maiorsegunda = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}], [{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
print('-='*40)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma dos valores pares é: {somapar}')
for linha in range(0, 3):
    somaterceira += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {somaterceira}')
for coluna in range(0, 3):
    if coluna == 0:
        maiorsegunda = matriz[1][coluna]
    elif matriz[1][coluna] > maiorsegunda:
        maiorsegunda = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maiorsegunda}')
