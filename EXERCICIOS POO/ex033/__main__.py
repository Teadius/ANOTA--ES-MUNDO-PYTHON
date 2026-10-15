from pessoa import *

def main():
    p = Pessoa(nome="Ana", nasc=2000)
    print(p.idade)
    print(p.__dict__)

    a = Aluno(nome="Marcia", nasc=2010, curso="ADM")
    b = Aluno(nome="Pedro", nasc=2015, curso="ENG")
    a.add_curso("MODA")
    print(a.cursos_oficiais)
    print(a.__dict__)
    print(b.cursos_oficiais)
    print(b.__dict__)


if __name__ == "__main__":
    main()