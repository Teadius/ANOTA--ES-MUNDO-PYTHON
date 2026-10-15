import xml.etree.ElementTree as ET
from json import dumps


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class JSON:
    def exportar(self, dados):
        lista = [item.__dict__ for item in dados]
        txt = dumps(lista, ensure_ascii=False, indent=2)
        return txt


class XML:
    def exportar(self, dados):
        pai = ET.Element("dados")
        nome = dados[0].__class__.__name__.lower()
        
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
                
        ET.indent(pai, space="\t")
        txt = ET.tostring(pai, encoding="unicode")
        return txt


def exportar(formato, dados):
    print(formato.exportar(dados))