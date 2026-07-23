# POO (Programação Orientada a Objetos)
# OOP (Object Oriented Programming)
# OOAD (Object Oriented Analysis and Design)

# Esse curso tratara sobre a programação orientada a objetos.
# Começando a historia de on veio.
# Para que serve.
# As vantagens do usu.
# Entendendo o paradigma.

# Fundamentação:
# Classe.
# objeto.
# Atributos.
# Metodos.
# Estado.
# instancia.
# visibilidade.
# Os pilares do POO. (Esse curso ira considerar 4 pilares)

# Pilares do POO:
# 1 - Abstração
# 2 - Encapsulamento
# 3 - Herança
# 4 - Polimorfismo

# Outros conceitos:
# Getters e Setters.
# self e super.
# dunder methods.
# associação.
# agregação.
# compposição.

# Ao fim o curso tratara sobre bancos de dados.
# Acesso de bases locais.
# SQLite3.
#Object-relational mapping. (ORM)



# OBS: O curso ira ter bibliografia recomenmdada para estudo.
# E so abrir o python.org e abrir a opção localizada apra PTBR.

# Livros recomendados:
# Introdução à Programação com python - Nilo Ney Coutinho Menezes
# Object-oriented python - Irv Kalb (ingles)
# Python 3 (ingles)




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




#As 6 VANTAGENS da  POO: Programação Orientada a Objetos - Curso Python POO: Aula 02

# Quais as  vantagens em aprender a linguagem orientada a objetos.
# EX: Um carro por exemplo e feito for varios componentes/objetos,
#  uma carcaça que depois recebe mais partes e em alguma horas 
# com auxilio de varios processos se torna um carro completo.
#  Cada objeto do sistem faz seu trabalho.

# "COMERNada" esse simples resumo diz as principais vantagens da POO
# Confiavel    - O isolameto emtre as partes cria um sistema seguro que ao alterar um parte as outras não se afetam. Se uma porta quebrar o carro continua andando.
# Oportuno     - Ao dividir tudo em partes cada parte pode ser desenvolvida em paralelo. Cada parte de um carro pode ser melhorada ou fabricada ao mesmo tempo para a montagem final.
# Manutenível  - Atualizar e mais facil. Uma pequena alteração vai benedificar todas as aprtes relacionadas. Trocar o motor pode beneficiar todas as partes do carro e sua performace.
# Extensível   - Um sistema não deve ser estatico. Tudo deve mudar e crever para permanecer util. Do mesmo modo todas as prates podem ser trocadas para uma melhoria no todo.
# reutilizável - Objetos que foram criados apra um sistema podem ser aproveitados em outros sistemas. Tipo o motor de um carro a pode ser bom para um outro carro b e funcionar muito 
#                bem.
# Natural      - Mais facil de entender. Maior atenção as funcionalidades do que aos detalhes de implementação. Ou seja não preciso saber como o motor funciona somente que o que ele 
#                faz ao final do seu processo.

# 6. Criei um sistema para um escola, ao criar um outro sistema para uma academia, estara feito, pois tenho alunos nos dois.
# a.confiavel
# b.natural
# c.manutenivel
# d.reutilizavel xxxxx

# 7. Se precsiar adicionar uma nova funcionalidade ao sistema, consigo fazer com grande facilidade.
# a.natural
# b.extencivel  xxxxxx
# c.reutilizavel 
# d.oportuno

# 8.Posso desenvolver varias funcoes que dependam da outra ao mesmo tempo se o planejamento for seguido.
# a.oportuno   xxxxxxxxxx
# b.reutilizavel
# c.confiaevl
# d.manutenivel  

# 9.O codigo fica muito simples de ler e entender. ja que não preciso saber os detalhes de funcionalidade ao programar.
# a.natural  xxxxxxxxx
# b.extensivel 
# c.manutenivel
# d.Oportuno

# 10.Posso alterar como uma funcionalidade trabalha e tudo continua funcionando como antes.
# a.oportuno 
# b.Reutilizavel
# c.confiavel  xxxxxx
# d.natural


"""
================================================================================
          GABARITO AVALIADO: PRINCÍPIOS E VANTAGENS DA POO
================================================================================

[NOTA FINAL: 7.0 / 10.0]
Você demonstrou excelente entendimento prático, especialmente em reutilização 
e extensibilidade. Atenção apenas na diferenciação técnica entre o resultado 
esperado (ex: confiabilidade) e a propriedade de design que gera esse resultado 
(ex: manutenibilidade/encapsulamento).

--------------------------------------------------------------------------------

QUESTÃO 6: Criei um sistema para uma escola, ao criar um outro sistema para 
uma academia, estará feito, pois tenho alunos nos dois.
  - Resposta Escolhida: d. reutilizavel
  - Status: [ CORRETO ] 🟢
  - Justificativa: Se você já modelou a classe 'Aluno' com seus atributos base, 
    reaproveitar essa mesma estrutura lógica em um sistema de contexto diferente 
    é a definição exata de Reutilização de Código.

QUESTÃO 7: Se precisar adicionar uma nova funcionalidade ao sistema, consigo 
fazer com grande facilidade.
  - Resposta Escolhida: b. extensivel
  - Status: [ CORRETO ] 🟢
  - Justificativa: A capacidade de um software crescer, aceitando novos recursos, 
    módulos ou novos comportamentos sem a necessidade de reescrever ou quebrar 
    a base antiga, chama-se Extensibilidade.

QUESTÃO 8: Posso desenvolver várias funções que dependam da outra ao mesmo tempo 
se o planejamento for seguido.
  - Resposta Escolhida: a. oportuno
  - Status: [ INCORRETO ] 🔴
  - Resposta Correta: d. manutenivel (ou Modular / Baixo Acoplamento)
  - Justificativa: O desenvolvimento em paralelo e estruturado sem gerar o 
    "efeito dominó" (onde mexer em um canto quebra o outro) indica alta 
    Manutenibilidade. O planejamento permite isolar as dependências de forma limpa.

QUESTÃO 9: O código fica muito simples de ler e entender, já que não preciso 
saber os detalhes de funcionalidade ao programar.
  - Resposta Escolhida: a. natural
  - Status: [ CORRETO ] 🟢
  - Justificativa: A POO busca aproximar a programação do nosso raciocínio real. 
    Interagir com objetos simulados de forma intuitiva, ocultando a complexidade 
    técnica oculta sob os panos, torna o fluxo muito mais Natural para o humano.

QUESTÃO 10: Posso alterar como uma funcionalidade trabalha e tudo continua 
funcionando como antes.
  - Resposta Escolhida: c. confiavel
  - Status: [ INCORRETO ] 🔴
  - Resposta Correta: c. manutenivel (Benefício direto do Encapsulamento)
  - Justificativa: Embora isso gere confiabilidade ao sistema, a característica 
    técnica descrita é a Manutenibilidade gerada pelo Encapsulamento. Você altera 
    o comportamento interno de um método (ex: a fórmula de cálculo) sem precisar 
    modificar nenhuma outra linha de código do restante do programa.

================================================================================
"""

# Seu código ou próximas anotações da aula podem continuar aqui abaixo...




# Python Orientado a Objetos: Criando Classes e Objetos na Prática - Curso Python POO: Aula 04
# "Objetos são variaveis evoluidas"
# O conceito de objeto se basea em estar juntando dados+funções.
# Objeto
# Assim, um objeto e uma variavel que alem de guardar dados, pode executar funcionalidades.
# Em outras palavras, objetos são variaveis que, alem de gaurdar dados, podem fazer coisas com esses dados.

#EX000
#Declaração da classe:
class MinhaClasse:
    """area de Atributos"""
    """area de Metodos"""


# Declaração da clsse:
obj = MinhaClasse("instancia")  # Instancia > Metodo construtor > def__init__(self):

#EX001
# Declaração de classe
class Gafanhoto:
    def __init__(self): # Metodo construtor
        # Atributo de instancia
        self.nome = ""
        self.idade = 0

    # Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        if self.nome == "":
            self.nome = "Nome não definido"
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 18
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())


# EX002
# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que e um pessoa que tem nome e idade.

    Para criar uma pessoa, use
    variavel = Gaganhoto(nome, idade)
    """
    def __init__(self, n="Sem nome", i=0): # Metodo construtor
        # Atributo de instancia
        self.nome = n
        self.idade = i
    # Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade-1} anos de idade e fara {self.idade} em seu aniversario!"
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"


# Declaração de objetos
g1 = Gafanhoto(n="Maria", i=17) # define a variavel como um objeto com dois atributos
g1.aniversario() # Adiciona um para o aniversario
print(g1) # Chama o __str__() que retorna a mensagem 

print(g1.__doc__) # DEUNDER ATTRIBUTE descreve a documentação presente no codigo

print(g1.__dict__) # Atributo pois não tem parenteses
print(g1.__getstate__()) # Metodo pois possui parentesis no final
print(g1.__class__) # Mostra o nome da classe
"""
Classe: É a "planta" ou o modelo que define a estrutura de um objeto. Ela descreve quais características (atributos) e comportamentos (métodos) um objeto terá (23:44).

Objeto: É a instância concreta da classe. Se a classe é o projeto de uma casa, o objeto é a casa construída fisicamente (23:57).

Atributo: São as variáveis que definem as características de um objeto (ex: nome, idade, saldo). Eles armazenam os dados específicos daquela instância (24:02).

Estado: É o conjunto dos valores atuais dos atributos de um objeto em um dado momento. O estado diz "quem" ou "como" aquele objeto está (ex: uma conta bancária com saldo de R$ 3.500) 
(24:04).

Método: São as funções definidas dentro da classe que representam o comportamento do objeto. Eles permitem que o objeto execute ações ou altere seu próprio estado (ex: depositar(), 
sacar()) (1:48, 33:47).
"""
