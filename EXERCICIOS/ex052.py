num = int(input('digite um numero: '))
mult = 0

for i in range(1, num + 1):
    if num % i == 0:
        mult += 1

if mult == 2:
    print('{} é um numero primo'.format(num))
else:
    print('{} não e um numero primo'.format(num))
