
class Aluno:
    notas_aluno = [7.5, 8.0, 6.5, 9.0]

    media = sum(notas_aluno) / len(notas_aluno)

    print('A media do aluno é {}'.format(media))
    def aprovacao(self, media):
        if media >= 6.0:
            print('O aluno foi aprovado!')
        else:
            print('O aluno foi reprovado!')

Aluno1 = Aluno()
Aluno1.aprovacao(Aluno1.media)
