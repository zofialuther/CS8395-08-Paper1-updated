import tkinter as tk

window = tk.Tk()
window.title("Goodbye")
window.geometry("250x100")

text = tk.Label(window, text="Goodbye, World !")
text.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()