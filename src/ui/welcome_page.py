import tkinter as tk
from ui.login_page import LoginPage
from ui.create_account_page import CreateAccountPage

#I made all the functions and ChatGPT helped me make it into a class that I will use as a reference
#to how to do the rest of the classes for my ui-files

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Budgeting App")
        self.root.geometry("1000x800")

        self.styles = {
            "bg": "#333333",
            "fg": "pink",
        }

        self.font_large = ("Arial", 30)
        self.font_small = ("Arial", 20)

        self.frame = tk.Frame(self.root, bg=self.styles["bg"])
        self.frame.pack(fill="both", expand=True)

        self._initialize_ui()

    def _initialize_ui(self):
        welcome_label = tk.Label(
            self.frame,
            text="Welcome to the Budgeting App!",
            font=self.font_large,
            **self.styles
        )
        welcome_label.pack(pady=20)

        question_label = tk.Label(
            self.frame,
            text="Do you already have an account?",
            font=self.font_small,
            **self.styles
        )
        question_label.pack(pady=20)

        yes_button = tk.Button(
            self.frame,
            text="Yes",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            width=40,
            command=self.redirect_to_login
        )
        yes_button.pack(pady=15)

        no_button = tk.Button(
            self.frame,
            text="No",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            width=40,
            command=self.redirect_to_create_account
        )
        no_button.pack(pady=10)

    def redirect_to_login(self):
        self._switch_view(LoginPage)

    def redirect_to_create_account(self):
        self._switch_view(CreateAccountPage)

    def _switch_view(self, new_view):
        self.frame.destroy()
        new_view(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()
