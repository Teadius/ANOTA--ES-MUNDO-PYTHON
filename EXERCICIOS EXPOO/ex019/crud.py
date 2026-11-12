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


def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Gustavo", "1.84"),
        ("2", "Gabriela", "1.63"),
        ("3", "Pedro", "2.02"),
        ("4", "Mariana", "1.72"),
    ]
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.executemany("INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)", cad_pessoas)
    except sqlite3.Error as erro:
        print("[ERRO] Falha ao fazer cadastro em massa")

def cadastrar_pessoa() -> bool:
    print("\n ==== NOVO CADASTRO DE PESSOA ==== ")
    val_nome = input("Nome: ").strip()
    if not val_nome:
        print("[ERRO] O nome é um campo obrigatorio!")
        return False
    val_altura = input("Altura(metros): ").strip().replace(",", ".")
    if not val_altura:
        print("[ERRO] A altura é um campo obrigatorio!")
        return False
    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura >= 3.00:
            print("[ERRO] A altura deve ser um valor entre 0.30 e 3.00 metros!")
            return False
    except ValueError:
        print("[ERRO] A altura deve ser um valor numérico!")
        return False
    try: 
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)", (val_nome, altura))
            print(f"\n[INFO] Pessoa cadastrada com sucesso! Código: {cur.lastrowid}")
            return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao cadastrar pessoa: {erro}")
        return False


def listar_pessoa() -> bool:
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa() -> bool:
    pass

