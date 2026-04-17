somaidade = 0
mediaidade = 0
maiordadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('pessoa {}'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maiordadehomen = idade
        nomevelho = nome
    if sexo in 'M' and idade > maiordadehomen:
        maiordadehomen = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de iadade do grupo e {} anos'.format(mediaidade))
print('O hoemen mais velho tem {} anos'.format(maiordadehomen, nomevelho))
print('ao todo {} mulheres tem menos de 20 anos'.format(totmulher20))
