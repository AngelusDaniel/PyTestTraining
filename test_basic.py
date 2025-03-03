import functions


def test_positive():
    assert functions.is_positive(5) == True
    assert functions.is_positive(-1) == False


def test_email():
    assert functions.validate_email("teste@teste.c") is  True
    assert functions.validate_email("teste.c") is False