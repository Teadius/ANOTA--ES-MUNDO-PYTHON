while True:
    numero = int(input('digite um valor para ver sua tabuada: '))
    print('--'*20)
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')
    print('--'*20)
print('programa encerrado')
