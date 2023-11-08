```python
import tkinter as tk
import functools

def on_click(counter, label):
    counter.set(counter.get() + 1)
    label.config(text="Number of clicks: " + str(counter.get()))

def main():
    root = tk.Tk()
    root.title("Click Counter")

    counter = tk.IntVar()
    counter.set(0)

    label = tk.Label(root, text="Number of clicks: 0")
    label.pack()

    button = tk.Button(root, text="Click me", command=functools.partial(on_click, counter, label))
    button.pack()

    root.mainloop()

main()
```