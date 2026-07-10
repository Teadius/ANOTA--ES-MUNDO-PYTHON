# Essa aula fala sobre como tratar erros nos porgramas python
# Não se espente tem varios erros sendo cometidos todos os dias
# O foco e como lidar com eles.


# Tipos de erros
#   Erro de sintaxe: Ocorre quando o interpretador encontra um 
# erro na sintaxe do código, ou seja, quando o código não segue 
# as regras da linguagem Python.

#   Erro de indentação: Ocorre quando o código não respeita o 
# alinhamento correto de espaços ou tabulações exigido pelo 
# Python.

#   Erro de executação: Ocorre quando o código é sintaticamente 
# correto, mas durante a execução do programa ocorre um erro que 
# impede que ele continue a ser executado.

#   Erro de manipulação de dados e variaveis: Ocorre quando o 
# código tenta manipular dados ou variáveis de forma incorreta, 
# como tentar usar uma variável não definida ou converter um texto 
# inválido em número.

#   Erro de tipo: Ocorre ao tentar realizar uma operação matemática 
# ou lógica combinando tipos de dados incompatíveis.

#   Erro de coleções: Ocorre ao tentar acessar um índice que não 
# existe em uma lista ou uma chave inexistente em um dicionário.

#   Erro matemático: Ocorre quando uma operação quebra regras da 
# matemática, como tentar dividir um número pelo algarismo zero.

#   Erro de arquivos e sistema: Ocorre quando o programa tenta 
# ler ou modificar um arquivo que não existe ou que está bloqueado.

#   Erro de importação: Ocorre quando o interpretador não consegue 
# encontrar um módulo ou pacote que está sendo importado no código.

#   Erro de lógica: Ocorre quando o código é sintaticamente 
# correto e não gera erros de execução, mas o resultado produzido 
# pelo programa não é o esperado devido a um erro na lógica do código.



# ==============================================================================
# SIMULADOR DE ERROS E EXCEÇÕES NATIVAS DO PYTHON
# ==============================================================================

print("-" * 60)
print("      SIMULADOR DE EXCEÇÕES: MENSAGENS ORIGINAIS DO PYTHON")
print("-" * 60)

# --- 1. ERRO DE MANIPULAÇÃO DE DADOS (NameError) ---
try:
    print(variavel_que_nunca_existiu)
except NameError as erro:
    print(f"1. [NameError] Mensagem Original: {erro}")

# --- 2. ERRO DE VALOR (ValueError) ---
try:
    numero = int("texto_invalido")
except ValueError as erro:
    print(f"2. [ValueError] Mensagem Original: {erro}")

# --- 3. ERRO DE TIPO (TypeError) ---
try:
    soma = "Texto" + 5
except TypeError as erro:
    print(f"3. [TypeError] Mensagem Original: {erro}")

# --- 4. ERRO DE ÍNDICE EM COLEÇÕES (IndexError) ---
try:
    lista = [10, 20]
    item = lista[5]
except IndexError as erro:
    print(f"4. [IndexError] Mensagem Original: {erro}")

# --- 5. ERRO DE CHAVE EM DICIONÁRIOS (KeyError) ---
try:
    dicionario = {"nome": "Guilherme"}
    idade = dicionario["idade"]
except KeyError as erro:
    print(f"5. [KeyError] Mensagem Original: {erro}")

# --- 6. ERRO MATEMÁTICO (ZeroDivisionError) ---
try:
    divisao = 10 / 0
except ZeroDivisionError as erro:
    print(f"6. [ZeroDivisionError] Mensagem Original: {erro}")

# --- 7. ERRO DE ARQUIVO NÃO ENCONTRADO (FileNotFoundError) ---
try:
    with open("arquivo_fantasma_123.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as erro:
    print(f"7. [FileNotFoundError] Mensagem Original: {erro}")

# --- 8. ERRO DE IMPORTAÇÃO (ModuleNotFoundError) ---
try:
    import biblioteca_que_nao_existe
except ModuleNotFoundError as erro:
    print(f"8. [ModuleNotFoundError] Mensagem Original: {erro}")

# --- 9. ERRO DE ATRIBUTO (AttributeError) ---
try:
    texto = "Curso em Video"
    texto.append("Guanabara") # .append não existe em strings, só em listas
except AttributeError as erro:
    print(f"9. [AttributeError] Mensagem Original: {erro}")


# ------------------------------------------------------------------------------
# SOBRE ERROS DE SINTAXE E INDENTAÇÃO:
# ------------------------------------------------------------------------------
# Os erros abaixo não podem ser capturados pelo 'try/except' durante a execução
# porque eles quebram o código antes dele começar a rodar. 
# Se você descommantar as linhas abaixo, o simulador inteiro vai parar.

# Erro de Sintaxe (SyntaxError):
# print("Olá" if x = 10) 

# Erro de Indentação (IndentationError):
# def funcao():
# print("Erro de espaço")
# ------------------------------------------------------------------------------

print("-" * 60)
print("Simulação concluída com sucesso!")
print("-" * 60)



# Lista de Exceções do Python (Python Exception List)
#   BaseException: A classe mãe de todas as exceções do sistema, 
# responsável por gerenciar erros estruturais e interrupções.

#   Exception: A classe mãe de todas as exceções comuns e erros de 
# execução do dia a dia, usada para capturar falhas genéricas.

#   SyntaxError: Ocorre quando o código quebra as regras gramaticais 
# e estruturais da linguagem Python antes de começar a rodar.

#   IndentationError: Ocorre quando os blocos de código não seguem 
# o alinhamento correto de espaços ou tabulações exigido.

#   TabError: Ocorre especificamente quando há uma mistura confusa 
# de espaços e caracteres de tabulação (Tabs) no mesmo arquivo.

#   NameError: Ocorre ao tentar usar uma variável, função ou objeto 
# que não foi previamente criado ou definido no código.

#   TypeError: Ocorre quando uma operação ou função é aplicada a um 
# tipo de dado inadequado ou incompatível com aquela ação.

#   ValueError: Ocorre quando um dado possui o tipo correto, mas seu 
# conteúdo ou valor é inadequado para a conversão ou operação.

#   AttributeError: Ocorre ao tentar acessar uma função, método ou 
# propriedade que aquele tipo de objeto específico não possui.

#   LookupError: A classe base para erros que envolvem falhas na 
# busca de elementos dentro de coleções ou sequências de dados.

#   IndexError: Ocorre ao tentar acessar uma posição ou índice que 
# está fora dos limites existentes em uma lista ou tupla.

#   KeyError: Ocorre exclusivamente em dicionários ao tentar buscar 
# por uma chave ou propriedade que não existe lá dentro.

#   ArithmeticError: A classe base que engloba todas as falhas 
# numéricas e erros de cálculos matemáticos no código.

#   ZeroDivisionError: Ocorre ao tentar realizar a operação 
# matematicamente impossível de dividir um número pelo algarismo 
# zero.
#   OverflowError: Ocorre quando o resultado de um cálculo numérico 
# é grande demais para a capacidade de memória atual do sistema.

#   FloatingPointError: Ocorre em falhas raras e internas do sistema 
# ao processar operações complexas com números decimais.

#   OSError: A classe base para erros causados por falhas de 
# comunicação direta com o sistema operacional da máquina.

#   FileNotFoundError: Ocorre quando o programa tenta abrir, ler ou 
# modificar um arquivo que não existe no caminho informado.

#   PermissionError: Ocorre quando o programa tenta acessar um arquivo 
# protegido que exige privilégios de administrador do sistema.


#   IsADirectoryError: Ocorre ao tentar abrir ou manipular uma pasta 
# inteira como se ela fosse um arquivo de texto comum.

#   ImportError: Ocorre quando o Python encontra uma falha geral ao 
# tentar importar um módulo, biblioteca ou elemento específico.

#   ModuleNotFoundError: Ocorre quando você tenta importar uma 
# biblioteca que ainda não foi instalada no ambiente do computador.

#   KeyboardInterrupt: Ocorre quando o usuário interrompe a execução 
# do programa pressionando as teclas Ctrl+C no terminal.

#   SystemExit: Gerado internamente pela função exit() quando o 
# programa é finalizado de forma proposital pelo desenvolvedor.

#   StopIteration: Sinaliza de forma automática que um laço de 
# repetição ou gerador chegou ao fim da sua lista de itens.



# ==============================================================================
# EXEMPLOS PRÁTICOS DE CADA EXCEÇÃO DO PYTHON (Python Exception List)
# ==============================================================================

print("-" * 60)
print("      EXEMPLOS PRÁTICOS DAS EXCEÇÕES DO PYTHON")
print("-" * 60)

# --- BaseException ---
# Classe mãe de todas as exceções. Geralmente não forçada diretamente, 
# mas captura interrupções críticas do sistema.
try:
    raise BaseException("Erro estrutural crítico")
except BaseException as erro:
    print(f"[BaseException] Exemplo disparado: {erro}")

# --- Exception ---
# Classe mãe de exceções comuns. Usada para capturar erros genéricos de execução.
try:
    raise Exception("Um erro genérico qualquer aconteceu")
except Exception as erro:
    print(f"[Exception] Exemplo disparado: {erro}")

# --- NameError ---
# Ocorre ao tentar usar algo que não foi definido no código.
try:
    print(variavel_fantasma)
except NameError as erro:
    print(f"[NameError] Exemplo disparado: {erro}")

# --- TypeError ---
# Ocorre ao aplicar uma operação a um tipo de dado incompatível.
try:
    resultado = "Texto" + 10
except TypeError as erro:
    print(f"[TypeError] Exemplo disparado: {erro}")

# --- ValueError ---
# Ocorre quando o tipo está correto, mas o valor é inválido para a operação.
try:
    numero = int("Python")
except ValueError as erro:
    print(f"[ValueError] Exemplo disparado: {erro}")

# --- AttributeError ---
# Ocorre ao tentar usar um método que o objeto não possui.
try:
    lista = [1, 2, 3]
    lista.upper()  # .upper() pertence a strings, não a listas
except AttributeError as erro:
    print(f"[AttributeError] Exemplo disparado: {erro}")

# --- LookupError ---
# Classe base para erros de busca. Pode ser usada para capturar IndexError ou KeyError.
try:
    raise LookupError("Falha genérica ao buscar elemento")
except LookupError as erro:
    print(f"[LookupError] Exemplo disparado: {erro}")

# --- IndexError ---
# Ocorre ao tentar acessar um índice inexistente em uma lista ou tupla.
try:
    lista = [10, 20]
    print(lista[5])
except IndexError as erro:
    print(f"[IndexError] Exemplo disparado: {erro}")

# --- KeyError ---
# Ocorre ao buscar uma chave inexistente dentro de um dicionário.
try:
    dados = {"nome": "Ana"}
    print(dados["idade"])
except KeyError as erro:
    print(f"[KeyError] Exemplo disparado: {erro}")

# --- ArithmeticError ---
# Classe base para erros numéricos e matemáticos.
try:
    raise ArithmeticError("Falha em cálculo aritmético")
except ArithmeticError as erro:
    print(f"[ArithmeticError] Exemplo disparado: {erro}")

# --- ZeroDivisionError ---
# Ocorre ao tentar dividir qualquer número por zero.
try:
    calculo = 5 / 0
except ZeroDivisionError as erro:
    print(f"[ZeroDivisionError] Exemplo disparado: {erro}")

# --- OverflowError ---
# Ocorre quando um cálculo numérico excede o limite máximo de memória.
try:
    import math
    math.exp(1000)  # Gera um número absurdamente grande
except OverflowError as erro:
    print(f"[OverflowError] Exemplo disparado: {erro}")

# --- FloatingPointError ---
# Nota: Esta exceção exige configurações de hardware/kernel específicas para estourar,
# por isso simulamos o seu disparo controlado.
try:
    raise FloatingPointError("Falha interna em operação float")
except FloatingPointError as erro:
    print(f"[FloatingPointError] Exemplo disparado: {erro}")

# --- OSError ---
# Classe base para erros do sistema operacional.
try:
    raise OSError("Falha de comunicação com o Sistema Operacional")
except OSError as erro:
    print(f"[OSError] Exemplo disparado: {erro}")

# --- FileNotFoundError ---
# Ocorre quando o arquivo solicitado não existe no caminho informado.
try:
    with open("documento_nao_existente.txt", "r") as arquivo:
        pass
except FileNotFoundError as erro:
    print(f"[FileNotFoundError] Exemplo disparado: {erro}")

# --- PermissionError ---
# Ocorre ao tentar modificar arquivos protegidos do sistema sem autorização.
try:
    with open("/root/protegido.txt", "w") as arquivo:  # Caminho restrito no Linux/Unix
        pass
except PermissionError as erro:
    print(f"[PermissionError] Exemplo disparado: {erro}")
except OSError: # Fallback caso o sistema operacional barra de outra forma
    print("[PermissionError/OSError] Bloqueado pelo sistema")

# --- IsADirectoryError ---
# Ocorre ao tentar ler uma pasta como se ela fosse um arquivo de texto comum.
try:
    with open("minha_pasta", "r") as arquivo:  # Tentando ler a pasta recém-criada
        conteudo = arquivo.read()
except PermissionError as erro:
    print(f"[PermissionError] Exemplo disparado: {erro}")


# --- ImportError ---
# Ocorre quando há falha geral ao tentar puxar um elemento de um módulo.
try:
    from math import funcao_que_nao_existe
except ImportError as erro:
    print(f"[ImportError] Exemplo disparado: {erro}")

# --- ModuleNotFoundError ---
# Ocorre ao tentar importar uma biblioteca que não está instalada.
try:
    import biblioteca_fantasma_xyz
except ModuleNotFoundError as erro:
    print(f"[ModuleNotFoundError] Exemplo disparado: {erro}")

# --- KeyboardInterrupt ---
# Disparado quando o usuário aperta Ctrl+C. Simulamos o disparo controlado.
try:
    raise KeyboardInterrupt()
except KeyboardInterrupt:
    print("[KeyboardInterrupt] Exemplo disparado: Interrupção via teclado simulada.")

# --- SystemExit ---
# Disparado pela função exit(). Simulamos a captura para o programa não fechar de verdade.
try:
    raise SystemExit()
except SystemExit:
    print("[SystemExit] Exemplo disparado: Encerramento de programa interceptado.")

# --- StopIteration ---
# Sinaliza que um iterador não possui mais elementos para entregar.
try:
    iterador = iter([1])
    next(iterador)
    next(iterador)  # Segundo 'next' quebra porque a lista só tinha 1 item
except StopIteration:
    print("[StopIteration] Exemplo disparado: Fim dos itens do iterador atingido.")


# ------------------------------------------------------------------------------
# EXCEÇÕES DE COMPILAÇÃO (NÃO PODEM SER CAPTURADAS POR TRY/EXCEPT EM EXECUÇÃO)
# ------------------------------------------------------------------------------
# Os erros abaixo quebram o interpretador antes de rodar o código. 
# Deixamos comentados para não travar o script inteiro:

# SyntaxError:
# print("Olá" if x = 10)

# IndentationError:
# def funcao():
# print("Espaço errado")

# TabError:
# Ocorre quando misturamos espaços (Spaces) com tabulações (Tabs) na mesma indentação.
# ------------------------------------------------------------------------------

print("-" * 60)
print("Todos os exemplos foram executados com sucesso!")
print("-" * 60)
