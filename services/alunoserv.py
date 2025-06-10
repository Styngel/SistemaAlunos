from database.db import conectar
from services.arquivo import Arquivo
from models.aluno import Aluno

class AlunoService:
    def __init__(self):
        self.arquivo = Arquivo()

    def adicionar(self, matricula: int, nome: str, cpf: str):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM alunos WHERE matricula = ?", (matricula,))
            if cursor.fetchone():
                print("Erro: Matrícula já cadastrada.")
                return

            cursor.execute(
                "INSERT INTO alunos (matricula, nome, cpf) VALUES (?, ?, ?)",
                (matricula, nome, cpf)
            )
            conn.commit()
            print("Aluno cadastrado com sucesso!")
            self._salvar_arquivo()
        except Exception as e:
            print(f"Erro ao cadastrar aluno: {e}")
        finally:
            conn.close()

    def listar(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alunos")
            linhas = cursor.fetchall()
            if not linhas:
                print("Nenhum aluno cadastrado.")
                return
            for l in linhas:
                print(Aluno(l[0], l[1], l[2]))
        except Exception as e:
            print(f"Erro ao listar alunos: {e}")
        finally:
            conn.close()

    def remover(self, matricula: int):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alunos WHERE matricula = ?", (matricula,))
            conn.commit()
            if cursor.rowcount:
                print("Aluno removido com sucesso!")
                self._salvar_arquivo()
            else:
                print("Aluno não encontrado.")
        except Exception as e:
            print(f"Erro ao remover aluno: {e}")
        finally:
            conn.close()

    def vincular_disciplina(self, matricula: int, disciplina_id: int):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM alunos WHERE matricula = ?", (matricula,)
            )
            if not cursor.fetchone():
                print("Aluno não encontrado.")
                return
            cursor.execute(
                "SELECT 1 FROM disciplinas WHERE id = ?", (disciplina_id,)
            )
            if not cursor.fetchone():
                print("Disciplina não encontrada.")
                return
            cursor.execute(
                "INSERT OR IGNORE INTO aluno_disciplina (aluno_matricula, disciplina_id) VALUES (?, ?)",
                (matricula, disciplina_id)
            )
            conn.commit()
            print("Disciplina vinculada ao aluno.")
            self._salvar_arquivo()
            self._salvar_vinculos_arquivo()
        except Exception as e:
            print(f"Erro ao vincular disciplina: {e}")
        finally:
            conn.close()

    def dar_nota(self, matricula: int, disciplina_id: int, nota: float):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM aluno_disciplina WHERE aluno_matricula = ? AND disciplina_id = ?",
                (matricula, disciplina_id)
            )
            if not cursor.fetchone():
                print("Aluno não está vinculado a essa disciplina.")
                return
            cursor.execute(
                "INSERT INTO notas (aluno_matricula, disciplina_id, nota) VALUES (?, ?, ?)",
                (matricula, disciplina_id, nota)
            )
            conn.commit()
            print("Nota cadastrada com sucesso!")
            self._salvar_arquivo()
        except Exception as e:
            print(f"Erro ao cadastrar nota: {e}")
        finally:
            conn.close()

    def listar_disciplinas_e_notas(self, matricula: int):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT d.id, d.nome FROM disciplinas d "
                "JOIN aluno_disciplina ad ON d.id = ad.disciplina_id "
                "WHERE ad.aluno_matricula = ?", (matricula,)
            )
            disciplinas = cursor.fetchall()
            if not disciplinas:
                print("Nenhuma disciplina vinculada a este aluno.")
                return
            for d in disciplinas:
                cursor.execute(
                    "SELECT nota FROM notas WHERE aluno_matricula = ? AND disciplina_id = ?",
                    (matricula, d[0])
                )
                res = cursor.fetchone()
                nota_str = res[0] if res else "[Sem nota]"
                print(f"Disciplina: {d[1]} | Nota: {nota_str}")
        except Exception as e:
            print(f"Erro ao listar disciplinas e notas: {e}")
        finally:
            conn.close()

    def _salvar_vinculos_arquivo(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT aluno_matricula, disciplina_id FROM aluno_disciplina")
            dados_vinculos = [
                {"matricula": row[0], "disciplina_id": row[1]} for row in cursor.fetchall()
            ]
            conn.close()
            self.arquivo.salvar_dados('vinculos', dados_vinculos)
        except Exception as e:
            print(f"Erro ao salvar vínculos no arquivo: {e}")

    def _salvar_arquivo(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT matricula, nome, cpf FROM alunos")
            dados = [dict(matricula=l[0], nome=l[1], cpf=l[2]) for l in cursor.fetchall()]
        finally:
            conn.close()
        self.arquivo.salvar_dados('alunos', dados)
