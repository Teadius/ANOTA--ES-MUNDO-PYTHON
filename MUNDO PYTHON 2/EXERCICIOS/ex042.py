a = int(input('digite a reta a: '))
b = int(input('digite a reta b: '))
c = int(input('digite a reta c: '))

if c < a + b and a < b + c and b < a + c:
    print('e um triangulo')
    if a == b == c:
        print('triangulo equilatero')
    elif a == b != c or a == c != b or b == c != a:
        print('triangulo isoceles')
    elif a != b != c:
        print('triangulo escaleno')
else:
    print('nao e um triangulo')
