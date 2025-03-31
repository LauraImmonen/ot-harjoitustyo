from database.queries import user_exists, make_account, login_by_username


def create_user(username, password):
    if user_exists(username):
        return "Username already exists! Please choose another username."
    make_account(username, password)
    return "Account created successfully!"

#I used ChatGPt to help me make this
def validate_login(username, password):
    user = login_by_username(username)

    if user is None:
        return "Username not found!"
    elif user[0] != password:
        return "Incorrect password!"
    else:
        return "Logged in successfully!"
#AI generated code stops


