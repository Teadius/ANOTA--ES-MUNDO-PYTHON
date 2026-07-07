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