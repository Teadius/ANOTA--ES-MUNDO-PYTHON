aluno = dict()
aluno['nome'] = str(input('Digite seu nome: ')).strip()
aluno['media'] = float(input('Digite sua média: '))
if aluno['media'] >= 7:
    aluno['estado'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['estado'] = 'recuperação'
else:
    aluno['estado'] = 'reprovado'
print('-' * 30)
for chave, valor in aluno.items():
    print(f'- {chave} é igual a {valor}')

# O dicionario e definido como aluno =  dict() de forma aberta 
# seus valores são definidos por "nome" e "media" e "estado" onde o nome é definido pelo usuario
# o for c, v in aluno.items() é usado para imprimir os valores do dicionario onde c é a chave e v é o valor da chave.
# .items() celeciona todos os itens do dicionario
