```python
from tkinter import *

D = Tk()
D.title('Goodbye')
D.geometry('250x100')

S = StringVar()
S.set('Goodbye, World !')
T = Label(D, textvariable=S)
T.pack()

F = T['font']
M = F.measure(S.get())
XT = (250 - M) / 2

H = F.metrics('linespace')
YT = (100 - H) / 2

T.place(x=XT, y=YT)

D.mainloop()
```