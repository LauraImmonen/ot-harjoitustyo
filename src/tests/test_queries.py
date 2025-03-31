import unittest
from services.account_service import create_user, validate_login
from database.create_database import get_connection, create_table

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.username = "test_user_name"
        self.password = "123"
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




