# Laço de repetição while

# while significa enquanto, ou seja, ele executa um blobo de 
# codigo ate que uma condicao nao seja correspondente.

a = 1
while a < 11:
    print('a = {}'.format(a))
    a += 1

# pode usar tanto o for quanto o while, porem quando nao se 
# sabe o final do loop usase somente o while.

r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('quer continuar? [S/N]: ')).upper()
print('fim')
