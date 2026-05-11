num = int(input('quantos termos voce que ver da sequencia de fibonacci: '))
t1 = 0
t2 = 1
cont = 1
while cont <= num:
    print('{}'.format(t1), end=' → ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
print('\n FIM')

