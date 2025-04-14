import tkinter as tk
from ui.login_page import LoginPage
from services.account_service import create_user

#I used the welcome_page as a reference while making this code

class CreateAccountPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("900x600")

        self.styles = {
            "bg": "#333333",
            "fg": "pink",
        }

        self.font_large = ("Arial", 30)
        self.font_small = ("Arial", 20)

        self.frame = tk.Frame(self.root, bg=self.styles["bg"])
        self.frame.pack(fill="both", expand=True)

       #made by ChatGBT
        self.message_label = tk.Label(self.frame, text="", font=self.font_small, bg=self.styles["bg"], fg=self.styles["bg"])
        self.message_label.pack(fill="x", pady=20)
        #AI generated code ends

        self._initialize_ui()

    def _initialize_ui(self):
        create_account_label = tk.Label(
            self.frame,
            text="Create account:",
            font=self.font_large,
            **self.styles
        )
        create_account_label.pack(pady=10)

        username_label = tk.Label(
            self.frame,
            text="Username:",
            font=self.font_small,
            **self.styles
        )
        username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(
            self.frame,
            text="Password:",
            font=self.font_small,
            **self.styles
        )
        password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.frame)
        self.password_entry.pack(pady=5)

        create_account_button = tk.Button(
            self.frame,
            text="Create account",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            command=self.create_account
        )
        create_account_button.pack(pady=10)

        welcome_page_button = tk.Button(
            self.frame,
            text="Back to welcome page",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            command=self.redirect_to_welcome_page
        )
        welcome_page_button.pack(pady=20)

    #made by ChatGPT, modified by me
    def show_message(self, message, color="pink"):
        self.message_label.config(text=message, bg=color)
        self.root.after(1400, lambda: self.message_label.config(text=""))
     #AI generated code ends

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        message = create_user(username, password)

        if message == "Username already exists! Please choose another username.":
            self.show_message(message)
        elif message == "Account created successfully!":
            self.show_message(message)
            self.root.after(1400, self.redirect_to_login)

    def redirect_to_login(self):
        self.frame.destroy()
        LoginPage(self.root)

    def redirect_to_welcome_page(self):
        from ui.welcome_page import WelcomePage
        self.frame.destroy()
        WelcomePage(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = CreateAccountPage(root)
    root.mainloop()
