# ==============================================================================
# ARQUIVO PRINCIPAL DO SISTEMA (ex115index.py)
# ==============================================================================
from ex115 import *
from time import sleep

# Nome do arquivo de texto que armazenará os dados
arq = 'cursoemvideo.txt'

# Verifica a existência do arquivo antes de iniciar o loop do menu
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo txt
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de fazer um novo registro
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Encerramento controlado do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[0m')
    sleep(1)
