ValorI = int(input('digite um valor para ver seu fatorial: '))
Valor = ValorI
count = Valor

while count != 1:
    print('{} * {} = {}'.format(Valor, count, Valor * (count - 1)))
    Valor = Valor * (count - 1)
    count -= 1
print('{}! = {}'.format(ValorI, Valor))