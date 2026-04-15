# Condicoes aninhadas 
# uma condicao dentro de outra condicao

nome = str(input('Qual seu nome? '))
if nome == 'gustavo':
    print('que nome legal')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome e bem popular no brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('belo nome feminino')
else:
    print('{}, que nome legal'.format(nome))

print('Tenha um bom dia, {}'.format(nome))
