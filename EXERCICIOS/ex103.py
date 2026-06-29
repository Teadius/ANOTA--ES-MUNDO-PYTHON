def jogador(n='<Desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-'*40)
nomej = str(input('Nome do jogador: ')).strip()
golsj = str(input('Número de gols: ')).strip()
if golsj.isnumeric():
    golsj = int(golsj)
else:
    golsj = 0
if nomej == '':
    jogador(g=golsj)
else:
    jogador(nomej, golsj)
