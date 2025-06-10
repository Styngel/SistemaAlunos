from database.db import Database
from services.alunoserv import AlunoService
from services.disciplinaserv import DisciplinaService
from services.notaserv import NotaService

# Inicialização do banco e arquivos
Database()

aluno_service = AlunoService()
disciplina_service = DisciplinaService()
nota_service = NotaService()


def menu_alunos():
    while True:
        print("\n--- MENU ALUNOS ---")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Remover aluno")
        print("4. Vincular disciplina")
        print("5. Dar nota")
        print("6. Consultar disciplinas e notas")
        print("0. Voltar")

        opc = input("Escolha: ")
        if opc == '1':
            try:
                m = int(input("Matrícula: "))
                n = input("Nome: ")
                c = input("CPF: ")
                aluno_service.adicionar(m, n, c)
            except ValueError:
                print("Matrícula inválida.")
        elif opc == '2':
            aluno_service.listar()
        elif opc == '3':
            try:
                m = int(input("Matrícula a remover: "))
                aluno_service.remover(m)
            except ValueError:
                print("Matrícula inválida.")
        elif opc == '4':
            try:
                m = int(input("Matrícula do aluno: "))
                disciplina_service.listar()
                d = int(input("ID da disciplina: "))
                aluno_service.vincular_disciplina(m, d)
            except ValueError:
                print("Entrada numérica inválida.")
        elif opc == '5':
            try:
                m = int(input("Matrícula do aluno: "))
                disciplina_service.listar()
                d = int(input("ID da disciplina: "))
                nota = float(input("Nota (ex 8.5): "))
                aluno_service.dar_nota(m, d, nota)
            except ValueError:
                print("Entrada numérica inválida.")
        elif opc == '6':
            try:
                m = int(input("Matrícula do aluno: "))
                aluno_service.listar_disciplinas_e_notas(m)
            except ValueError:
                print("Matrícula inválida.")
        elif opc == '0':
            break
        else:
            print("Opção inválida.")


def menu_disciplinas():
    while True:
        print("\n--- MENU DISCIPLINAS ---")
        print("1. Cadastrar disciplina")
        print("2. Listar disciplinas")
        print("3. Remover disciplina")
        print("0. Voltar")

        opc = input("Escolha: ")
        if opc == '1':
            nome = input("Nome da disciplina: ")
            disciplina_service.adicionar(nome)
        elif opc == '2':
            disciplina_service.listar()
        elif opc == '3':
            try:
                i = int(input("ID da disciplina: "))
                disciplina_service.remover(i)
            except ValueError:
                print("ID inválido.")
        elif opc == '0':
            break
        else:
            print("Opção inválida.")


def menu_notas_geral():
    while True:
        print("\n--- MENU NOTAS ---")
        print("1. Listar todas notas")
        print("2. Remover nota")
        print("0. Voltar")

        opc = input("Escolha: ")
        if opc == '1':
            nota_service.listar()
        elif opc == '2':
            try:
                i = int(input("ID da nota: "))
                nota_service.remover(i)
            except ValueError:
                print("ID inválido.")
        elif opc == '0':
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1. Alunos")
        print("2. Disciplinas")
        print("3. Notas")
        print("0. Sair")

        opc = input("Escolha: ")
        if opc == '1':
            menu_alunos()
        elif opc == '2':
            menu_disciplinas()
        elif opc == '3':
            menu_notas_geral()
        elif opc == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()