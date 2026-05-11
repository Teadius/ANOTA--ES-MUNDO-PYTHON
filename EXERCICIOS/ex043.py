peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('abaixo do peso')
elif imc <=25:
    print('peso ideal')
elif imc <=30:
    print('sobrepeso')
elif imc <= 40:
    print('obesidadede')
else:
    print('obesidade morbida')
