galera = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    if pessoa['sexo'] not in 'MF':
        print('Erro! Por favor, digite apenas M ou F para o sexo.')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    con = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while con not in 'SN':
        print('Erro! Por favor digite apenas S ou N para continaur.')
        con = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if con == 'N':
        break

print('-='*30)
print(galera)
print('-='*30)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = (sum(pessoa['idade'] for p in galera)) / len(galera)

print(f'B) A media de idade é de {media:.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('D) Lista das pessoa que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')
