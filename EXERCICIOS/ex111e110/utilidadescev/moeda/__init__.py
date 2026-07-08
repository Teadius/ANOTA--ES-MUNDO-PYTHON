def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: O preço que se quer reajustar.
    :param taxa: A taxa de aumento.
    :param formato: Se deseja formatar o resultado.
    :return: O valor reajustado, com ou sem formatação.
    '''
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    '''
    -> Calcula a redução de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: O preço que se quer reajustar.
    :param taxa: A taxa de redução.
    :param formato: Se deseja formatar o resultado.
    :return: O valor reajustado, com ou sem formatação.
    '''
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    '''
    -> Calcula o dobro de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: O preço que se quer dobrar.
    :param formato: Se deseja formatar o resultado.
    :return: O valor dobrado, com ou sem formatação.
    '''
    return preco * 2 if not formato else moeda(preco * 2)


def metade(preco=0, formato=False):
    '''
    -> Calcula a metade de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: O preço que se quer reduzir à metade.
    :param formato: Se deseja formatar o resultado.
    :return: O valor pela metade, com ou sem formatação.
    '''
    return preco / 2 if not formato else moeda(preco / 2)


def moeda(preco=0, moeda='R$'):
    '''
    -> Formata o valor com o símbolo da moeda e duas casas decimais.
    :param preco: O valor a ser formatado.
    :param moeda: O símbolo da moeda.
    :return: O valor formatado.
    '''
    return f'{moeda}{preco:>0.2f}'.replace('.', ',')


def resumo(preco=0, taxa_aumento=10, taxa_reducao=10, formato=False):
    '''
    -> Exibe um resumo das operações realizadas sobre o preço, incluindo aumento, redução, dobro e metade.
    :param preco: O preço base para as operações.
    :param taxa_aumento: A taxa de aumento a ser aplicada.
    :param taxa_reducao: A taxa de redução a ser aplicada.
    :param formato: Se deseja formatar os resultados.
    '''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, formato)}')
    print(f'Metade do preço: \t{metade(preco, formato)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, formato)}')
    print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, formato)}')
    print('-' * 30)


