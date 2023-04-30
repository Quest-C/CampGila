import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
from styles import COLOR_THEME, TTK_THEME
from views import AboutFrame, DeleteFrame, CreateFrame, UpdateFrame, PaymentFrame, SearchFrame, CampersFrame, AssignmentFrame

class MainPage:

    # Define settings upon initialization
    def __init__(self, master):
        # we usually define
        self.master = master
        self.master.geometry("1200x800")
        self.master.title("Gila Breath Camp Master Application")

        self.page = ttk.Frame(self.master)
        self.page.pack()
        self.create_page()
        self.show_about()

    def create_page(self):
        self.navigation_bar()
        self.about_frame = AboutFrame(self.master)
        self.delete_frame = DeleteFrame(self.master)
        self.create_frame = CreateFrame(self.master)
        self.update_frame = UpdateFrame(self.master)
        self.payment_frame = PaymentFrame(self.master)
        self.search_frame = SearchFrame(self.master)
        self.campers_frame = CampersFrame(self.master)
        self.assignment_frame = AssignmentFrame(self.master)

    def navigation_bar(self):
        # apply the ttk style
        self.style = ttk.Style(self.master)
        self.style.configure("nav.TFrame", background=TTK_THEME['nav.TFrame']['background'])

        # top Navigation bar:
        self.topFrame = ttk.Frame(self.master, style="nav.TFrame")
        self.topFrame.pack(side="top", fill=tk.X)

        # Navigation bar
        # Header label text:
        tk.Label(self.topFrame, text="  ", font="Bahnschrift 10", bg=COLOR_THEME['main'], fg=COLOR_THEME['text'],
                 height=2, padx=20).pack(side="right")

        # Navbar button:
        tk.Button(self.topFrame, text='Home', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_about,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Add', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  bd=0, padx=20,
                  command=self.show_create).pack(side="left")

        tk.Button(self.topFrame, text='Update', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_update,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Remove', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_delete,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Payment', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_payment,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Camper Lookup', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_campers,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Assignment', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_assignment,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Payment Records', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.show_search,
                  bd=0, padx=20).pack(side="left")

        tk.Button(self.topFrame, text='Sign out', font="Bahnschrift 10", fg=COLOR_THEME['text'],
                  bg=COLOR_THEME['main'], activebackground=COLOR_THEME['light'],
                  command=self.signout,
                  bd=0, padx=20).pack(side="left")

    def show_create(self):
        self.create_frame.pack()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_update(self):
        self.update_frame.pack()
        self.create_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_payment(self):
        self.payment_frame.pack()
        self.create_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_search(self):
        self.search_frame.pack()
        self.create_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_delete(self):
        self.delete_frame.pack()
        self.about_frame.pack_forget()
        self.create_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_about(self):
        self.about_frame.pack()
        self.delete_frame.pack_forget()
        self.create_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def show_assignment(self):
        self.assignment_frame.pack()
        self.create_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.campers_frame.pack_forget()

    def show_campers(self):
        self.campers_frame.pack()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.create_frame.pack_forget()
        self.update_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.search_frame.pack_forget()
        self.assignment_frame.pack_forget()

    def signout(self):
        quit()

if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
