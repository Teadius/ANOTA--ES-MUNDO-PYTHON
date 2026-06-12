from datetime import datetime
dici = dict()
dici['nome'] = str(input('nome: '))
dici['Ano de nascimento: '] = int(input('ano de nascimento: '))
dici['ctps'] = int(input('carteira de trabalho: '))
dici['idade'] = datetime.now().year - dici['Ano de nascimento: ']
if dici['ctps'] != 0:
    dici['Ano de contratação: '] = int(input('ano de contratação: '))
    dici['Salário: '] = float(input('salário: '))
    dici['Aposentadoria: '] = dici['idade'] + ((dici['Ano de contratação: '] + 35) - datetime.now().year)
print('-='*30)
for k, v in dici.items():
    print(f'{k} {v}')
