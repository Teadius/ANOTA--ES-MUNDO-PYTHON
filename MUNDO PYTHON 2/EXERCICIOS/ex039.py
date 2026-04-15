from datetime import date

ano_a = date.today().year
ano_n = int(input('digite o ano de nacimento'))

idade = ano_a - ano_n

if idade < 18:
    print('ainda vai se alistar')
elif idade == 18:
    print('hora de se alistar')
elif idade > 18:
    print('passou do tempo de se alistar')
else:
    ('')
