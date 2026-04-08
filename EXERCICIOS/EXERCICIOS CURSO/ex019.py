import random


for i in range(1, 11):
    alunos = ['Carlos', 'Lana', 'Yago', 'Jolyne']
    sorteio = random.choice(alunos)
    print('o aluno sortiado foi {}'.format(sorteio))
