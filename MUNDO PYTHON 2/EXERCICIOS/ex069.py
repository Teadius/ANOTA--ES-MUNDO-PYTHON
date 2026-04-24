pm18 = homens = m20menos = 0
while True:
    print('=='*20)
    print('CADASTRE UMA PESSOA')
    print('=='*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    print('=='*20)
    if idade > 18:
        pm18 =+1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        m20menos += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print('=='*20)
print('Programa encerrado')
print(f'{pm18} pessoas tem mais de 18 anos.')
print(f'{homens} deles sao homens.')
print(f'{m20menos} são mulheres com menos de 20 anos.')
