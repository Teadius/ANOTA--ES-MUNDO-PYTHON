'''termo = int(input('digite um valor do termo: '))
razao = termo
for i in range(0, 10, 1):
    print(termo)
    termo = termo + razao'''

termo = int(input("digite o valor do termo: "))
razao = termo
count = 0
while count < 10:
    print(('{} →').format(termo), end='')
    termo = termo + razao
    count += 1
print('fim')