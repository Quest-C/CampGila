import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
from db import Database
from styles import COLOR_THEME, TTK_THEME

class AboutFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text="About Page", font=('Bahnschrift',16)).pack()
        ttk.Label(self).pack()
        ttk.Label(self, text='About Product: Created by Tkinter').pack()
        ttk.Label(self, text='Authors: Quest Crotty, Tess Studdiford, Anders Ortlieb').pack()
        ttk.Label(self, text='Project: ITM 360 Midterm').pack()
        ttk.Label(self, text='Version: v1.0.0').pack()

class DeleteFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text="Remove Camper", font=('Bahnschrift',16)).pack()
        ttk.Label(self).pack()
        #ttk.Label(self, text="For future development").pack()

        self.email = tk.StringVar()
        self.create_page()


    def create_page(self):
        self.payment = ttk.Frame(self)
        self.payment.pack()

        ttk.Label(self.payment, text="Email Address: ", font=("Calibri 12")).grid(row=0, column=0, pady=10, sticky=tk.W)
        ttk.Entry(self.payment, textvariable=self.email, width=30).grid(row=0, column=1, pady=10, sticky=tk.W)
        ttk.Button(self, text="Submit", command=self.delete_camper).pack(pady=10, anchor=tk.E)

    def delete_camper(self):
        db = Database()
        values = (self.email.get())
        if self.email.get() == "":
            tk.messagebox.showerror('Warning!',
                                    "Please enter a camper's email!")
        else:
            status = db.delete_one_record('campers', 'email', self.email.get())
            if status == False:
                tk.messagebox.showerror('Error!',
                                        "This email address doesn't exist!")
            else:
                tk.messagebox.showinfo('Success!',
                                       "Camper was removed from database.")
            self.email.set("")

class CreateFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text="Add Camper", font=('Bahnschrift', 16)).pack()
        ttk.Label(self).pack()

        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.gender = tk.StringVar()
        self.mobile = tk.StringVar()
        self.address = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.zipcode = tk.StringVar()
        self.email = tk.StringVar()

        self.create_page()
        ttk.Button(self, text='Submit', command=self.create_camper).pack(side="right", pady=10, padx=5,
                                                                                anchor=tk.E)
        ttk.Button(self, text='Clear', command=self.clear_create_data).pack(side="right", pady=10, padx=5, anchor=tk.E)

    def create_page(self):
        self.info = ttk.Frame(self)
        self.info.pack()

        # first row
        ttk.Label(self.info, text='First Name(*): ', font=("Calibri 12")).grid(row=0, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.fname, width=20).grid(row=0, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=0, column=2)

        ttk.Label(self.info, text='Last Name(*): ', font=("Calibri 12")).grid(row=0, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.lname, width=20).grid(row=0, column=4, pady=5, sticky=tk.W)

        # Second Row
        # gender menu list
        ttk.Label(self.info, text='Gender(*): ', font=("Calibri 12")).grid(row=1, column=0, pady=5, sticky=tk.W)
        menu_list = ['', 'Female', 'Male']

        self.gender.set(menu_list[0])
        field_drop = ttk.OptionMenu(self.info, self.gender, *menu_list)
        field_drop.config(width=15)
        field_drop.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=1, column=2)

        ttk.Label(self.info, text='Date of Birth: ', font=("Calibri 12")).grid(row=1, column=3, pady=5, sticky=tk.W)
        # self.dob entry!
        self.dob = DateEntry(self.info, width=20, date_pattern='yyyy-mm-dd',
                             bg="darkblue", fg="white",
                             year=date.today().year)
        self.dob.delete(0, "end")
        self.dob.grid(row=1, column=4, sticky=tk.W)

        # Thrid Row
        ttk.Label(self.info, text='Email(*)', font=("Calibri 12")).grid(row=2, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.email, width=20).grid(row=2, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=2, column=2)

        ttk.Label(self.info, text='Mobile(*)', font=("Calibri 12")).grid(row=2, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.mobile, width=20).grid(row=2, column=4, pady=5, sticky=tk.W)

        # Fourth Row
        ttk.Label(self.info, text='Address', font=("Calibri 12")).grid(row=3, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.address, width=20).grid(row=3, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=3, column=2)

        ttk.Label(self.info, text='City ', font=("Calibri 12")).grid(row=3, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.city, width=20).grid(row=3, column=4, pady=5, sticky=tk.W)

        # Fifth Row
        ttk.Label(self.info, text='State: ', font=("Calibri 12")).grid(row=4, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.state, width=20).grid(row=4, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=4, column=2)

        ttk.Label(self.info, text='Zipcode', font=("Calibri 12")).grid(row=4, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.zipcode, width=20).grid(row=4, column=4, pady=5, sticky=tk.W)

    def create_camper(self):
        db = Database()
        today = str(date.today())
        required_values = [self.fname.get(), self.lname.get(), self.gender.get(),
                            self.mobile.get(), self.email.get()]
        values = (self.fname.get(), self.lname.get(), self.gender.get(),
                  self.dob.get(), self.mobile.get(), self.address.get(),
                  self.city.get(), self.state.get(), self.zipcode.get(),
                  self.email.get(), today)

        if '' in required_values:
            tk.messagebox.showerror('Warning!',
                                    "Please complete all the required information")
        else:
            status = db.insert_one_record("campers", values)
            if status == False:
                tk.messagebox.showerror('Error!',
                                        "This email address is already registered")
                self.clear_create_data()
            else:
                tk.messagebox.showinfo('Successful!',
                                    "The camper has been successfully registered")
                self.clear_create_data()

    def clear_create_data(self):
        self.fname.set('')
        self.fname.set('')
        self.lname.set('')
        self.gender.set('')
        self.dob.delete(0, "end")
        self.mobile.set('')
        self.address.set('')
        self.city.set('')
        self.state.set('')
        self.zipcode.set('')
        self.email.set('')

class UpdateFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text='Update Page', font=("Bahnschrift", 16)).pack()
        ttk.Label(self).pack()

        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.gender = tk.StringVar()
        self.mobile = tk.StringVar()
        self.address = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.zipcode = tk.StringVar()
        self.email = tk.StringVar()

        self.create_page()

    def create_page(self):
        # Search By Frame
        self.search_by_frame = ttk.LabelFrame(self, text='Search Profile By Email')
        self.search_by_frame.pack(pady=5, expand=True)

        ttk.Entry(self.search_by_frame, textvariable=self.email, width=30).grid(row=0, column=1, padx=5)
        ttk.Button(self.search_by_frame, text="Search", command=self.show_camper_data).grid(row=0, column=2, pady=10)

        # Show Camper Frame
        self.info = ttk.LabelFrame(self, text='Camper Profile')
        self.info.pack(pady=5, expand=True)

        # first row
        ttk.Label(self.info, text='First Name(*): ', font=("Calibri 12")).grid(row=0, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.fname, width=20).grid(row=0, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=0, column=2)

        ttk.Label(self.info, text='Last Name(*): ', font=("Calibri 12")).grid(row=0, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.lname, width=20).grid(row=0, column=4, pady=5, sticky=tk.W)

        # Second Row
        # gender menu list
        ttk.Label(self.info, text='Gender(*): ', font=("Calibri 12")).grid(row=1, column=0, pady=5, sticky=tk.W)
        menu_list = ['', 'Female', 'Male']

        self.gender.set(menu_list[0])
        field_drop = ttk.OptionMenu(self.info, self.gender, *menu_list)
        field_drop.config(width=15)
        field_drop.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=1, column=2)

        ttk.Label(self.info, text='Date of Birth: ', font=("Calibri 12")).grid(row=1, column=3, pady=5, sticky=tk.W)
        # self.dob entry!
        self.dob = DateEntry(self.info, width=20, date_pattern='yyyy-mm-dd',
                             bg="darkblue", fg="white",
                             year=date.today().year)
        self.dob.delete(0, "end")
        self.dob.grid(row=1, column=4, sticky=tk.W)

        # Thrid Row
        ttk.Label(self.info, text='Email(*)', state='disabled', font=("Calibri 12")).grid(row=2, column=0, pady=5,
                                                                                          sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.email, state='disabled', width=20).grid(row=2, column=1, pady=5,
                                                                                       sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=2, column=2)

        ttk.Label(self.info, text='Mobile(*)', font=("Calibri 12")).grid(row=2, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.mobile, width=20).grid(row=2, column=4, pady=5, sticky=tk.W)

        # Fourth Row
        ttk.Label(self.info, text='Address', font=("Calibri 12")).grid(row=3, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.address, width=20).grid(row=3, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=3, column=2)

        ttk.Label(self.info, text='City ', font=("Calibri 12")).grid(row=3, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.city, width=20).grid(row=3, column=4, pady=5, sticky=tk.W)

        # Fifth Row
        ttk.Label(self.info, text='State: ', font=("Calibri 12")).grid(row=4, column=0, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.state, width=20).grid(row=4, column=1, pady=5, sticky=tk.W)

        ttk.Label(self.info, width=5).grid(row=4, column=2)

        ttk.Label(self.info, text='Zipcode', font=("Calibri 12")).grid(row=4, column=3, pady=5, sticky=tk.W)
        ttk.Entry(self.info, textvariable=self.zipcode, width=20).grid(row=4, column=4, pady=5, sticky=tk.W)

        ttk.Button(self.info, text='Clear', command=self.clear_camper_data).grid(row=5, column=3, sticky=tk.W)
        ttk.Button(self.info, text='Submit', command=self.update_camper_data).grid(row=5, column=4, sticky=tk.W)

    def show_camper_data(self):
        db = Database()
        conditions = f"email = '{self.email.get()}'"
        result = db.query_table_with_condition("campers", "*", conditions)
        print(result)
        if len(result) == 0:
            tk.messagebox.showerror('Warning!',
                                    "This email address doesn't exist!")
        else:
            self.fname.set(result[0][0])
            self.lname.set(result[0][1])
            self.gender.set(result[0][2])
            if len(result[0][3]) != 0:
                self.dob.set_date(result[0][3])
            self.mobile.set(result[0][4])
            self.address.set(result[0][5])
            self.city.set(result[0][6])
            self.state.set(result[0][7])
            self.zipcode.set(result[0][8])

    def clear_camper_data(self):
        self.fname.set("")
        self.lname.set("")
        self.gender.set("")
        self.dob.delete(0, "end")
        self.mobile.set("")
        self.address.set("")
        self.city.set("")
        self.state.set("")
        self.zipcode.set("")
        self.email.set("")

    def update_camper_data(self):
        db = Database()

        if self.email.get() == '':
            tk.messagebox.showerror('Warning!',
                                    "This email address doesn't exist!")

        else:
            flag = db.update_camper_data(self.fname.get(), self.lname.get(), self.gender.get(),
                                            self.dob.get(), self.mobile.get(), self.address.get(),
                                            self.city.get(), self.state.get(), self.zipcode.get(),
                                            self.email.get())
            if flag == False:
                tk.messagebox.showerror('Warning!',
                                        "This email address doesn't exist!")
            else:
                tk.messagebox.showinfo('Success!',
                                       "The camper's profile has been successfully updated")
            self.clear_camper_data()

class PaymentFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text='Payment Page', font=("Bahnschrift", 16)).pack()
        ttk.Label(self).pack()

        self.type = tk.StringVar()
        self.email = tk.StringVar()
        self.p_amount = tk.StringVar()
        self.transaction_id = tk.StringVar()
        self.create_page()

    def create_page(self):
        self.payment = ttk.Frame(self)
        self.payment.pack()

        ttk.Label(self.payment, text='Payment Type: ', font=("Calibri 12")).grid(row=0, column=0, pady=10, sticky=tk.W)
        menu_list = ['', 'Pay', 'Refund']

        self.type.set(menu_list[0])
        field_drop = ttk.OptionMenu(self.payment, self.type, *menu_list, command=self.handle_payment_type)
        field_drop.config(width=15)
        field_drop.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(self.payment, text="Email Address: ", font=("Calibri 12")).grid(row=1, column=0, pady=10, sticky=tk.W)
        self.email_entry=ttk.Entry(self.payment, textvariable=self.email, width=30, state='disabled')
        self.email_entry.grid(row=1, column=1, pady=10, sticky=tk.W)

        ttk.Label(self.payment, text="Payment Amount: ", font=("Calibri 12")).grid(row=2, column=0, pady=10, sticky=tk.W)
        self.pay_entry=ttk.Entry(self.payment, textvariable=self.p_amount, width=30, state='disabled')
        self.pay_entry.grid(row=2, column=1, pady=10, sticky=tk.W)

        ttk.Label(self.payment, text="Transaction ID: ", font=("Calibri 12")).grid(row=3, column=0, pady=10, sticky=tk.W)
        self.id_entry=tk.Entry(self.payment, textvariable=self.transaction_id, width=30, state='disabled')
        self.id_entry.grid(row=3, column=1, pady=10, sticky=tk.W)

        ttk.Label(self.payment, text="Payment Date: ", font=("Calibri 12")).grid(row=4, column=0, pady=10, sticky=tk.W)
        self.p_date = DateEntry(self.payment, width=20, date_pattern='yyyy-mm-dd',
                                bg="darkblue", fg="white", year=date.today().year, state='disabled')
        self.p_date.grid(row=4, column=1, sticky=tk.W)

        ttk.Button(self, text="Submit", command=self.check_type).pack(pady=10, anchor=tk.E)

    def disable_all(self):
        self.transaction_id.set("")
        self.email_entry.configure(state='normal')
        self.pay_entry.configure(state='normal')
        self.id_entry.configure(state='disabled')
        self.p_date.configure(state='normal')

    def handle_payment_type(self, type):
        if type == "Pay":
            self.transaction_id.set("")
            self.email_entry.configure(state='normal')
            self.pay_entry.configure(state='normal')
            self.id_entry.configure(state='disabled')
            self.p_date.configure(state='normal')
        else:
            self.email.set("")
            self.p_amount.set("")
            self.email_entry.configure(state='disabled')
            self.pay_entry.configure(state='disabled')
            self.id_entry.configure(state='normal')
            self.p_date.configure(state='disabled')

    def check_type(self):
        if self.type.get() == "Pay":
            return self.create_payment_data()
        elif self.type.get() == "Refund":
            return self.refund_payment()
        else:
            tk.messagebox.showerror('Warning!',
                                    "Please select a payment type.")

    def create_payment_data(self):
        db = Database()
        values = (self.email.get(), self.p_date.get(), self.p_amount.get())
        if "" in values:
            tk.messagebox.showerror('Warning!',
                                    "Please complete all the required information")
        else:
            status = db.insert_one_record("payments(email, payment_date, payment_amount)", values)

            if status == False:
                tk.messagebox.showerror('Error!',
                                        "This email address doesn't exist!")
            else:
                transaction_id=db.get_last_payment()
                tk.messagebox.showinfo('Success!',
                                       f"Your transaction ID is {transaction_id}")

            self.email.set("")
            self.p_amount.set("")
            self.transaction_id.set("")

    def refund_payment(self):
        db = Database()
        if self.transaction_id == "":
            tk.messagebox.showerror('Warning!',
                                    "Please enter a transaction ID")
        else:
            status = db.delete_one_record('payments', 'transaction_id', self.transaction_id.get())

            if status == False:
                tk.messagebox.showerror('Error!',
                                        "This transaction ID doesn't exist!")
            else:
                tk.messagebox.showinfo('Success!',
                                       "The refund is processed!")
            self.email.set("")
            self.p_amount.set("")
            self.transaction_id.set("")

class SearchFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self).pack()
        ttk.Label(self, text='Search Page', font=("Bahnschrift", 16)).pack()
        ttk.Label(self).pack()

        self.create_page()
        ttk.Button(self, text="Refresh", command=self.show_payment_data).pack(pady=5, anchor=tk.E)

    def create_page(self):
        # Search By Frame
        self.search_by_frame = ttk.LabelFrame(self, text='Search By')
        self.search_by_frame.pack(pady=5, expand=True)

        # contain the treeview!
        self.table_by_frame = ttk.Frame(self)
        self.table_by_frame.pack()

        menu_list = ['', 'email', 'payment_date', 'payment_amount', 'transaction_id']

        oMenuWidth = len(max(menu_list, key=len))

        self.clicked = tk.StringVar()
        self.clicked.set(menu_list[0])

        field_drop = ttk.OptionMenu(self.search_by_frame, self.clicked, *menu_list)
        field_drop.config(width=oMenuWidth)
        field_drop.grid(row=0, column=0)

        self.field_value = ttk.Entry(self.search_by_frame, width=30)
        self.field_value.grid(row=0, column=1)

        ttk.Button(self.search_by_frame, text="Search", command=self.show_payment_data).grid(row=0, column=2)

        # Table view - to display the search result
        columns = ("Transaction_id", 'Email', "Payment Date", "Payment Amount")
        self.tree_view = ttk.Treeview(self.table_by_frame, show='headings',
                                      selectmode='browse', columns=columns)

        self.tree_view.column("Transaction_id", width=100, anchor='center')
        self.tree_view.heading("Transaction_id", text="Transaction ID")

        for item in columns[1:]:
            self.tree_view.column(item, width=130, anchor='center')
            self.tree_view.heading(item, text=item)

        self.tree_view.pack(side="left", fill=tk.BOTH, expand=True)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.table_by_frame, orient=tk.VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill='y')

    def show_payment_data(self):
        # delete the old records!
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass

        db = Database()

        field = self.clicked.get()
        field_value = self.field_value.get()

        if len(field_value) == 0:
            records = db.query_table("payments", "*")
            print(records)
            index = 0
            for record in records[::-1]:
                rowid = record[0]
                email = record[1]
                p_date = record[2]
                p_amount = record[3]
                self.tree_view.insert("", index + 1, values=(rowid, email, p_date, p_amount))

        else:
            conditions = f"{field} = '{field_value}'"
            results = db.query_table_with_condition("payments", "*", conditions)
            if results == False:
                tk.messagebox.showerror('Warning!',
                                        "This record doesn't exist!")
            else:
                index = 0
                for record in results[::-1]:
                    rowid = record[0]
                    email = record[1]
                    p_date = record[2]
                    p_amount = record[3]
                    print(record)
                    self.tree_view.insert("", index + 1, values=(rowid, email, p_date, p_amount))

