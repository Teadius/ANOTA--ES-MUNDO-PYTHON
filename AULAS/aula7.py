# Operadores Aritméticos

print('5 + 2 = {}'.format(float(5+2)))
print('5 - 2 = {}'.format(float(5-2)))
print('5 * 2 = {}'.format(float(5*2)))
print('5 / 2 = {}'.format(float(5/2)))

print('5 ** 2 = {}'.format(float(5**2))) #potenciação
print('5 // 2 = {}'.format(float(5//2))) #divisão inteira
print('5 % 2 = {}'.format(float(5%2))) #resto da divisão

print()
print('=='*20)
print()

# Ordem de Precedência
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

# Exemplo:
print('3 * 5 + 4 ** 2 =?')
a = 3 * 5
b = 4 ** 2
print('3 * 5 = {}'.format(int(a)))
print('4 ** 2 = {}'.format(int(b)))
print('15 + 16 = {}'.format(int(a+b)))
print(3 * 5 + 4 ** 2)

# o \n continua na proxima linha
nome = input('Digite seu nome:\n  ')
print('Olá, {:=^20}!'.format(nome))
