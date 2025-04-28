import tkinter as tk
from tkinter import *
from services.budget_service import check_budget, final_report, add_expenses, past_expenses
from ui.session import get_current_user, clear_current_user

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1000x800")

        self.styles = {
            "bg": "#333333",
            "fg": "pink",
        }

        self.font_large = ("Arial", 30)
        self.font_small = ("Arial", 20)

        self.frame = tk.Frame(self.root, bg=self.styles["bg"])
        self.frame.pack(fill="both", expand=False)

        #AI generated code starts
        self.message_label = tk.Label(self.frame, text="", font=self.font_small, bg=self.styles["bg"], fg=self.styles["bg"])
        self.message_label.pack(fill="x", pady=20)

        self.bottom_frame = tk.Frame(self.root, bg=self.styles["bg"])
        self.bottom_frame.pack(fill="both", expand=True)
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.config(height=400)
        #AI generated code stops

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
                font=self.font_small,
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
            create_budget_button.pack(pady=20)

        final_report_label = tk.Label(
            self.frame,
            text="Final report:",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            font=self.font_small
        )
        final_report_label.pack(pady=10, anchor=tk.W)

        self.final_report_numbers_label = tk.Label(
            self.frame,
                text=final_report(get_current_user()),
                font=self.font_small,
                **self.styles
            )
        self.final_report_numbers_label.pack(pady=10, anchor=tk.W)

        #AI generated
        inputs_frame = tk.Frame(self.frame, bg=self.styles["bg"])
        inputs_frame.pack(pady=20, anchor="w")
        #AI generated code ends

        expenses_label = tk.Label(
            inputs_frame,
            text="New expense:",
            font=self.font_small,
            fg=self.styles["bg"],
            bg=self.styles["fg"]
        )
        expenses_label.grid(row=2, column=0, padx=5, pady=10, sticky="w")

        amount_label = tk.Label(
            inputs_frame,
            text="Amount:",
            font=self.font_small,
            **self.styles
        )
        amount_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.expenses_entry = tk.Entry(inputs_frame)
        self.expenses_entry.grid(row=3, column=1, padx=5, pady=5)

        description_label = tk.Label(
            inputs_frame,
            text="Description:",
            font=self.font_small,
            **self.styles
        )
        description_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.expense_description_entry = tk.Entry(inputs_frame)
        self.expense_description_entry.grid(row=3, column=3, padx=5, pady=5)

        expense_button = tk.Button(
            inputs_frame,
            text="Add expense",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            command=self.add_expense_command
        )
        expense_button.grid(row=3, column=4, padx=5, pady=5)

        past_expenses_label = tk.Label(
            self.frame,
            text="Past expenses this month:",
            fg=self.styles["bg"],
            bg=self.styles["fg"],
            font=self.font_small
        )
        past_expenses_label.pack(pady=10, anchor=tk.W)

        self.show_expenses()

    def show_expenses(self):
#AI generated code starts
        if hasattr(self, "scroll_area"):
            self.scroll_area.destroy()

        self.scroll_area = tk.Frame(self.bottom_frame, bg=self.styles["bg"])
        self.scroll_area.pack(fill="both", expand=True, pady=10)

        canvas = tk.Canvas(self.scroll_area, bg=self.styles["bg"], highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.scroll_area, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.expenses_frame = tk.Frame(canvas, bg=self.styles["bg"])
        canvas.create_window((0, 0), window=self.expenses_frame, anchor="nw")

        self.expenses_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.expense_labels = []

        expenses = past_expenses(get_current_user())

        if not expenses:
            label = tk.Label(
                self.expenses_frame,
                text="No expenses have been added",
                fg=self.styles["fg"],
                bg=self.styles["bg"],
                font=self.font_small
            )
            label.pack(pady=10, anchor="w")
            self.expense_labels.append(label)
        else:
            for amount, description, date in expenses:
                label = tk.Label(
                    self.expenses_frame,
                    text=f"- {amount} € on: {description}",
                    font=self.font_small,
                    **self.styles
                )
                label.pack(pady=5, anchor="w")
                self.expense_labels.append(label)


    def show_message(self, message, color="pink"):
        self.message_label.config(text=message, bg=color)
        self.root.after(1400, lambda: self.message_label.config(text=""))
    #AI generated code stops

    def redirect_to_create_budget_page(self):
        from ui.create_budget_page import CreateBudgetPage
        self.frame.destroy()
        self.bottom_frame.destroy()
        CreateBudgetPage(self.root)

    def add_expense_command(self):
        expense = float(self.expenses_entry.get())
        description = self.expense_description_entry.get()
        message = add_expenses(get_current_user(), expense, description)
        self.show_message(message)

#AI generated code starts
        self.expenses_entry.delete(0, tk.END)
        self.expense_description_entry.delete(0, tk.END)

        self.final_report_numbers_label.config(text=final_report(get_current_user()))
        self.show_expenses()

    def logout(self):
        clear_current_user()
        self.frame.destroy()
        self.bottom_frame.destroy()
        from ui.login_page import LoginPage
        LoginPage(self.root)
#AI generated code ends

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
