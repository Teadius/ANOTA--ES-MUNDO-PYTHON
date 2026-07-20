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
