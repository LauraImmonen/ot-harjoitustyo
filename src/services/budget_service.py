from database.queries import get_budget, add_budget, get_user_id, add_expense
from database.queries import current_month_expenses, get_user_expenses

def check_budget(username):
    budget = get_budget(username)
    return budget

def create_budget(budget, username):
    if budget == "":
        raise ValueError("Budget cannot be empty!")
    try:
        budget = float(budget)
    except ValueError as exc:
        raise ValueError("Budget must be a number!") from exc
    if budget <= 0:
        raise ValueError("Budget cannot be 0 or below!")

    add_budget(budget, username)
    return "Budget created successfully!"

def add_expenses(username, amount, description):
    if amount == "":
        raise ValueError("Amount cannot be empty!")
    try:
        amount = float(amount)
    except ValueError as exc:
        raise ValueError("Amount must be a number!") from exc
    #AI generated
    if any(char.isdigit() for char in description):
    #AI generated code ends
        raise ValueError("Description must be a word (no numbers allowed)!")
    if amount <= 0:
        raise ValueError("Amount cannot be 0 or below!")

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
