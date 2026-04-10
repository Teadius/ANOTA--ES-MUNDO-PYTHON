km = float(input('digite a velocidade: '))

if km > 80:
    val = km - 80
    multa = 7.00 * val
    print('Voce foi multado por andar a {} KM'.format(km))
    print('sua multa foi de {} R$'.format(multa))

else:
    print('circulando')
