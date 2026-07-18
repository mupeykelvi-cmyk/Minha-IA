import json
import os

ARQUIVO = "data/memory.json"


def carregar_memoria():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as arquivo:
            memoria = json.load(arquivo)

            if "conhecimento" not in memoria:
                memoria["conhecimento"] = {}

            return memoria

    return {
        "conhecimento": {}
    }


def salvar_memoria(memoria):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(memoria, arquivo, indent=4)


def aprender(chave, valor, memoria):
    memoria["conhecimento"][chave] = valor
    salvar_memoria(memoria)


def lembrar(chave, memoria):
    return memoria["conhecimento"].get(chave)
