data = int(input('digite o ano: '))
naci = int(input('digite o ano de nacimento'))

idade = data - naci

if idade <= 9: 
    print('mirin')
elif idade <= 14:
    print('infanto')
elif idade <= 19:
    print('junior')
elif idade == 20:
    print('senior')
elif idade > 20:
    print('master')
else:
    print('')
