from database.db import conectar
from services.arquivo import Arquivo
from models.disciplina import Disciplina

class DisciplinaService:
    def __init__(self):
        self.arquivo = Arquivo()

    def adicionar(self, nome: str):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO disciplinas (nome) VALUES (?)", (nome,))
            conn.commit()
            print("Disciplina cadastrada com sucesso!")
            self._salvar_arquivo()
        except Exception as e:
            print(f"Erro ao cadastrar disciplina: {e}")
        finally:
            conn.close()

    def listar(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM disciplinas")
            linhas = cursor.fetchall()
            if not linhas:
                print("Nenhuma disciplina cadastrada.")
                return
            for l in linhas:
                print(Disciplina(l[0], l[1]))
        except Exception as e:
            print(f"Erro ao listar disciplinas: {e}")
        finally:
            conn.close()

    def remover(self, id: int):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM disciplinas WHERE id = ?", (id,))
            conn.commit()
            if cursor.rowcount:
                print("Disciplina removida com sucesso!")
                self._salvar_arquivo()
            else:
                print("Disciplina não encontrada.")
        except Exception as e:
            print(f"Erro ao remover disciplina: {e}")
        finally:
            conn.close()

    def buscar_por_id(self, id: int):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas WHERE id = ?", (id,))
        disc = cursor.fetchone()
        conn.close()
        return disc

    def _salvar_arquivo(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM disciplinas")
        dados = [dict(id=l[0], nome=l[1]) for l in cursor.fetchall()]
        conn.close()
        self.arquivo.salvar_dados('disciplinas', dados)