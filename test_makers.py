import pytest


def funcao_unidade(x):
    """ Função de exemplo para testes unitários """
    return x * 2

def funcao_integracao(x):
    """ Função de exemplo para testes de integração """
    return x + 10


#teste unitário
@pytest.mark.unit
def test_funcao_unidade():
    assert funcao_unidade(2) == 4
    assert funcao_unidade(0) == 0
    assert funcao_unidade(-1) == -2

@pytest.mark.integration
def test_funcao_integracao():
    funcao_integracao(2) == 12
    funcao_integracao(0) == 10
    funcao_integracao(-5) == 5


@pytest.mark.slow
def test_funcao_lenta():
    import time
    time.sleep(2)
    assert True

@pytest.mark.unit
@pytest.mark.integration
def test_funcao_combinada():
    assert funcao_unidade(3) == 6
    assert funcao_integracao(3) == 13

    


