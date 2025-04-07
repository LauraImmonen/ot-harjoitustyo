import unittest
from services.account_service import create_user, validate_login
from database.create_database import get_connection, create_table

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.username = "test_user_name"
        self.password = "123"
        self.wrong_username = "wrong_username"
        self.wrong_password = "456"
        get_connection()
        create_table()
        self.delete_test_user()

    def delete_test_user(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM users WHERE username=(?)""", (self.username,))
        connection.commit()
        connection.close()

    def test_create_user_that_doesnt_exist(self):
        self.assertEqual(create_user(self.username, self.password), "Account created successfully!")

    def test_create_user_that_exists(self):
        create_user(self.username, self.password)
        self.assertEqual(create_user(self.username, self.password), "Username already exists! Please choose another username.")

    def test_login_successful(self):
        create_user(self.username, self.password)
        self.assertEqual(validate_login(self.username, self.password), "Logged in successfully!")

    def test_login_wrong_password(self):
        create_user(self.username, self.password)
        self.assertEqual(validate_login(self.username, self.wrong_password), "Incorrect password!")

    def test_login_wrong_username(self):
        create_user(self.username, self.password)
        self.assertEqual(validate_login(self.wrong_username, self.password), "Username not found!")



