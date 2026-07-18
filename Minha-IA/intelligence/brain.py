from data.memory import aprender, lembrar
from intelligence.nlp import normalizar_texto
from intelligence.intent import identificar_intencao


def responder(mensagem, memoria):

    texto = normalizar_texto(mensagem)

    intencao = identificar_intencao(texto)


    if intencao == "aprender":

        partes = texto.replace("meu ", "").split(" é ")

        chave = partes[0].strip()
        valor = partes[1].strip()

        aprender(chave, valor, memoria)

        return f"Vou lembrar que seu {chave} é {valor}."


    elif intencao == "lembrar":

        chave = texto
        chave = chave.replace("qual é o meu ", "")
        chave = chave.replace("qual meu ", "")
        chave = chave.replace("?", "")
        chave = chave.strip()

        valor = lembrar(chave, memoria)

        if valor:
            return f"Seu {chave} é {valor}."

        return "Ainda não sei essa informação."


    elif intencao == "saudacao":

        return f"Olá, {memoria.get('usuario')}!"


    elif intencao == "identidade":

        return f"Você é {memoria.get('usuario')}."


    else:

        return "Ainda estou aprendendo essa informação."
