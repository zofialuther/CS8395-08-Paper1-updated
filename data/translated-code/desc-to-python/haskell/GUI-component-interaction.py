```python
import tkinter as tk
import random

def increment():
    value = int(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(value + 1))

def randReplace():
    entry.delete(0, tk.END)
    entry.insert(0, str(random.randint(1, 100)))

def checkKeys(event):
    if event.keysym.isdigit() or event.keysym == "BackSpace":
        return
    else:
        return "break"

def main():
    root = tk.Tk()
    
    entry = tk.Entry(root)
    entry.pack()
    
    button1 = tk.Button(root, text="Increment", command=increment)
    button1.pack()
    
    button2 = tk.Button(root, text="Random Replace", command=randReplace)
    button2.pack()
    
    entry.bind("<Key>", checkKeys)

    root.mainloop()

if __name__ == "__main__":
    main()
```