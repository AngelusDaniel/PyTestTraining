def length(list):
    return len(list)


def is_positive(num):
    return num > 0


def validate_email(email):
    return "@" in email and "." in email \
    and email[len(email)-1] != "."

def soma_lista(valores):
    """Soma todos os valores em uma lista """
    if not all(isinstance(i, (int, float)) for i in valores):
        raise ValueError("Todos os itens d alista devem ser números")
    return sum(valores)

def encontrar_valor(dicionario, chave):
    """Retorno valor associado a uma chave e dicionário."""
    if not isinstance(dicionario, dict):
        raise ValueError("O primeiro argumento deve ser um diconário")
    return dicionario.get(chave, None)

    