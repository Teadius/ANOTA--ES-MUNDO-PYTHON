d = dict()
gols = list()
d['jogador'] = str(input('Nome do jogador: ')).upper().strip()
tot_partidas = int(input(f'Quantas partidas {d["jogador"]} jogou? '))
for i in range(0, tot_partidas):
    gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
d['gols'] = gols
d['total'] = sum(gols)
print('-=' * 20)
print(d)  
print('-=' * 20)
print(f'O campo jogador tem o valor: {d["jogador"]}')
print(f'O campo gols tem o valor: {d["gols"]}')
print(f'O campo total tem o valor: {d["total"]}')
print('-=' * 20)
print(f'O jogador {d["jogador"]} jogou {tot_partidas} partidas.')
for i in range(0, tot_partidas):
    print(f'Na partida {i} ele fez {gols[i]}.')
print(f'foi no total {sum(gols)} gols.')
