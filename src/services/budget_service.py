from database.queries import get_budget, add_budget

def check_budget(username):
    budget = get_budget(username)
    return budget

def create_budget(budget, username):
    add_budget(budget, username)
    return "Budget created successfully!"