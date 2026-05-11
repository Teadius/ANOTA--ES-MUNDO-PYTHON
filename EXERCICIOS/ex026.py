frase = str(input('digite uma frase: ')).upper().strip()

print('a letra A aparece: {}'.format(frase.count('A')))
print('primeira vez que A aparece: {}'.format(frase.find('A')+1))
print('ultima vez que A aparece: {}'.format(frase.rfind('A')+1))
