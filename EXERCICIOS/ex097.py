def escreva(txt):
    tamanho = len(txt) + 2
    print('~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('~' * tamanho)


valor = str(input('digite uma frase:  '))
escreva(txt=valor)
escreva(txt='MUNDO PYTHON')
escreva(txt='CURSO EM VIDEO')
