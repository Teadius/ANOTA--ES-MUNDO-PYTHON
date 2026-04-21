
while True:
    valor = str(input('Escolha um sexo [M/F]: ')).upper()
    if valor == 'M':
        print('voce escolheu homen')
        break
    elif valor == 'F':
        print('voce escolheu mulher')
        break
    else:
        print('valor invalido, digite um valor correto por favor')
print('fim do programa')