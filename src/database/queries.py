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
    create_table()
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

def add_expense(user_id, amount, description):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO expenses (user_id, amount, description)
                  VALUES (?, ?, ?)""", (user_id, amount, description))
    connection.commit()
    connection.close()

def get_budget(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT budget FROM users WHERE username = ?""", (username,))
    budget = cursor.fetchone()
    connection.close()

    return budget[0]

def get_user_id(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT id FROM users WHERE username = ?""", (username,))
    user_id = cursor.fetchone()
    connection.close()

    return user_id[0]

def current_month_expenses(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    #AI generated code starts (by ChatGPT)
    cursor.execute("""SELECT SUM(amount) FROM expenses
        WHERE user_id = ? AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')""", (user_id,))
    #AI generated code stops
    expenses = cursor.fetchone()
    connection.close()

    return expenses[0] or 0
