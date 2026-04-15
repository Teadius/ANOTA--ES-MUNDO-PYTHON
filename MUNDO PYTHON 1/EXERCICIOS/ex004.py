algo = input('digite algo: ')

print('algo é \n {:=^20}'.format(algo))

print('o tipo primitivo desse valor é {}'.format(type(algo)))
print('só tem espaços? {}'.format(algo.isspace()))
print('é um numero? {}'.format(algo.isnumeric()))
print('é alfabetico? {}'.format(algo.isalpha()))
print('é alfanumerico? {}'.format(algo.isalnum()))
print('está em maiusculo? {}'.format(algo.isupper()))
print('está em minusculo? {}'.format(algo.islower()))
print('está capitalizada? {}'.format(algo.istitle()))
