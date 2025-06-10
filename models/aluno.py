class Aluno:
    def __init__(self, matricula: int, nome: str, cpf: str):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Matrícula: {self.matricula} | Nome: {self.nome} | CPF: {self.cpf}'