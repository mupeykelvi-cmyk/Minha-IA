nome_ia = "Aurora"

print(f"Olá! Eu sou {nome_ia}, uma IA simples.")

nome_usuario = input("Qual é o seu nome? ")

print(f"Prazer em conhecer você, {nome_usuario}!")

while True:
    pergunta = input(f"{nome_usuario}: ")

    if pergunta.lower() == "olá":
        print(f"{nome_ia}: Olá, {nome_usuario}! Como posso ajudar?")

    elif pergunta.lower() == "sair":
        print(f"{nome_ia}: Até logo, {nome_usuario}!")
        break

    else:
        print(f"{nome_ia}: Ainda estou aprendendo.")

