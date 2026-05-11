print('digite uma frase para ver se e um palindromo')
frase = str(input('R: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
print('voce digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('É um palindromo')
else:
    print('Não e um palindromo')
