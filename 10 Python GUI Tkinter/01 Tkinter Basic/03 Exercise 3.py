import tkinter as tk 

main_window = tk.Tk()
main_window.geometry("800x500")
main_window.title("My new window")
# bg color window:
main_window.configure(background='#1d2d44')
# create label
label = tk.Label(main_window, text="This is my label")
label.config(font=("Arial", 25, "bold"))
# publish label
label.pack(pady=20)

main_window.mainloop()