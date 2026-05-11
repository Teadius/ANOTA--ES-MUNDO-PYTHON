lista = []
maior = 0
menor = float('inf')
for i in range(0, 5):
    numero = int(input(f'Digite um valor para a Posição {i}: '))
    lista.append(numero)
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('=-'*40)
print(f'você digitou os valores [{lista}]')
indmaior = [i for i, v in enumerate(lista) if v == maior]
indmenor = [i for i, v in enumerate(lista) if v == menor]
print(f'O maior valor digitado foi {maior} nas posições {indmaior}')
print(f'O menor valor digitado foi {menor} nas posições {indmenor}')
