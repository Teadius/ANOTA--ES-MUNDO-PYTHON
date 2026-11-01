import sqlite3


busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect('data.db') as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", ('%' + busca + '%',))
        total = 0
        for amigo in cur.fetchall():
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")


except sqlite3.Error as erro:
    print(f"Erro ao acessar o banco de dados: {erro}")
except FileNotFoundError:
    print("Erro: O arquivo 'banco.sql' não foi encontrado na mesma pasta do script.")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
