lista = []
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: ')) 
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])

    con = ''
    while con != 'SN':
        con = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if con in 'SN':
            break
    if con == 'N':
        break

print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--'*20)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-=' * 20)
