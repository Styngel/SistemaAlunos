class Nota:
    def __init__(self, id: int, aluno_matricula: int, disciplina_id: int, nota: float):
        self.id = id
        self.aluno_matricula = aluno_matricula
        self.disciplina_id = disciplina_id
        self.nota = nota

    def __str__(self):
        return f'ID: {self.id} | Matrícula: {self.aluno_matricula} | Disciplina ID: {self.disciplina_id} | Nota: {self.nota}'