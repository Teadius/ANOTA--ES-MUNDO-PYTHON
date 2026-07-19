# ==============================================================================
# AULA 1 - O MOTIVO DO SURGIMENTO DA POO
# ==============================================================================

# O que é POO?
# Como o próprio nome sugere, esse paradigma de programação utiliza "objetos" 
# para representar elementos do mundo real de forma computacional. 
# Ao longo do curso, qualquer elemento estruturado será chamado de objeto.

# --- Inspirações Filosóficas ---
# "A necessidade é a mãe da invenção." — Platão
# "É preciso ter o caos dentro de si para dar à luz uma estrela dançante." — Friedrich Nietzsche

# ------------------------------------------------------------------------------
# EVOLUÇÃO HISTÓRICA DOS PARADIGMAS
# ------------------------------------------------------------------------------

# Década de 1950: Baixo Nível (Assembly)
# Permitiu programar computadores de forma mais direta (substituindo o código de máquina),
# mas a codificação ainda era extremamente limitada, complexa e difícil de manter.

# Ano 1955: Linguagens Lineares / Sequenciais
# Os programas eram executados linearmente, da esquerda para a direita, do começo ao fim.
# Não possuíam estruturas de encapsulamento, reutilização ou escopo de código.

# O Papel de Edsger Dijkstra (Programação Estruturada)
# Dijkstra, um dos maiores cientistas da computação, criticou severamente o modelo linear
# e o uso indiscriminado de desvios (como o 'GOTO'), que geravam o "código espaguete".
# Ele foi um dos grandes defensores da Programação Estruturada e influenciou a criação 
# do ALGOL (ALGOrithmic Language), que introduziu blocos de código, condições e funções.
# Nota: Dijkstra também criou o famoso "Algoritmo de Dijkstra" para caminhos mínimos.

# ------------------------------------------------------------------------------
# O DISCURSO HISTÓRICO: "O PROGRAMADOR HUMILDE" (Prêmio Turing, 1972)
# ------------------------------------------------------------------------------
DISCURSO_DIJKSTRA = """
    Como resultado de um prêmio por decisão oficial ou critério de serviço, lerei agora para vocês a palestra intitulada "O Programador Humilde".
    Como resultado de uma longa cadeia de condições e coincidências, minha linha de vida tem corrido de forma coincidente com a história da computação automática por vários anos. 
    Comecei como programador na Holanda na primavera de 1952. Até onde sei, fui o primeiro holandês a fazê-lo em meu país e, além disso, ao olhar para trás, não posso deixar de ver que 
a comunidade científica daquela época ainda não estava totalmente consciente do que a programação realmente era.
Naqueles dias, a atitude predominante em relação à programação era de que se tratava de uma questão de perícia eletrônica ou de uma questão de aplicação de matemática numérica. 
    O programador era um funcionário de escalão um pouco inferior que aplicava as regras. Lembro-me do meu chefe, o Professor A. van Wijngaarden, dizendo-me quando fui me candidatar ao 
emprego que procurava um matemático disposto a trabalhar como programador. A ideia de que a programação pudesse ser uma disciplina intelectual independente ainda não havia nascido.
    Quando me casei em 1957, tive que declarar minha profissão para os registros oficiais e escrevi "Programador". As autoridades municipais de Amsterdã não aceitaram isso; declararam 
que não existia tal profissão. Como resultado, minha certidão de casamento afirma que sou um "Físico Teórico", que era a minha formação universitária.
    No início dos anos cinquenta, as máquinas eram muito pequenas e lentas. Tínhamos que viver com memórias de alguns milhares de palavras e velocidades de algumas milhares de 
operações por segundo. Passávamos muito tempo no que chamávamos de "espremer código": economizando uma instrução aqui ou um microssegundo ali. Era um esporte, um desafio, mas, 
olhando para trás, era um esporte muito perigoso porque desviava nossa atenção dos problemas reais da programação: como escrever programas que sejam corretos, compreensíveis e 
fáceis de manter.
    Enquanto as máquinas eram pequenas, o problema de programação também era pequeno. Mas então ocorreu uma grande mudança: o hardware tornou-se muito mais poderoso. Em vez de milhares 
de palavras de memória, obtivemos centenas de milhares; em vez de milissegundos, obtivemos microssegundos.
    Essa mudança foi chamada de "Revolução do Computador". Mas foi uma revolução em um sentido muito estranho: foi uma revolução que não resolveu nossos problemas, mas os criou. O 
cerne do problema é que, à medida que a potência das máquinas aumentava por um fator de mil, a complexidade dos programas que queríamos escrever aumentava por um fator de um 
milhão. Esta é a origem do que tem sido chamado de "Crise do Software".
    A principal causa da crise do software é que as máquinas se tornaram várias ordens de magnitude mais poderosas! Para ser bastante franco: enquanto não havia computadores, a 
programação não era problema algum; quando tínhamos alguns computadores fracos, a programação tornou-se um problema leve, e agora que temos computadores gigantescos, a programação 
tornou-se um problema igualmente gigantesco. Nesse sentido, a indústria eletrônica não resolveu nenhum dos nossos problemas, ela apenas criou o problema de usar os seus produtos.
    Uma das lições mais importantes que aprendemos nos últimos vinte anos é que a mente humana é limitada e que devemos fazer tudo o que pudermos para manter a complexidade dos nossos 
programas dentro dos limites da nossa capacidade intelectual. É por isso que acredito que a linguagem de programação que usamos é de vital importância. Uma linguagem de programação 
não deve ser uma ferramenta que nos permita expressar qualquer pensamento caótico que possamos ter; deve ser uma ferramenta que nos ajude a estruturar os nossos pensamentos e a 
evitar erros.
    A este respeito, sou muito crítico em relação a algumas das linguagens de programação amplamente utilizadas hoje, tais como FORTRAN, PL/I e até mesmo alguns recursos do ALGOL 60. 
Elas são muito complexas, cheias de acidentes históricos e recursos ad-hoc. Elas incentivam a esperteza em vez da clareza.
    A ferramenta que usamos tem uma influência profunda nos nossos hábitos de pensamento e, portanto, nas nossas capacidades de pensamento. Um programador que foi treinado em uma 
linguagem ruim fica intelectualmente incapacitado pelo resto de sua vida.
    Devemos aprender a ser humildes. Devemos aceitar que nossos cérebros são pequenos e que não podemos lidar com muita complexidade de uma só vez. O programador do futuro deve ser um 
"programador humilde". Ele não deve tentar ser esperto, mas deve tentar ser limpo. Ele deve usar métodos que lhe permitam provar a correção dos seus programas, em vez de confiar em 
testes para encontrar bugs após o fato. O teste pode mostrar a presença de bugs, mas nunca a ausência deles!
    A visão de futuro que quero apresentar a vocês é aquela em que a programação não é mais uma arte ou um ofício, mas uma disciplina científica rigorosa. Uma disciplina baseada na 
lógica matemática e no raciocínio estruturado. Só então seremos capazes de dominar a complexidade das máquinas que os engenheiros de hardware estão construindo para nós.
    Agradeço a vocês pela atenção.
"""

# ------------------------------------------------------------------------------
# A EVOLUÇÃO PARA A MODULARIZAÇÃO E POO
# ------------------------------------------------------------------------------

# Ano 1965: Linguagens Modulares
# Permitiram a criação de módulos com blocos de código separados. 
# Desenvolvedores podiam chamar essas funções sem precisar saber como funcionavam internamente.

# Década de 1970: O Surgimento da Orientação a Objetos (POO)
# Criada por Kristen Nygaard e Ole-Johan Dahl (cientistas da computação noruegueses).
# Eles desenvolveram a linguagem 'Simula' (focada em simulações), que introduziu formalmente 
# os conceitos de classes e objetos pela primeira vez na história.

# A Popularização e o Termo "POO"
# Alan Kay cunhou o termo "Programação Orientada a Objetos". 
# Ele foi o principal idealizador da linguagem 'Smalltalk', a primeira a adotar o paradigma 
# de forma pura e ampla, influenciando diretamente o C++, Java e o próprio Python.
# Inventor no leptope Alan Kay, que também foi um dos pioneiros na criação do conceito de interface gráfica (GUI) e da 
# programação visual. Ele tinha o "caso interior".
# Como nenhuma linguagem permitia a criação de sua invenção Kay criou a smalltalk, que foi a 
# primeira linguagem a adotar o paradigma de forma pura e ampla, influenciando diretamente o 
# C++, Java e o próprio Python.

# OOAD (Object Oriented Analysis and Design)
# O OOAD é uma metodologia de desenvolvimento de software que utiliza os conceitos da
# significa analise e design orientados a objetos. Ele se concentra na identificação de classes, objetos,
# atributos, métodos e relacionamentos entre eles, a fim de criar um modelo de software.



#  nota =  4/5  nota 8

# Em que decada aconteceu a crise do softwere no mercado?
# A. 1950
# B. 1960                         x
# C. 1980
# D. 2000

# Qual das caracteristicas a seguir identifica as priemiras 
# linguagens lineares?
# A. Maior modularidade
# B. Desvio forçados              O correto
# C. Estrururas de controle
# D. Instruções de baixo nivel    x

# Quem foi o criador da linguagem smalltalk, uma das primeiras 
# Linguagens POO?
# A. Edgar Dijstra]
# B. Guido Van Rossum
# C. Alan kay                    x
# D. Kisten Nygyaard


# A linbguagem Simula fo ium superconjunto de que outra 
# linguargem?

# a.algol                      x
# b.c
# c.smalltalk
# d.python

# Na sigla OOAD, as ultimas duas letras significam...?
# a.algol/dashboard
# b.algorithms/digital
# c.analysis/default
# d.analysis/desing             x