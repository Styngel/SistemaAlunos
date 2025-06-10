import sqlite3
import os

DB_FILE = 'dados/sistema.db'

def conectar():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    return sqlite3.connect(DB_FILE)

class Database:
    def __init__(self):
        self.criar_tabelas()

    def criar_tabelas(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                matricula INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS disciplinas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno_disciplina (
                aluno_matricula INTEGER,
                disciplina_id INTEGER,
                PRIMARY KEY (aluno_matricula, disciplina_id),
                FOREIGN KEY (aluno_matricula) REFERENCES alunos(matricula),
                FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_matricula INTEGER,
                disciplina_id INTEGER,
                nota REAL,
                FOREIGN KEY (aluno_matricula) REFERENCES alunos(matricula),
                FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
            );
        ''')

        conn.commit()
        conn.close()