from classes import Aluno, JSON, XML, Usuario, exportar


def main():
    u = [
        Usuario(nome="Maria", email="maria@gmail.com"),
        Usuario(nome="Joao", email="joao@gmail.com"),
        Usuario(nome="Ana", email="ana@gmail.com")
    ]
    a = [
        Aluno(nome="Pedro", curso="Informatica", serie="4 periodo"),
        Aluno(nome="Clara", curso="ADS", serie="8 periodo")
    ]
    json_exporter = JSON()
    xml_exporter = XML()

    print("=== EXPORTANDO USUÁRIOS EM JSON ===")
    exportar(json_exporter, u)

    print("\n=== EXPORTANDO ALUNOS EM XML ===")
    exportar(xml_exporter, a)


if __name__ == "__main__":
    main()