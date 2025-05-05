from database.queries import user_exists, make_account, login_by_username

def create_user(username, password):
    if username == "":
        raise ValueError("Username cannot be empty!")
    if password == "":
        raise ValueError("Password cannot be empty!")
    if user_exists(username):
        return "Username already exists! Please choose another username."
    make_account(username, password)
    return "Account created successfully!"

#AI generated code starts
def validate_login(username, password):
    user = login_by_username(username)

    if user is None:
        return "Username not found!"
    if user[0] != password:
        return "Incorrect password!"
    return "Logged in successfully!"
#AI generated code stops
