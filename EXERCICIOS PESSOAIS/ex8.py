num = [2, 5, 9, 1]
num[2] = 3

print(num)
num.append(7)
print(num)
num.sort(reverse=True)  
print(num)
print(f'Essa lista tem {len(num)} elementos')


num = [2, 5, 9, 1]
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')