#!/usr/bin/python
from tkinter import *
root = Tk()
root.title("PAYxROLL SOFTWARE")
root.geometry("800x2400")

my_menu = Menu(root)
root.config(menu=my_menu)

def action_master():
    pass

master_menu = Menu(my_menu)

my_menu.add_cascade(label="Master", menu=master_menu)

master_menu.add_cascade(label="Entity Configuration", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Employee Master", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Department Master", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Location Master", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Pay and Deduct Elements Master", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Advances Schedule", command= action_master)
master_menu.add_separator()
master_menu.add_cascade(label="Salary Changes", command= action_master)

transaction_menu = Menu(my_menu)

my_menu.add_cascade(label="Transactions", menu=transaction_menu)

transaction_menu.add_cascade(label="Monthly Changes", command= action_master)
transaction_menu.add_separator()
transaction_menu.add_cascade(label="Leave Record (Annual / Sick)", command= action_master)
transaction_menu.add_separator()
transaction_menu.add_cascade(label="Leave Adjustments", command= action_master)
transaction_menu.add_separator()
transaction_menu.add_cascade(label="Leave Without Pay", command= action_master)
transaction_menu.add_separator()
transaction_menu.add_cascade(label="Leave Entitlement", command= action_master)


root.mainloop()