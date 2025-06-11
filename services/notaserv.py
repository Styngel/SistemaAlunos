from database.db import conectar
from services.arquivo import Arquivo

class NotaService:
            def __init__(self):
                self.arquivo = Arquivo()

            def dar_nota(self, matricula: int, disciplina_id: int, nota: float):
                try:
                    nota = float(nota)
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO notas (aluno_matricula, disciplina_id, nota) VALUES (?, ?, ?)",
                        (matricula, disciplina_id, nota)
                    )
                    conn.commit()
                    print("Nota cadastrada com sucesso!")
                    self._salvar_arquivo()
                except ValueError:
                    print("Erro: nota deve ser um valor decimal.")
                except Exception as e:
                    print(f"Erro ao cadastrar nota: {e}")
                finally:
                    conn.close()

            def listar(self):
                try:
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM notas")
                    notas = cursor.fetchall()
                    if not notas:
                        print("Nenhuma nota cadastrada.")
                        return
                    for n in notas:
                        print(f"ID: {n[0]} | Matrícula: {n[1]} | Disciplina ID: {n[2]} | Nota: {n[3]}")
                except Exception as e:
                    print(f"Erro ao listar notas: {e}")
                finally:
                    conn.close()

            def remover(self, id: int):
                try:
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM notas WHERE id = ?", (id,))
                    conn.commit()
                    if cursor.rowcount:
                        print("Nota removida com sucesso!")
                        self._salvar_arquivo()
                    else:
                        print("Nota não encontrada.")
                except Exception as e:
                    print(f"Erro ao remover nota: {e}")
                finally:
                    conn.close()

            def atualizar_nota(self, id: int, nova_nota: float):
                try:
                    nova_nota = float(nova_nota)
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE notas SET nota = ? WHERE id = ?",
                        (nova_nota, id)
                    )
                    conn.commit()
                    if cursor.rowcount:
                        print("Nota atualizada com sucesso!")
                        self._salvar_arquivo()
                    else:
                        print("Nota não encontrada.")
                except ValueError:
                    print("Erro: nota deve ser um valor decimal.")
                except Exception as e:
                    print(f"Erro ao atualizar nota: {e}")
                finally:
                    conn.close()


            def _salvar_arquivo(self):
                try:
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("SELECT id, aluno_matricula, disciplina_id, nota FROM notas")
                    dados = [dict(id=l[0], matricula=l[1], disciplina_id=l[2], nota=l[3]) for l in cursor.fetchall()]
                    conn.close()
                    self.arquivo.salvar_dados('notas', dados)
                except Exception as e:
                    print(f"Erro ao salvar notas no arquivo: {e}")