numero = int(input('digite um numero: '))

escolha = input('escolha entre (1)binario, (2)octal, (3)hexadecimal: ')



if escolha == '1':
    print('o numero {} em binario fica: {}'.format(numero, bin(numero)))
elif escolha == '2':
    print('o nuemro {} em octal fica: {}'.format(numero, oct(numero)) )
elif escolha == '3':
    print('o nuemro {} em hexadeciamal fica: {}'.format(numero, hex(numero)))
else:
    print('valor invalido')
    
print('')
print('o numero {} em binario fica: {}'.format(numero, bin(numero)))
print('o nuemro {} em octal fica: {}'.format(numero, oct(numero)) )
print('o nuemro {} em hexadeciamal fica: {}'.format(numero, hex(numero)))
