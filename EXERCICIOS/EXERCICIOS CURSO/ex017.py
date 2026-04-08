catetoO = float(input('digite o valor do cateto oposto: '))
catetoA = float(input('digite o valor do cateto adjacente: '))

# metodo sem import
hipotenusa = ((catetoO ** 2) + (catetoA ** 2)) ** (1/2)
print('a hipotenusa é {:.2f}'.format(hipotenusa))

# com a funcionalidade hypot da biblioteca math
from math import hypot
hypote = hypot(catetoO, catetoA)
print('a hipotenusa e {:.2f}'.format(hypote))

# outro metodo
from math import sqrt
sqrth = sqrt((catetoO ** 2) + (catetoA ** 2))
print('a hipotenusa e {:.2f}'.format(sqrth))
