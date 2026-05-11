from datetime import date
atual = date.today().year
totmaior = 0 
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('em que ano a {} pessao naceu'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo tivemos {} pessoaas maiores de idade'. format(totmaior))
print('e tivemos {} pessaos menores de idade'.format(totmenor))
