import functools
import tkinter as tk

def on_click(label, counter):
    counter.set(counter.get() + 1)
    label.config(text="Number of clicks: " + str(counter.get()))

def main():
    window = tk.Tk()
    window.geometry("300x200")
    
    label = tk.Label(window, text="There have been no clicks yet")
    label.pack()
    
    counter = tk.IntVar()
    
    update_counter = functools.partial(on_click, label, counter)
    
    button = tk.Button(window, text="click me", command=update_counter)
    button.pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()