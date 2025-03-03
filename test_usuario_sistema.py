import sqlite3

import pytest
from usuario_sistema import adicionar_usuario, buscar_usuario


@pytest.fixture
def db_connection():
    """
    Fixture que configura uma conexão com banco de dados SQLite
    temporário e garante a limpeza de recursos após o teste
    """

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )

    conn.commit()

    yield conn, cursor

    conn.close()

@pytest.mark.parametrize(
    "name, email, esperado_name",
    [
        ("Alice", "alice@exemple.com", "Alice"),
        ("Bob", "bob@exemple.com", "Bob"),
        ("Charlie", "charlie@exemple.com", "Charlie"),
    ]
)
@pytest.mark.unit
def test_adicionar_usuario(db_connection, name, email, esperado_name):
    conn, cursor = db_connection
    adicionar_usuario(cursor, name, email)
    resultado = buscar_usuario(cursor, email)
    
    assert resultado is not None
    assert resultado[1] == esperado_name
    assert resultado[2] == email


@pytest.mark.integration
def test_buscar_usuario_com_email_inexistente(db_connection):
    conn, cursor = db_connection
    resultado = buscar_usuario(cursor, "naoexiste@example.com")
    assert resultado is None


@pytest.mark.slow
@pytest.mark.integration
def test_adicionar_e_buscar_usuarios(db_connection):
    import time
    conn, cursor = db_connection

    for i in range(100):
        adicionar_usuario(cursor, f"user{i}" ,f"user{i}@example.com")

    conn.commit()

    time.sleep(2)

    for i in range(100):
        resultado = buscar_usuario(cursor, f"user{i}@example.com")

        assert resultado is not None
        assert resultado[1] == f"user{i}"
        assert resultado[2] == f"user{i}@example.com"



