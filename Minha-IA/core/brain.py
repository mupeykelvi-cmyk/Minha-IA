from core.memory import aprender, lembrar


def responder(mensagem, memoria):

    texto = mensagem.lower()

    if "eu gosto de" in texto:
        assunto = texto.replace("eu gosto de", "").strip()
        aprender("gosto", assunto, memoria)
        return f"Vou lembrar que você gosta de {assunto}."

    elif "do que eu gosto" in texto:
        gosto = lembrar("gosto", memoria)

        if gosto:
            return f"Você gosta de {gosto}."

        return "Ainda não sei do que você gosta."

    elif "olá" in texto or "ola" in texto:
        return f"Olá, {memoria.get('usuario')}!"

    elif "quem sou eu" in texto:
        return f"Você é {memoria.get('usuario')}."

    else:
        return "Ainda estou aprendendo essa informação."
