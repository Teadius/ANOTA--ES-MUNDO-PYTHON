a = int(input('digite a reta a: '))
b = int(input('digite a reta b: '))
c = int(input('digite a reta c: '))

if c < a + b and a < b + c and b < a + c:
    print('e um triangulo')
else:
    print('nao e um triangulo')
