from tkinter import Tk, Label, Entry, Button
import random

def increment(input_field):
    val = int(input_field.get())
    val += 1
    input_field.delete(0, 'end')
    input_field.insert(0, str(val))

def my_random(input_field):
    window = Tk()
    window.title("GUI Interaction")
    Label(window, text="Confirm your choice !").pack()
    Button(window, text="OK", command=lambda: send_random(input_field)).pack()
    Button(window, text="Cancel", command=window.destroy).pack()
    window.mainloop()

def send_random(input_field):
    x = random.randint(0, 10000)
    input_field.delete(0, 'end')
    input_field.insert(0, str(x))

def input(gui_interaction, increment_btn, input_field, selection):
    try:
        val = int(selection)
        increment_btn.focus_set()
    except ValueError:
        print("Please type a number!")
        input_field.delete(0, 'end')

window = Tk()
window.title("Rosetta Code")

input_field = Entry(window)
input_field.grid(row=0, column=1)
Label(window, text="Value :").grid(row=0, column=0)

increment_btn = Button(window, text="Increment", command=lambda: increment(input_field))
increment_btn.grid(row=1, column=0)

random_btn = Button(window, text="Random", command=lambda: my_random(input_field))
random_btn.grid(row=1, column=1)

window.mainloop()