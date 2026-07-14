# ==============================================================================
# ARQUIVO DE MÓDULOS E FUNÇÕES (ex115.py)
# ==============================================================================

# --- FUNÇÕES DE INTERFACE ---
def leiaInt(msg):
    """Valida a entrada de números inteiros tratando ValueError e interrupções."""
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[0m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[0m - \033[34m{item}\033[0m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[0m')
    return opc


# --- FUNÇÕES DE MANIPULAÇÃO DE ARQUIVOS ---
def arquivoExiste(nome):
    """Verifica se o arquivo txt já existe no diretório atual."""
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """Cria um novo arquivo txt usando o modo wt+."""
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'Houve um ERRO na criação do arquivo: {erro}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """Lê os dados gravados e formata o layout de exibição no console."""
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'Erro ao ler o arquivo: {erro}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha_arq in a:
            dado = linha_arq.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    """Abre o arquivo no modo 'at' (append text) e insere uma nova pessoa."""
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Houve um ERRO na abertura do arquivo: {erro}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(f'Houve um ERRO na hora de escrever os dados: {erro}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
