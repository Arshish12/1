import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

title_label = tk.Label(root, text="Basic Calculator", font=("Arial", 14, "bold"))
title_label.pack()

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 18), justify='right')
entry.pack(fill='x', padx=10, pady=5)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for button in row:
        btn = tk.Button(row_frame, text=button, font=("Arial", 14), width=5, height=2)
        btn.pack(side='left', padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
