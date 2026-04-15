preco = float(input('digite o valor do produto: '))
print('forma de pagamento: \n(1)dinheiro/cheque\n(2)cartao\n(3)2x cartao\n(4)3x no cartao')
forma = str(input('escolha a forma de pagamento: '))

if forma == '1':
    print('total a pagar {}'.format(preco * 0.90))
elif forma == '2':
    print('total a pagar {}'.format(preco * 0.95))
elif forma == '3':
    print('total a pagar {}'.format(preco))
    print('2x de {}'.format(preco / 2))
elif forma == '4':
    print('total a pagar {}'.format(preco * 1.20))
    print('3x de {}'.format((preco * 1.20) / 3))
else:
    print('valor invalido')
