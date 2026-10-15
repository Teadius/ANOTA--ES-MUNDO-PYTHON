# Banco de Dados com Python: Aprenda SQL do Zero - Curso Python POO: Aula 16

# O que e um banco de dados?
# Todo computador tem uma memoria prinvipal, nela e armazenado todo dado armazenado e volatil na memoria ram e é apenas para rodar um dado ou programa.
# A memoria principal e volatil ela se perde ao desligar o programa.

# Ja a memoria secundario e utilizada par armazenar de forma permanente.

# Quando a quantidade de dados aumenta em um numeor elevado por exmeplo bilhoes de nomes de pessoas, e utilizado um banco de dados.
# Basicamente um banco de dados e composto por uma ou mais tabelas, e uma extrutura complexa que armazena uma serie de dados de forma eficiente e organizada.
# Alem disso e possivel determinar relações entre esses dados, tipo um cliente da tabela A compra um produto da tabela B.

# Existem diferentes opções de bancos de dados para utilizar como:

# PostgrSQL
# MySQL
# MariaDB
# Oracle
# SQL Server
# SQLite - banco de dados simples utilizado para esse curso

# O SQLite e um banco de dados relacional, ou seja, ele organiza os dados em tabelas que podem se relacionar entre si. Ele e muito utilizado em aplicativos mobile, 
# sistemas embarcados e ate mesmo em alguns sistemas desktop. E um banco de dados leve rapido e de facil utilizacao, sendo uma excelente escolha para projetos pequenos e medianos.
# Alem de ser compativel com python.


"""
MySQL exemplo 01:

CREATE TABLE amigos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacimento DATE NOT NULL
);

INSERT INTO amigos 
    ( nome, nacimento )
VALUES
    ( 'Joao', '2000-01-01' ),
    ( 'Maria', '1995-05-10' ),
    ( 'Pedro', '1988-12-20' );

SELECT nome, nacimento
FROM amigos
WHERE nacimento >= '2000-01-01'
"""