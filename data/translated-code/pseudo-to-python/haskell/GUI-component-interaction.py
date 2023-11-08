from tkinter import *

def main():
    frm = Frame(text="Interact")
    fld = Entry(text="0", on=checkKeys)
    inc = Button(text="increment", on_command=lambda: increment(fld))
    ran = Button(text="random", on_command=lambda: randReplace(fld, frm))
    frm.layout(margin=5, floatCentre=True, column=2).centre_widget(fld).row(2, inc, ran)
    return start(frm)

def increment(field):
    val = field.get_text()
    if val is not None:
        field.set_text(str(1 + int(val)))

def checkKeys(EventKey):
    if EventKey.show() in ["Backspace", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return propagateEvent

def randReplace(field, frame):
    answer = confirmDialog(frame, "Random", "Generate a random number?", True)
    if answer:
        num = getStdRandom(randomR(1, 100))
        field.set_text(str(num))