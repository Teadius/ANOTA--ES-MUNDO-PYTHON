import random
competidores  = dict()
for i  in range(1, 5):
    colocacao = random.randint(1, 4)
    while colocacao in competidores.values():
        colocacao = random.randint(1, 4)
    competidores[f'jogador{i}'] = colocacao
print('Valores sorteados:')
for k, v in competidores.items():
    print(f'{k} tirou {v}')
print('Ranking dos competidores:')
ranking = sorted(competidores.items(), key=lambda x: x[1], reverse=False)
for i, (k, v) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {k} com {v}')
