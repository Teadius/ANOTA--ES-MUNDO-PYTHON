CREATE TABLE IF NOT EXISTS amigos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL
);

INSERT INTO amigos (nome, nascimento) VALUES 
('Joao', '2000-01-01'),
('Maria', '1995-05-10'),
('Pedro', '1988-12-20');
