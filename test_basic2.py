import pytest
from functions import encontrar_valor, length, soma_lista


def test_len():
    assert length([1, 2, 3, 4]) == 4

def test_soma_lista():
    assert soma_lista([1, 2, 3]) == 6
    assert soma_lista([10.5, 4.5, 5]) == 20.0
    assert soma_lista([]) == 0

    with pytest.raises(ValueError):
        soma_lista([1, 2, "a"])


def test_encontrar_valor():
    dicionario = {'a': 1, 'b': 2, 'c': 3}
    assert encontrar_valor(dicionario, "a") == 1
    assert encontrar_valor(dicionario, "b") == 2
    assert encontrar_valor(dicionario, "d") == None

    with pytest.raises(ValueError):
        encontrar_valor("Não é um dicionário", "a")


