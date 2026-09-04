from rich import inspect, print
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():
    a1 = Aluno(nome="João", idade=20, curso="Engenharia", turma="A")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    print(a1)
    p1 = Professor(nome="Maria", idade=35, especialidade="Matemática", nivel="Doutorado")
    p1.fazer_aniversario()
    p1.dar_aula()
    print(p1)
    f1 = Funcionario(nome="Carlos", idade=40, cargo="Gerente", setor="Financeiro")
    f1.fazer_aniversario()
    f1.bater_ponto()
    print(f1)



    inspect(a1, methods=True, private=True, all=True)
    inspect(p1, methods=True, private=True, all=True)
    inspect(f1, methods=True, private=True, all=True)

if __name__ == "__main__":
    main()