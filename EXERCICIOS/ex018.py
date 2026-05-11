import math

angulo = float(input('digite o angulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('angulo {} \n seno {:.2f}\n cosseno {:.2f}\n tangente {:.2f}'.format(angulo, seno, coseno, tangente))

