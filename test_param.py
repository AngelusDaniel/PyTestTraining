import pytest


def calcular_area(base, altura):
    return base * altura

@pytest.fixture
def dados_teste():
    """
    Fixture que fornece diferentes conjuntos de dados para 
    testar a função de cálculo de área
    """

    return [
        {"base": 2, "altura": 3, "esperado": 6},
        {"base": 5, "altura": 6, "esperado": 30},
        {"base": 9, "altura": 9, "esperado": 81},
        {"base": 7, "altura": 5, "esperado": 35},
        {"base": 12, "altura": 10, "esperado": 120},
    ]

@pytest.mark.parametrize("dados", [
    {"base": 2, "altura": 3, "esperado": 6},
    {"base": 5, "altura": 6, "esperado": 30},
    {"base": 9, "altura": 9, "esperado": 81},
    {"base": 7, "altura": 5, "esperado": 35},
    {"base": 12, "altura": 10, "esperado": 120},
])
def test_calcular_area(dados):
    base = dados["base"]
    altura = dados["altura"]
    esperado = dados["esperado"]

    resultado = calcular_area(base, altura)
    assert resultado == esperado


    