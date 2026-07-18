from core.memory import aprender, lembrar


def responder(mensagem, memoria):

    texto = mensagem.lower()

    if texto.startswith("meu ") and " é " in texto:

        partes = texto.replace("meu ", "").split(" é ")

        chave = partes[0].strip()
        valor = partes[1].strip()

        aprender(chave, valor, memoria)

        return f"Vou lembrar que seu {chave} é {valor}."


    if "qual" in texto and "meu" in texto:

        chave = texto

        chave = chave.replace("qual é o meu ", "")
        chave = chave.replace("qual é meu ", "")
        chave = chave.replace("qual meu ", "")
        chave = chave.replace("qual éo meu ", "")
        chave = chave.replace("?", "")
        chave = chave.strip()

        valor = lembrar(chave, memoria)

        if valor:
            return f"Seu {chave} é {valor}."

        return f"Ainda não sei qual é seu {chave}."


    if "nome" in texto:
        return "Meu nome é Aurora AI."


    if "quem sou eu" in texto:
        return f"Você é {memoria.get('usuario')}."


    if "olá" in texto or "ola" in texto:
        return f"Olá, {memoria.get('usuario')}!"


    return "Ainda estou aprendendo essa informação."
