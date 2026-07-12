# Crie um codigo em python que teste se o site pudim esta 
# acessivel pelo computador usado.
# https://www.pudim.com.br/
import urllib.request
import urllib.error
import webbrowser

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    requisicao = urllib.request.Request('https://www.pudim.com.br/', headers=headers)
    site = urllib.request.urlopen(requisicao, timeout=5)
except urllib.error.URLError:
    print('\033[31mO site Pudim não esta disponivel no momeneto.\033[m')
else:
    print('\033[32mO site Pudim esta acessivel com sucesso.\033[m')
    webbrowser.open('https://www.pudim.com.br/')
