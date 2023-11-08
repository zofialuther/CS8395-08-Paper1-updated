```python
import tkinter as tk
import random

class GUI_Interaction:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rosetta Code")

        self.input_label = tk.Label(self.root, text="Input:")
        self.input_entry = tk.Entry(self.root, width=10)
        self.increment_button = tk.Button(self.root, text="Increment", command=self.increment)
        self.random_button = tk.Button(self.root, text="Random", command=self.my_random)

        self.input_label.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)
        self.increment_button.grid(row=1, column=0)
        self.random_button.grid(row=1, column=1)

    def gui_component(self):
        self.root.mainloop()

    def increment(self):
        current_value = int(self.input_entry.get())
        self.input_entry.delete(0, 'end')
        self.input_entry.insert(0, str(current_value + 1))

    def my_random(self):
        self.input_entry.delete(0, 'end')
        self.input_entry.insert(0, str(random.randint(1, 100)))

    def input(self, e):
        if not e.isdigit():
            self.input_entry.delete(0, 'end')
            self.input_entry.focus_set()

gui = GUI_Interaction()
gui.gui_component()
```