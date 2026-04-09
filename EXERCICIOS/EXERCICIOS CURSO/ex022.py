nome = input('digite um nome: ').strip()
print("""
""")
print('O nome todo em maiusculo fica: {}'.format(nome.upper()))
print('O nome todo em minusculo fica: {}'.format(nome.lower()))
print('O nome sem espaços fica: {}'.format(len(nome.replace(" ", ""))))
print('O primeiro nome tem {} letras'.format(len(nome.split()[0])))
