from abc import ABC, abstractmethod


class Arquivo(ABC):

    def __init__(self, nome: str, tam: int = 0):
        self.nome = nome
        self._extensao = None
        self.tam = tam

    @abstractmethod
    def abrir_arquivo(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext: str):
        formatos = ["pdf", "doc", "docx"]
        ext_formatada = ext.lower().strip()
        if ext_formatada in formatos:
            self._extensao = ext_formatada
        else:
            raise AttributeError("O arquivo está em um formato não suportado.")

    @property
    def nome_completo(self):
        return f"{self.nome}.{self.extensao}({self.tam/1000000}MB)"


class PDF(Arquivo):

    def __init__(self, nome: str, tam: int = 0):
        super().__init__(nome, tam)
        self.extensao = "pdf"

    def abrir_arquivo(self):
        print(
            f"Abrindo o arquivo '{self.nome_completo}' no Adobe Reader..."
        )


class DOC(Arquivo):

    def __init__(self, nome: str, tam: int = 0):
        super().__init__(nome, tam)
        self.extensao = "doc"

    def abrir_arquivo(self):
        print(
            f"Abrindo o arquivo '{self.nome_completo}' no Microsoft Word..."
        )


def abrir_arquivo(arquivo: Arquivo):
    arquivo.abrir_arquivo()
