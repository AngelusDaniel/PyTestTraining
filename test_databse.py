import sqlite3

import pytest


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


def test_database_search(db_connection):
    """
    Testa a inserção de um usuário da tabela users
    do banco de dados sqlite
    """

    conn, cursor = db_connection
    cursor.execute(
        """
        INSERT INTO users(name, email)
        VALUES (?, ?)
        """, ("John Doe", "john@example.com")
    )

    conn.commit()

    cursor.execute("SELECT * FROM users WHERE email = ?",
    ("john@example.com",))

    user = cursor.fetchone()
    assert user is not None
    assert user[1] == "John Doe"
    assert user[2] == "john@example.com"

