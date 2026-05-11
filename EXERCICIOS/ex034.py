salario = float(input('digite seu salario: '))

if salario >= 1250.00:
    salario = salario * 1.10
    print('o almento foi de {}'.format(salario))
else:
    salario = salario * 1.15
    print('o almento foi de {}'.format(salario))
