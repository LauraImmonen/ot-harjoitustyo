import unittest
from services.account_service import create_user, validate_login
from services.budget_service import create_budget, check_budget, add_expenses, final_report, past_expenses
from database.create_database import get_connection, create_table
from datetime import datetime

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.username = "test_user_name"
        self.password = "123"
        self.wrong_username = "wrong_username"
        self.wrong_password = "456"
        self.budget = 1000
        self.amount = 100
        self.big_amount = 1500
        self.small_amount = 500
        self.description = "Dog treats"
        get_connection()
        create_table()
        self.delete_test_expenses()
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

    def delete_test_expenses(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM expenses
                       WHERE user_id = (SELECT id
                       FROM users WHERE username = ?)""", (self.username,))
        connection.commit()
        connection.close()

    def test_create_budget(self):
        create_user(self.username, self.password)
        self.assertEqual(create_budget(self.username, self.budget), "Budget created successfully!")

    def test_get_budget(self):
        create_user(self.username, self.password)
        create_budget(self.budget, self.username)
        self.assertEqual(check_budget(self.username), self.budget)

    def test_add_expense(self):
        create_user(self.username, self.password)
        create_budget(self.budget, self.username)
        self.assertEqual(add_expenses(self.username, self.amount, self.description), "Expense added successfully!")

    def test_final_report_when_over_budget(self):
        create_user(self.username, self.password)
        create_budget(self.budget, self.username)
        add_expenses(self.username, self.big_amount, self.description)
        self.assertEqual(final_report(self.username), "You are 500 euros over the budget this month.")

    def test_final_report_when_no_expenses(self):
        create_user(self.username, self.password)
        create_budget(self.budget, self.username)
        self.assertEqual(final_report(self.username), "You have yet to add any expenses.")

    def test_final_report_when_expenses_under_budget(self):
        create_user(self.username, self.password)
        create_budget(self.budget, self.username)
        add_expenses(self.username, self.small_amount, self.description)
        self.assertEqual(final_report(self.username), "You have saved 500 euros so far this month.")

    def test_past_expenses(self):
        self.test_add_expense()
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        self.assertEqual(past_expenses(self.username), [(self.amount, 'Dog treats', date)])
