from tkinter import Tk, Label, Button

click = []

def btnclick(Label):
    V = click[0]
    click.clear()
    V1 = V + 1
    click.append(V1)
    A = '{} click(s)'.format(V1)
    Label.config(text=A)

def simple_windowed():
    click.clear()
    click.append(0)
    root = Tk()
    root.title('Simple windowed application')
    name = Label(root, text='There have been no clicks yet')
    name.pack()
    button = Button(root, text='Click me !', command=lambda: btnclick(name))
    button.pack()
    root.mainloop()

simple_windowed()