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
        if resp in 'SN' and resp != '':
            break
        print('Erro! Resposta inválida.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    print(f'{v["jogador"]:<15}', end='')
    print(f'{str(v["gols"]):<15}', end='')
    print(f'{str(v["total"]):<15}')
print('-' * 50)
while True:
    busca = int(input('Mostrar o dado de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'Erro, não existe jogador com o código {busca} na lista.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 50)
print('<< Volte sempre! >>')