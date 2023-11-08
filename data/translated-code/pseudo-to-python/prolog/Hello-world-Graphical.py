import tkinter

D = tkinter.Tk()
D.title('Goodbye')
D.geometry('250x100')

S = "Goodbye, World !"
T = tkinter.Label(D, text=S)

F = T['font']
M = tkinter.font.Font(font=F).measure(S)
XT = (250 - M)/2
H = tkinter.font.Font(font=F).metrics('linespace')
YT = (100-H)/2

T.place(x=XT, y=YT)

D.mainloop()