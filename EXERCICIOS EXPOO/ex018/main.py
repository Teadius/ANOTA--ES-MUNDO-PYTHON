import sqlite3

try:
    with sqlite3.connect(r'c:\Users\gabri\Desktop\programação\EXERCICIOS\ANOTAÇÕES MUNDO PYTHON\EXERCICIOS EXPOO\ex018\meubanco.db') as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        
        cur.execute("SELECT * FROM amigos")
        for amigo in cur:
            print(f"{amigo['nome']} nasceu em {amigo['nacimento']}")

except sqlite3.Error as erro:
    print(f"Erro ao acessar o banco de dados: {erro}")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
