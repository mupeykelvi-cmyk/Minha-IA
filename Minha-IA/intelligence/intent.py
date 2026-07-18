def identificar_intencao(texto):

    if "meu " in texto and " é " in texto:
        return "aprender"

    if "qual" in texto and "meu" in texto:
        return "lembrar"

    if "olá" in texto or "ola" in texto:
        return "saudacao"

    if "quem sou eu" in texto:
        return "identidade"

    return "desconhecido"
