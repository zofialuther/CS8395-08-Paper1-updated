import tkinter as tk
import random

def increment_counter():
    try:
        current_value = int(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(current_value + 1))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

def reset_counter():
    entry.delete(0, tk.END)
    entry.insert(0, str(random.randint(1, 100)))

root = tk.Tk()
root.title("Simple Counter App")

entry = tk.Entry(root)
entry.pack()

increment_button = tk.Button(root, text="Increment", command=increment_counter)
increment_button.pack()

random_button = tk.Button(root, text="Random", command=reset_counter)
random_button.pack()

root.mainloop()