largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))

print('a area da parede é {}m^2'.format(largura*altura))
print('o perimetro da parede e {}m'.format(2*(largura+altura)))

print('para pintar a parede sera necessario {} litros de tinta'.format((largura*altura)/2))
