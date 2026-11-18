import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello! You clicked the Tkinter button.")

# Main window
window = tk.Tk()
window.title("Tkinter Hello World - [Your Name]")
window.geometry("350x200")

# Label
label = tk.Label(window, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Button
button = tk.Button(window, text="Click Me", command=show_message)
button.pack()

# Run
window.mainloop()