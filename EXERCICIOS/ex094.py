# codigo resolvido
'''galera = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    if pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F para o sexo.')
        pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    con = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while con not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N para continuar.')
        con = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if con == 'N':
        break
print('-=' * 30)
print(galera)
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
soma = sum(p['idade'] for p in galera)
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')
'''
