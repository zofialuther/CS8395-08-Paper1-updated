from tkinter import *

click = 0

def btnclick(label):
    global click
    click += 1
    label.config(text=str(click) + " click(s)")

def simple_windowed():
    global click
    click = 0
    
    root = Tk()
    root.title("Simple windowed application")
    
    name = Label(root, text="There have been no clicks yet")
    name.place(x=40, y=20, width=200, height=18)
    
    btn_click = Button(root, text="Click me !", command=lambda: btnclick(name))
    btn_click.place(x=90, y=60, width=80, height=24)
    
    root.mainloop()

simple_windowed()