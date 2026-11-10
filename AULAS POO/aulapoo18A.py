"""

================================================================================
ANOTAÇÕES DE ESTUDO: SISTEMA CRUD COM PYTHON E SQLITE
================================================================================

Perguntas Frequentes:
- Como criar um pequeno sistema com banco de dados?
- Como criar um banco de dados usando código Python?
- O que significa CRUD? — Create, Read, Update e Delete (criar, ler, atualizar e apagar).
- Como começar a montar um CRUD com Python e SQLite?

Conceitos Fundamentais:
1. SQLite para Pequenos Sistemas:
   Para criar um pequeno sistema com banco de dados usando Python, a melhor escolha 
   para começar é o SQLite. Ele já vem instalado nativamente no Python, não exige 
   nenhuma configuração complexa e armazena todas as informações em um único arquivo 
   local no seu computador.
   (Referências: https://cm-kls-content.s3.amazonaws.com/202002/INTERATIVAS_2_0/LINGUAGEM_DE_PROGRAMACAO/LIVRO_DIGITAL/npf_u3s3.html | https://pt.linkedin.com/pulse/criando-um-projeto-b%C3%A1sico-de-crud-em-python-com-sqlite-harada-vdg6f | https://dev.to/driuzim/criando-um-crud-simples-com-python-opl)

2. O que é CRUD?
   O acrônimo CRUD representa as quatro operações fundamentais de qualquer sistema 
   que manipula dados: Create (Criar), Read (Ler), Update (Atualizar) e Delete (Apagar). 
   Em bancos de dados relacionais, essas ações correspondem diretamente aos comandos 
   SQL INSERT, SELECT, UPDATE e DELETE.
   (Referências: https://www.youtube.com/watch?v=FHKZSuS0t1Q | https://querobolsa.com.br/revista/crud-o-que-e | https://realpython.com)

Próximos Passos de Evolução:
Deseja expandir esse sistema criando uma interface gráfica simples no terminal ou 
prefere evoluí-lo para uma API web usando frameworks como o Flask ou FastAPI?
(Referência: https://www.treinaweb.com.br/blog/criando-o-primeiro-crud-com-fastapi)


# CRUD Create Read Update Delete
#      Criar  Ler  Atualziar Deletar


"""



import sqlite3

# ==============================================================================
# PASSO 1: CRIANDO O BANCO DE DADOS E A TABELA
# ==============================================================================
def inicializar_banco():
    """Conecta ao arquivo do banco (ele será criado imediatamente caso não exista)."""
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    # Cria a tabela de usuários se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()


# ==============================================================================
# PASSO 2: CONSTRUINDO AS FUNÇÕES DO CRUD
# ==============================================================================

# 1. Create (Inserir dados)
def criar_usuario(nome, email):
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este e-mail já está cadastrado.")
    finally:
        conexao.close()


# 2. Read (Ler/Consultar dados)
def listar_usuarios():
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    
    conexao.close()
    return usuarios


# 3. Update (Atualizar dados)
def atualizar_email_usuario(id_usuario, novo_email):
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (novo_email, id_usuario))
    conexao.commit()
    
    if cursor.rowcount > 0:
        print("E-mail atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")
        
    conexao.close()


# 4. Delete (Apagar dados)
def deletar_usuario(id_usuario):
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    
    if cursor.rowcount > 0:
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")
        
    conexao.close()


# ==============================================================================
# PASSO 3: TESTANDO O FLUXO COMPLETO
# ==============================================================================
if __name__ == "__main__":
    # Garante que a estrutura inicial do banco existe antes dos testes
    inicializar_banco()
    
    print("--- 1. Testando o CREATE ---")
    criar_usuario("Alice Silva", "alice@email.com")
    criar_usuario("Bruno Costa", "bruno@email.com")

    print("\n--- 2. Testando o READ ---")
    usuarios = listar_usuarios()
    for u in usuarios:
        print(f"ID: {u[0]} | Nome: {u[1]} | E-mail: {u[2]}")

    print("\n--- 3. Testando o UPDATE ---")
    # Atualiza o e-mail do usuário com ID 1
    atualizar_email_usuario(1, "alice.silva@novoemail.com")

    print("\n--- 4. Testando o DELETE ---")
    # Remove o usuário com ID 2
    deletar_usuario(2)

    print("\n--- Estado Final do Banco de Dados ---")
    for u in listar_usuarios():
        print(f"ID: {u[0]} | Nome: {u[1]} | E-mail: {u[2]}")
