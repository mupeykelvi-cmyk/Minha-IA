def responder(mensagem, memoria):

    texto = mensagem.lower()

    if "nome" in texto:
        return "Meu nome é Aurora AI."

    elif "olá" in texto or "ola" in texto:
        return f"Olá, {memoria.get('usuario')}!"

    elif "quem sou eu" in texto:
        return f"Você é {memoria.get('usuario')}."

    elif texto == memoria.get("usuario", "").lower():
        return f"Sim, eu lembro de você, {memoria.get('usuario')}."

    else:
        return "Ainda estou aprendendo essa informação."
