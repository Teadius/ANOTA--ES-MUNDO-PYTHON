# Varieaveis compostas (Dicionarios)
# Dicionarios são estrurtuars de dados que armazenam pares de 
# chave e valor.
# escrecvese assim:
dicionario = dict()
dicionario = {
    'nome': 'pedro',
    'idade': 25
    }
print(dicionario['nome'])
print(dicionario['idade'])



# lembra muito uma lista onde o indice é a chave e o valor 
# é o valor do indice, mas a diferença é que a chave pode
# ser qualquer tipo de dado.



# para addicionar um elemento basta usar:
dicionario['sexo'] = 'masculino'
print(dicionario)
# para remover um elemento basta usar:
del dicionario['sexo']
print(dicionario)
print('\n\n\n')



filme = {
    'titulo': 'star wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values()) # retorna os valores do dicionario
print(filme.keys()) # retorna as chaves do dicionario
print(filme.items()) # retorna os pares de chave e valor do dicionario

for k, v in filme.items():
    print(f'O {k} é : {v}')
print('\n\n\n')



filmes = [
    {
    'titulo': 'star wars',
    'ano': 1977,
    'diretor': 'George Lucas'
    },
    {
    'titulo': 'avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
    },
    {
    'titulo': 'matrix',
    'ano': 1999,
    'diretor': 'Lana Wachowski'
    },
]

for filme in filmes:
    for k, v in filme.items():
        print(f'O {k} é : {v}')
