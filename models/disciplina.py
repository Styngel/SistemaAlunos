class Disciplina:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f'ID: {self.id} | Nome: {self.nome}'