from abc import ABC, abstractclassmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é invalido.")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterara a idade. Mude o ano de nascimento.")


class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "ENG", "CNT"]
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O Curso {curso} não esta na lista de cursos.")

    @classmethod
    def add_curso(cls, curso: str):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            if curso in cls.cursos_oficiais:
                raise ValueError(f"Curso {curso} ja incluso na lista de cursos")
            cls.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} esta fora de padrão para cursos")
