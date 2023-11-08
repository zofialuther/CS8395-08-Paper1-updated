from tkinter import Tk, Canvas, PhotoImage

def xor_pattern():
    root = Tk()
    root.title('XOR Pattern')

    canvas = Canvas(root, width=512, height=512)
    canvas.pack()

    img = PhotoImage(width=512, height=512)

    for i in range(512):
        for j in range(512):
            v = i ^ j
            r = (v * 1024) % 65536
            g = (65536 - v * 1024) % 65536
            if v % 2 == 0:
                b = (v * 4096) % 65536
            else:
                b = (65536 - (v * 4096)) % 65536
            img.put("#{:04x}{:04x}{:04x}".format(r, g, b), (i, j))

    canvas.create_image(0, 0, image=img, anchor='nw')

    root.mainloop()

xor_pattern()