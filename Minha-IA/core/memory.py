import json
import os

ARQUIVO = "data/memory.json"

def carregar_memoria():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_memoria(memoria):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(memoria, arquivo, indent=4)
