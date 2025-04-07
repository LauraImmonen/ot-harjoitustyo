import sqlite3

DB_NAME = "budgeting_app.db"

#code generated by ChatGPT, and tables refined by me

def get_connection():
    connection = sqlite3.connect(DB_NAME)
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        budget INTEGER DEFAULT 0)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                        type TEXT CHECK (type IN ('income', 'expense')),
                        amount INTEGER NOT NULL,
                        date DATE DEFAULT CURRENT_DATE)''')

    connection.commit()
    connection.close()




if __name__ == '__main__':
    create_table()
