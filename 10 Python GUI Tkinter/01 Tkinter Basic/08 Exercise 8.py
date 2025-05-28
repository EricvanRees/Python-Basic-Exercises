"""
Write a Python program that creates a basic menu bar with menu items using Tkinter.

"""

import tkinter as tk

root = tk.Tk()
root.title('tkinter menu bar')
root.geometry('400x400')

my_menu = tk.Menu(root)
root.config(menu=my_menu)

# click command


def our_command():
    my_label = tk.Label(root, text="You Clicked a Dropdown Menu!").pack()


# create a menu item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an edit menu item
edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

# create an Options menu item
option_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

root.mainloop()
