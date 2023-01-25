def registration(login, password, name, age, email, card, connection):
    cursor = connection.cursor()
    cursor.callproc('register_customer', (login, password, name, age, email, card))
    return cursor.fetchone()[0]