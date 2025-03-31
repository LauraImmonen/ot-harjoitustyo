from tkinter import Tk
from ui.welcome_page import WelcomePage

def main():
    window = Tk()
    window.title("Budgeting Application")
    window.geometry("800x500")

    ui_view = WelcomePage(window)

    window.mainloop()


if __name__ == "__main__":
    main()