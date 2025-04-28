from database.queries import get_budget, add_budget, get_user_id, add_expense
from database.queries import current_month_expenses, get_user_expenses

def check_budget(username):
    budget = get_budget(username)
    return budget

def create_budget(budget, username):
    add_budget(budget, username)
    return "Budget created successfully!"

def add_expenses(username, amount, description):
    user_id = get_user_id(username)
    add_expense(user_id, amount, description)
    return "Expense added successfully!"

def past_expenses(username):
    user_id = get_user_id(username)
    return get_user_expenses(user_id)

def final_report(username):
    user_id = get_user_id(username)

    expenses = current_month_expenses(user_id)
    budget = get_budget(username)

    if expenses == 0:
        return "You have yet to add any expenses."
    if expenses < budget:
        return f"You have saved {budget-expenses} euros so far this month."
    return f"You are {abs(budget-expenses)} euros over the budget this month."
