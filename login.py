import tkinter as tk
from tkinter import ttk, messagebox
from mainpage import MainPage
from db import Database

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x180")
        self.master.title("Gila Breath Camp Login")

        # tk variable
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = ttk.Frame(self.master)
        self.page.pack()

        ttk.Label(self.page).grid(row= 0, column = 0) #take the empty space
        # username
        ttk.Label(self.page, text = 'Username: ').grid(row =1, column = 1)
        ttk.Entry(self.page, textvariable = self.username).grid(row=1, column = 2)

        ttk.Label(self.page).grid(row=2, column=0)  # take the empty space

        # password
        ttk.Label(self.page, text='Password: ').grid(row=3, column=1)
        ttk.Entry(self.page, textvariable=self.password, show = "*").grid(row=3, column=2)

        # buttons
        ttk.Button(self.page, text = "Login", command = self.verify_login).grid(row=4, column= 1, pady = 20)
        ttk.Button(self.page, text = "Exit", command = self.master.destroy).grid(row = 4, column = 2, pady = 20)

    def verify_login(self):
        db = Database()
        if db.verify_login_from_database(self.username.get(), self.password.get()):
            tk.messagebox.showinfo(title="Successful", message="Login Successful")
            self.page.destroy()
            MainPage(root)
        else:
            tk.messagebox.showwarning(title="Alert", message="Login Failure. \nPlease try again")


if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
