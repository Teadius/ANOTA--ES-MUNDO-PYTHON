galera = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) # copia os dados para a lista galera
    dados.clear() # limpa a lista dados para receber novos dados

print(galera)
escolha = int(input('Digite o numero do indice da pessoa que deseja acessar: '))

if escolha < len(galera):
    print(f'Voce escolheu acessar o indice {escolha} da lista galera, que corresponde a {galera[escolha]}')
else:
    print(f'indice {escolha} invalido')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
