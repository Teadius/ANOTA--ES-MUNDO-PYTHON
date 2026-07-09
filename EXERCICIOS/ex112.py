from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 10, 10, True)
