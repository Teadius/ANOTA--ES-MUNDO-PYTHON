from abc import ABC, abstractmethod
import re

class Validar(ABC): 
    @abstractmethod
    def validar(self, valor: str) -> bool:
        pass


class Usuario(Validar):
    def validar(self, valor: str) -> bool:
        regex = r"^[a-zA-Z0-9_]{5,20}$"
        return bool(re.fullmatch(regex, valor))


class Email(Validar):
    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        return bool(re.fullmatch(regex, valor))


class Senha(Validar):
    def validar(self, valor: str) -> bool:
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#%^&*?]).{8,}$"
        return bool(re.fullmatch(regex, valor))


def validar_dado(validador: Validar, valor: str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é válido? {'Sim' if resultado else 'Não'}")
