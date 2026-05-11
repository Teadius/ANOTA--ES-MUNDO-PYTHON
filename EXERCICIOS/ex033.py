n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))
n3 = int(input('digite um numero'))

if n1 > n2 and n1 > n3:
    print('o numero {} e o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('o numero {} e o maior'.format(n2))
elif n3 > n1 and n3 > n2:
    print('o numero {} e o maior'.format(n3))
else: 
    print('valor invalido')

if n1 < n2 and n1 < n3:
    print('o numero {} e o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('o numero {} e o menor'.format(n2))
elif n3 < n1 and n3 < n2:
    print('o numero {} e o menor'.format(n3))
else: 
    print('valor invalido')
