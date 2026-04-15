print('para caucular se seu emprestimo sera aprovado para compra da casa: ')

valor_casa = float(input('digite o valor da casa: '))
salario = float(input('digite seu salario: '))



if (1.10 * valor_casa) / 12 > salario * 0.30:
    print('nao sera possivel efetuar o emprestimo')
    print('valro da casa: {}'.format(valor_casa))
    print('salario do cliente: {}'.format(salario))
    print('valor necessario mensalmente: {}'.format((1.10 * valor_casa) / 12))
elif (1.10*valor_casa) / 12 <= salario * 0.30:
    print('sera possivel efetuar o emprestimo')
    print('valro da casa: {}'.format(valor_casa))
    print('salario do cliente: {}'.format(salario))
    print('valor necessario mensalmente: {}'.format((1.10 * valor_casa) / 12))
else:
    print('houve um erro')
