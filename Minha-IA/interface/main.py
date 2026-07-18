from data.memory import carregar_memoria, salvar_memoria
from intelligence.brain import responder


memoria = carregar_memoria()

if "usuario" not in memoria:
    memoria["usuario"] = input("Qual é o seu nome? ")
    salvar_memoria(memoria)


print("Aurora AI iniciada.")


while True:
    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        print("Aurora: Até logo!")
        break

    resposta = responder(mensagem, memoria)

    print("Aurora:", resposta)
