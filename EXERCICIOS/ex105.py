def notas(*n, sit=False):
    """    
    => Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Aprovado'
        elif r['media'] >= 5:
            r['situação'] = 'Recuperação'
        else:
            r['situação'] = 'Reprovado'
    situacaofinal = r.get('situação', 'Situação não informada')
    return (f'A quantidade de notas e de {r["total"]}.\n'
            f'A maior nota e igual a {r["maior"]}\n'
            f'A menor nota e igual a {r["menor"]}\n'
            f'A media e igual a {r["media"]}\n'
            f'A situação do aluno e {situacaofinal}')


#Programa principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
