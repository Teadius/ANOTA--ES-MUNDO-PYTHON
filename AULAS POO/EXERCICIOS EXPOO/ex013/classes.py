from abc import ABC, abstractclassmethod


class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz Pudim com leite condensado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no oleo de soja")


class Filho(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite em po e chocolate com avela")


class Filha(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} frita a coxinha a air fryer")