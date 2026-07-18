def normalizar_texto(texto):

    texto = texto.lower()
    texto = texto.replace("?", "")
    texto = texto.strip()

    return texto
