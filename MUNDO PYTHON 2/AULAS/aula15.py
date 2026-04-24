# Como parar loops while 

# A palavra reservada break para o loop de onde ele estiver 
# ele nao escrevera o resto do bloco dentro do while ele ira para fora

count = 1
while True:
    if count > 10:
        break
    print(f'loop {count}')
    print('loop {}'.format(count))
    print('')
    count += 1

'''
print(f'o valor e {valor}') # f string do python 3.6+
print('o valor e {}'.format(valor)) # .format do python 3
print('o valor e %d' % (valor)) # % do python 2
'''