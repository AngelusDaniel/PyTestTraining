def adicionar_usuario(cursor, name, email ):
    """Adicionar um novo usuário na tabela """
    cursor.execute("""
        INSERT INTO users(name, email)
        VALUES (?, ?)
    """, (name, email))


def buscar_usuario(cursor, email):
    """Busca usuário por email"""
    cursor.execute("""
        SELECT * FROM users WHERE email = ?
    """, (email,))
    return cursor.fetchone()


    