lista = []
count = 0
while True:
    num = int(input('Digite um valor: '))
    count += 1
    lista.append(num)
    con = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if con == 'S':
        print('programa continuado')
    elif con == 'N':
        print('programa encerrado')
        break
    else:
        print('valor invalido')
decrecente = sorted(lista, reverse=True)
print(f'Voce digitou {count} elementos')
print(f'Os valores em ordem decrecente são {decrecente}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista')
