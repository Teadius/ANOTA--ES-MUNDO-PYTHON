from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("senha invalida")

    def validar(self, chave):
        usuario = sha256(chave.encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            print("senha confere!")
            return True
        else:
            print("senha invalida")
            return False

# hash = embaralhar uma senha para segurança da informação.
# SHA = secure hash algorithm : um algoritimo muito comun para proteção, uma criptografia popular.
# NSA = National security agency : tambem funcional para embaralhar palavras e proteger informações e utilizado pelo sistema de inteligencia.
