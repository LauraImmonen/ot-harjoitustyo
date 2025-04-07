import tkinter as tk
from services.budget_service import check_budget
from ui.session import get_current_user, clear_current_user

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x500")

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
        username = get_current_user()
        budget = check_budget(username)

        Logout_button = tk.Button(
            self.frame,
            text="Logout",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            command=self.logout
        )
        Logout_button.pack(anchor="ne", padx=10, pady=10)

        if budget > 0:
            budget_label = tk.Label(
                self.frame,
                text=f"Your monthly budget is: {budget} €",
                font=self.font_large,
                **self.styles
            )
            budget_label.pack(pady=10)
        else:
            create_budget_button = tk.Button(
                self.frame,
                text="Create your monthly budget",
                fg=self.styles["bg"],
                bg=self.styles["fg"],
                command=self.redirect_to_create_budget_page
            )
            create_budget_button.pack(pady=30)


    def redirect_to_create_budget_page(self):
        from ui.create_budget_page import CreateBudgetPage
        self.frame.destroy()
        CreateBudgetPage(self.root)

#Made by ChatGPT
    def logout(self):
        clear_current_user()
        self.frame.destroy()
        from ui.login_page import LoginPage
        LoginPage(self.root)
#AI generated code ends

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()


