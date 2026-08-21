# Encapsulamento: público, protegido e privado (Parte 1) - Curso Python POO: Aula 10

#  O encapsulamento visa manter a integridade do sistema, protegendo o estado interno do objeto contra interferencia externa não regulamentada.
# Basicamente por exemplo: Evitar que a pessoa mecha no que não deveria, tupo um controle remoto não tem seus circuitos espostos ele tem uma parte de plastico cobrindo os circuitos e 
# somente mostra os botoes.

# Visibilidad: Nesse caso se refere a tornar um codigo 
# privado (-) 
# protegido(#) 
# publico(+) 
# Onde esses são utilizados na linguagem orientada a objeto para afirmar a visibilidade que aquele codigo tera.

# EX: main
#     a=A()
#     b=B()
#     c=C()
# Visibilidade
#   A:
#     +atrib1   esse atributo e publico utilizavel onde for chamado
#     #atrib2   esse atributo e protegido acessivel em sua classe e suas filhas
#     -atrib2   esse atributo e privado acessivel em sua classe

# Em python não considera nada disso, ele utiliza o Consenting Adults: Liberdade com responsabilidade.
# "A expressão "We are all consenting adults here" ("somos todos adultos com consentimento aqui") significa que o Python confia no bom senso do programador em vez de impor travas 
# rígidas de código. É por isso que a linguagem não possui bloqueios reais de visibilidade (como private ou protected strictos), permitindo convenções como o uso de sublinhado simples"
#
# A convenção e não mexar no que não deve. Inclusive nem tem essa função de definir como publico, privado ou protegido. 
# por isso e utilizado no lugar dos simbolos +-# os simbolos __ para representar isso, tipo:
# __atributo3   privado
# _atributo2    protegido
# atributo1     publico
