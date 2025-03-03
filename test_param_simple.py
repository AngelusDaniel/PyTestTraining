import pytest


def adicionar(x, y):
    return x + y

@pytest.mark.parametrize(
    "entrada_x, entrada_y, result",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (5, 5, 10)
    ]
)
def test_adicionar(entrada_x, entrada_y, result):
    assert adicionar(entrada_x, entrada_y) == result