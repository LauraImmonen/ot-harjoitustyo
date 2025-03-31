from database.create_database import get_connection, create_table

def user_exists(username):
    connection = get_connection()
    cursor = connection.cursor()
    create_table()
    cursor.execute("""SELECT COUNT(*) FROM users WHERE username = (?)""", (username,))
    user_count = cursor.fetchone()
    connection.close()
    #added by ChatGBT
    user_count = user_count[0] if user_count else 0
    return user_count > 0
    #AI generated code ends

def make_account(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (username, password)
                   VALUES (?, ?)""", (username, password))
    connection.commit()
    connection.close()

def login_by_username(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username = ?""", (username,))
    user = cursor.fetchone()
    connection.close()

    return user if user else None

#add budget query made by ChatGPT
def add_budget(budget, username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""UPDATE users SET budget = ? WHERE username = ?""", (budget, username))
    connection.commit()
    connection.close()
#AI generated code stops

def add_transaction(user_id, type, amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO transactions user_id, type,
                   amount VALUES (?, ?, ?)""", (user_id, type, amount))
    connection.commit()
    connection.close()

