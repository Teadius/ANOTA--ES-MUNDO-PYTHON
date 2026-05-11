valor = str(input('informe um sexo [M/F]: ')).strip().upper()[0]
while valor not in 'MmFf':
    valor = str(input('informe um sexo [M/F]: ')).strip().upper()[0]
    if valor == 'M':
        print('voce escolheu Masculino')
        break
    elif valor == 'F':
        print('voce escolheu Feminino')
        break
    else:
        print('valor invalido, digite um valor correto por favor')
print('fim do programa')
