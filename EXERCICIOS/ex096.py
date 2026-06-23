def linha():
    print('-='*30)
def area(l, c):
    a = l * c
    return a


linha()
print(' Controle de terrenos ')
linha()
largura = int(input('Largura(m): '))
comprimento = int(input('Largura(m): ' ))
resiltado_area = area(l = largura, c = comprimento)
linha()
print(f'A área de um terreno de {largura}X{comprimento} é igual a {resiltado_area}m²')
linha()
