# nas strings o computador salva cada letra em uma posicao 
# na memoria, e cada caractere e separado.

# fatiamento de string (pegar um pedaço da string)
frase = 'Curso em Video Python' # 21 caracteres no total
#        0123456789
print(frase)
print(frase[9]) # pega a letra da posicao 9 (v)
print(frase[9:13]) # pega da posicao 9 ate 13 (vide)
print(frase[9:21]) # pega do 9 ate o final da string mesmo 
# sem colocar o 21
print(frase[9:21:2]) # de 9 a 21 pulando de 2 em 2 (vdo hto)
print(frase[:5]) # do 0 ate o 5 (curso)
print(frase[15:]) # do 15 ate o final (python)

# print(variavel_string[0:0:0]) [inicio:fim:pulo]
print('=='*20)



# Analise de string

len(frase) # len vem de length, significa comprimento 
# resulta em 21 um numero inteiro do total de caracters

print(frase.count('o')) # conta quantas vezes tem a letra 'o' (3)
print(frase.find('o')) # mostra em que posicao esta a letra 'o' (13)
print(frase.find('deo')) # mostra em que posicao esta a string 'deo' 
# (11)
print(frase.find('Android'), 'a string android nao existe') 
# mostra -1, pois a string nao existe
print(frase.rfind('o')) # mostra a posicao da ultima ocorrencia da 
# letra 'o' (17)



print('=='*20)



# Transformações de string

print(frase.replace('python','android')) 
# substituie python por android na string

print(frase.upper()) # upper e um metodo
# coloca todos as letras minusculas e coloca em maiusculo

print(frase.lower()) # lower tambem e um metodo
# coloca todas as letras maiusculas em minusculo

print(frase.capitalize()) # coloca todos os caracters em minusculo
# menos o primeiro caractere 

print(frase.title()) # transforma todos os primeiros caracteres em
# maiuscole e mantem os internos em minusculo

print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())
# apaga caracteres indejejados

print(frase.split()) # divide a string em um lista pelos espaços

print('-'.join(frase)) # junta os elementos de uma string


# para escrever strings grandes use """ ou ''' para abrir e fechar a 
# string, assim o python considera tudo o que esta nas aspas.
