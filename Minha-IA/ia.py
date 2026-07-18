print("Olá! Eu sou uma IA simples.")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "olá":
        print("IA: Olá! Como posso ajudar?")

    elif pergunta.lower() == "sair":
        print("IA: Até logo!")
        break

    else:
        print("IA: Ainda estou aprendendo.")
