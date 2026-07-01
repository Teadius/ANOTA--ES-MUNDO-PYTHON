def notas(*nota):
    """    
    => Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('='*40)
    if not nota:
        print('Nenhuma nota foi infomrada.')
        return
    notam = nota[0]
    mnota = nota[0]
    for i in range(1, len(nota)):
        if nota[i] > notam:
            notam = nota[i]
    for i in range(1, len(nota)):
        if nota[i] < mnota:
            mnota = nota[i]
    media = sum(nota) / len(nota)
    if media >= 7:
        situacao = 'Aprovado'
    elif media < 7 and media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    return f'A quantidade de notas e de {len(nota)}.\n'f'A maior nota e igual a {notam}\n'f'A menor nota e igual a {mnota}\n'f'A media e igual a {media}\n'f'A situação do aluno e {situacao}'


#Programa principal
resp = notas(5.5, 2.5, 10, 6.5)
print(resp)
help(notas) 
