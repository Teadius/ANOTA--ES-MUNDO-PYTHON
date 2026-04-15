dia = float(input('quantos dias o carro rodou? '))
km = float(input('quantos km o carro rodou neste periodo? '))

aluguel = (dia * 60) + (km * 0.15)

print('o aluguel ficou: {}'.format(aluguel))
