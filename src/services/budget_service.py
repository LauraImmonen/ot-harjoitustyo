from database.queries import get_budget, add_budget, get_user_id, add_expense
from database.queries import current_month_expenses
from ui.session import get_current_user

def check_budget(username):
    budget = get_budget(username)
    return budget

def create_budget(budget, username):
    add_budget(budget, username)
    return "Budget created successfully!"

def add_expenses(amount, description):
    username = get_current_user()
    user_id = get_user_id(username)
    add_expense(user_id, amount, description)
    return "Expense added successfully!"

def final_report(username):
    username = get_current_user()
    user_id = get_user_id(username)

    expenses = current_month_expenses(user_id)
    budget = get_budget(username)

    if expenses < budget:
        return f"You have saved {budget-expenses} euros so far this month."
    if expenses == 0:
        return "You have yet to add any expenses."
    return f"You are {budget-expenses} euros over the budget this month."
