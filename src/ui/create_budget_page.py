import tkinter as tk
from ui.session import get_current_user
from services.budget_service import create_budget

class CreateBudgetPage:
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

       #made by ChatGBT
        self.message_label = tk.Label(self.frame, text="", font=self.font_small, bg=self.styles["bg"], fg=self.styles["bg"])
        self.message_label.pack(fill="x", pady=20)
        #AI generated code ends

        self._initialize_ui()

    def _initialize_ui(self):
        create_budget = tk.Label(
            self.frame,
            text="Create your monthly budget:",
            font=self.font_large,
            **self.styles
        )
        create_budget.pack(pady=10)

        budget_label = tk.Label(
            self.frame,
            text="Monthly amount you are allowed to spend (euros):",
            font=self.font_small,
            **self.styles
        )
        budget_label.pack(pady=5)

        self.budget_entry = tk.Entry(self.frame)
        self.budget_entry.pack(pady=5)

        create_budget_button = tk.Button(
            self.frame,
            text="Create budget",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            command=self.create_budget
        )
        create_budget_button.pack(pady=10)

    #made by ChatGPT, modified by me
    def show_message(self, message, color="pink"):
        self.message_label.config(text=message, bg=color)
        self.root.after(1400, lambda: self.message_label.config(text=""))
     #AI generated code ends

    def create_budget(self):
        budget = self.budget_entry.get()
        username = get_current_user()

        message = create_budget(budget, username)

        if message == "Budget created successfully!":
            self.show_message(message)
            self.root.after(1400, self.redirect_to_home_page)

    def redirect_to_home_page(self):
        from ui.home_page import HomePage
        self.frame.destroy()
        HomePage(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = CreateBudgetPage(root)
    root.mainloop()
