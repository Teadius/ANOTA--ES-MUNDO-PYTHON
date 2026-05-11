distancia = int(input('digite a distancaia da sua viaem em KM: '))

if distancia >= 200:
    passagem = 0.50 * distancia
    print('preço da passagem: {}'.format(passagem))
else:
    passagem = 0.45 * distancia
    print('preço da passagem: {}'.format(passagem))
