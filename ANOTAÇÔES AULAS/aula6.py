#tipos primitivos

#int - numeros inteiros                   12
#float - numeros reais                    12.0
#str - texto                              'olá mundo'
#bool - booleano (verdadeiro ou falso)    True ou False
#True siginifica verdadeiro e False significa falso

a = int(input('digite um numero inteiro: '))
b = float(input('digite um numero real: '))
c = str(input('digite um texto: '))
d = bool(input('digite um valor booleano (verdadeiro ou falso): '))

print(f'o numero digitado foi: {a}')
print(f'o numero digitado foi: {b}')
print(f'o texto digitado foi: {c}')
if d == 'verdadeiro':
    d = True
    print(f'o valor booleano digitado foi: {d}')
else:
    d = False
    print(f'o valor booleano digitado foi: {d}')



#formas de usar print
valor = 1
valor2 = 2

print('o valor ', int(valor), 'mais', int(valor2), 'e igual a: ', int(valor) + int(valor2)) #forma 1
print('o valor ', valor, ' mais ', valor2, ' e igual a:', {valor + valor2}) #forma 2

print(f'o valor é {valor}!') #forma 3

print('o valor é {}!'.format(valor)) #forma 4
print('o valor {} mais {} e igual a: {}'.format(valor, valor2, valor + valor2)) 

print(type(valor), type(valor2)) #mostra o tipo dos valores
print(valor.isnumeric()) #verifica se o valor é numerico
print(valor.isalpha()) #verifica se o valor é alfabetico
print(valor.isalnum()) #verifica se o valor é alfanumerico
print(valor.isupper()) #verifica se o valor é maiusculo
print(valor.islower()) #verifica se o valor é minusculo
