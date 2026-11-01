import sqlite3
from datetime import date

script_sql = """
CREATE TABLE IF NOT EXISTS amigos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL
);

-- Deleta os registros antes de inserir para não duplicar toda vez que rodar o script
DELETE FROM amigos;

INSERT INTO amigos (nome, nascimento) VALUES 
('Joao', '2000-01-01'),
('Maria', '1995-05-10'),
('Pedro', '1988-12-20'),
('Carlos', '2000-01-01'),
('Jonas', '1995-06-10'),
('Lucia', '1998-03-02'),
('Gustavo', '2010-01-01'),
('Mario', '1975-05-10'),
('Nicolas', '2000-01-01');
"""

try:
    with sqlite3.connect('data.db') as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()

        cur.executescript(script_sql)
        banco.commit()

        busca = input("Digite o nome para buscar (ou Enter para todos): ").strip()
        
        if not busca:
            cur.execute("SELECT * FROM amigos")
        else:
            cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", ('%' + busca + '%',))

        total = 0
        for amigo in cur.fetchall():
            total += 1
            nasc = amigo['nascimento']

            if nasc:
                data = date.fromisoformat(nasc)
                
                hoje = date.today()
                idade = hoje.year - data.year
                if (hoje.month, hoje.day) < (data.month, data.day):
                    idade -= 1
                    
                print(f"{amigo['nome']} nasceu em {data:%d/%m/%Y} e tem {idade} anos.")
            else:
                print(f"{amigo['nome']} não informou a data de nascimento.")

        if total == 0:
            print("Nenhum amigo encontrado.")
        elif total == 1:
            print("1 amigo encontrado.")
        else:
            print(f"{total} amigos encontrados.")

except sqlite3.Error as erro:
    print(f"Erro ao acessar o banco de dados: {erro}")
