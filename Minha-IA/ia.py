nome_ia = "Aurora"

print(f"Olá! Eu sou {nome_ia}, uma IA simples.")

try:
    with open("memoria.txt", "r") as arquivo:
        nome_usuario = arquivo.read().strip()

except:
    nome_usuario = ""

if nome_usuario == "":
    nome_usuario = input("Qual é o seu nome? ")

    with open("memoria.txt", "w") as arquivo:
        arquivo.write(nome_usuario)

print(f"Prazer em falar com você, {nome_usuario}!")

while True:
    pergunta = input(f"{nome_usuario}: ")

    if pergunta.lower() == "olá":
        print(f"{nome_ia}: Olá, {nome_usuario}!")

    elif pergunta.lower() == "sair":
        print(f"{nome_ia}: Até logo, {nome_usuario}!")
        break

    else:
        print(f"{nome_ia}: Ainda estou aprendendo.")
