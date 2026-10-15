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