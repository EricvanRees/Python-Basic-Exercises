"""
Write a Python program to create a Tkinter-based login form with input fields for userid and password.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

window = tk.Tk()
window.geometry('600x400')
window.title('login')
window.configure(background='#1d2d44')

# window grid
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# create a style
styles = ttk.Style()
styles.theme_use('clam')
styles.configure(window, background='#1d2d44',
                 foreground='white', fieldbackground='black')
styles.configure('TButton', background='#005f73')
styles.map('TButton', background=[('active', '#0a9396')])

# add frame
frame = ttk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(0, weight=3)

# title
label = ttk.Label(frame, text='Login', font=('Arial', 20))
label.grid(row=0, column=0, columnspan=2)

# user
user_label = ttk.Label(frame, text="UserID: ")
user_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

user_text_box = ttk.Entry(frame)
user_text_box.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(frame, text="Password: ")
password_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_text_box = ttk.Entry(frame, show='*')
password_text_box.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# button
login_button = ttk.Button(frame, text='Send')
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


def validate(event):
    userID = user_text_box.get()
    password = password_text_box.get()
    if userID == 'root' and password == 'admin':
        showinfo(title='Login', message='Correct data')
    else:
        showerror(title='Login', message="Incorrect data")


# associate events with login button
login_button.bind('<Return>', validate)  # press enter
login_button.bind('<Button-1>', validate)  # left mouse click

frame.grid(row=0, column=0)

window.mainloop()
