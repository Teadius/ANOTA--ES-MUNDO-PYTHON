termo = int(input('Priemiro termo: '))
razao = termo
count = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while count <= 10:
        print('{} → '.format(termo), end='')
        termo += razao
        count += 1
    mais = int(input('quantas termos que ver a mais? '))
    count -= mais
print('fim    {} Termos usados'.format(count - 1))
