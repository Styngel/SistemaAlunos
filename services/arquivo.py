import os
import json

class Arquivo:
    def __init__(self, pasta='dados'):
        self.pasta = pasta
        if not os.path.exists(pasta):
            os.makedirs(pasta)

    def salvar_dados(self, nome_arquivo, dados):
        caminho = os.path.join(self.pasta, f"{nome_arquivo}.json")
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados(self, nome_arquivo):
        caminho = os.path.join(self.pasta, f"{nome_arquivo}.json")
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
