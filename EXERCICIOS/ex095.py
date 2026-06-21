time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['jogador'] = str(input('Nome do jogador: ')).upper().strip()
    tot_partidas = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
    partidas.clear()
    for i in range(0, tot_partidas):
        partidas.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('Erro resposta invalida.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k,v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar o dado de qual jogador?'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro, não tem jogador com esse valor na lista.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('Volte sempre.')
