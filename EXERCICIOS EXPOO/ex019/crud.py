import sqlite3
import os

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

NOME_BANCO = os.path.join(PASTA_ATUAL, "cadastro.db")


def criar_banco():
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS pessoas "
                        "(cod INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "nome TEXT NOT NULL, "
                        "altura REAL NOT NULL)")  
        return False
    except sqlite3.Error as erro:
        print(f"Falha na criação do banco: {erro}")
        return True


def cadastrar_pessoa() -> bool:
    pass


def listar_pessoa() -> bool:
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa() -> bool:
    pass

