from hashlib import sha256

texto = "https://www.pudim.com.br/"
cod = texto.encode('utf-8')
hash = sha256(cod).hexdigest()
print(hash)
