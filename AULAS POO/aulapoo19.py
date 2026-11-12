"""
================================================================================
ANOTAÇÕES DE ESTUDO: O "C" DO CRUD (CREATE) COM PYTHON E SQLITE - AULA 19
================================================================================

Perguntas Frequentes:
- Como inserir um único registro no SQLite usando Python? — Com cursor.execute().
- Como inserir vários registros de uma só vez? — Com cursor.executemany().
- Por que usar interrogações (?) nas consultas SQL? — Para evitar falhas de segurança 
  (SQL Injection) e tratar os tipos de dados com segurança.
- Como evitar erro quando o usuário digita vírgula na altura? — Substituindo ',' 
  por '.' antes de converter o texto para float.
- Como resolver o erro "database is locked"? — Fechando conexões abertas em 
  outros programas (como o DB Browser) e usando o bloco 'with' para gerenciar 
  automaticamente as transações.

Conceitos Fundamentais:
1. execute() vs executemany():
   O método execute() roda um comando SQL para uma única operação (como cadastrar 
   uma pessoa por vez). Já o executemany() recebe uma lista de tuplas e executa 
   o mesmo comando INSERT INTO para todos os itens de uma vez só, sendo muito 
   mais prático para cadastros em lote.

2. Segurança com Parâmetros SQL (?):
   Nunca devemos concatenar variáveis diretamente na string SQL usando f-strings. 
   O uso de marcadores '?' (placeholders) delega ao driver do SQLite a tarefa 
   de sanitizar e escapar os valores passados na tupla de parâmetros.

3. Gerenciamento de Contexto (with) e Tratamento de Erros (try/except):
   O bloco 'with sqlite3.connect(...) as db:' garante que o commit() seja feito 
   automaticamente em caso de sucesso e o rollback() em caso de erro. Combinado 
   com 'try/except sqlite3.Error', o programa não trava caso ocorra falha no 
   banco (como arquivo bloqueado por outro software).

4. Validação de Entrada do Usuário:
   Antes de enviar dados ao banco, validamos se o nome não está vazio e 
   convertemos a altura (aceitando vírgula ou ponto) para número real (float), 
   garantindo que valores inválidos sejam rejeitados antes da conexão.

Próximos Passos de Evolução:
Com o banco criado e populado pela operação Create, a próxima etapa do projeto 
é implementar o "R" do CRUD (Read) para listar todas as pessoas cadastradas 
e buscar registros específicos pelo nome.

# CRUD: Create   Read   Update     Delete
#       Criar    Ler    Atualizar  Deletar
================================================================================
"""

import sqlite3

NOME_BANCO = "cadastro.db"


# ==============================================================================
# PASSO 1: PREPARANDO O BANCO DE DADOS E A TABELA PESSOAS
# ==============================================================================
def criar_banco() -> bool:
    """Cria o arquivo cadastro.db e a tabela pessoas caso ainda não existam."""
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    altura REAL NOT NULL
                )
            """)
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao criar o banco de dados: {erro}")
        return False


# ==============================================================================
# PASSO 2: IMPLEMENTANDO O "C" DO CRUD (CREATE)
# ==============================================================================

# 1. Cadastro em lote usando executemany()
def cadastrar_varias_pessoas(lista_pessoas: list[tuple[str, float]]) -> bool:
    """Insere múltiplos registros de uma só vez usando executemany() e parâmetros (?)."""
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.executemany(
                "INSERT INTO pessoas (nome, altura) VALUES (?, ?)",
                lista_pessoas
            )
        print(f"{len(lista_pessoas)} registros inseridos em lote com sucesso!")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao inserir vários registros: {erro}")
        return False


# 2. Cadastro individual com validação de entrada e INSERT INTO
def cadastrar_pessoa_interativo() -> bool:
    """Solicita, valida os dados do usuário e insere um registro individual."""
    nome = input("Digite o nome da pessoa: ").strip()
    if not nome:
        print("Erro de validação: O nome não pode ficar em branco.")
        return False

    altura_texto = input("Digite a altura (ex: 1,75 ou 1.75): ").strip()
    try:
        # Aceita vírgula como separador decimal e converte para float
        altura = float(altura_texto.replace(",", "."))
        if altura <= 0:
            print("Erro de validação: A altura deve ser maior que zero.")
            return False
    except ValueError:
        print("Erro de validação: Digite um valor numérico válido para a altura.")
        return False

    # Inserção segura no banco com 'with' e tratamento de erros do SQLite
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO pessoas (nome, altura) VALUES (?, ?)",
                (nome, altura)
            )
        print(f"Pessoa '{nome}' ({altura:.2f}m) cadastrada com sucesso!")
        return True
    except sqlite3.OperationalError as erro:
        # Captura problemas como "database is locked" (banco aberto em outro programa)
        print(f"Erro operacional no SQLite (verifique se o banco não está bloqueado): {erro}")
        return False
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar pessoa no banco: {erro}")
        return False


# ==============================================================================
# PASSO 3: PREPARAÇÃO PARA A PRÓXIMA AULA (PRÉVIA DO READ)
# ==============================================================================
def listar_pessoas_teste():
    """Função auxiliar apenas para conferir os cadastros realizados nesta aula."""
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("SELECT codigo, nome, altura FROM pessoas")
            return cursor.fetchall()
    except sqlite3.Error as erro:
        print(f"Erro ao ler dados: {erro}")
        return []


# ==============================================================================
# PASSO 4: TESTANDO O FLUXO DA AULA 19
# ==============================================================================
if __name__ == "__main__":
    if criar_banco():
        print("--- 1. Testando inserção em lote com executemany() ---")
        lote_inicial = [
            ("Gustavo Guanabara", 1.82),
            ("Maria Oliveira", 1.65),
            ("Carlos Eduardo", 1.78)
        ]
        cadastrar_varias_pessoas(lote_inicial)

        print("\n--- 2. Testando cadastro individual com validação ---")
        cadastrar_pessoa_interativo()

        print("\n--- Registros atuais na tabela 'pessoas' ---")
        for pessoa in listar_pessoas_teste():
            print(f"Código: {pessoa[0]} | Nome: {pessoa[1]} | Altura: {pessoa[2]:.2f}m")
