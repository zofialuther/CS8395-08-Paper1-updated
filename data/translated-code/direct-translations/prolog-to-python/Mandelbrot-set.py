from tkinter import Tk, Canvas

def mandelbrot():
    root = Tk()
    canvas = Canvas(root, width=700, height=650)
    canvas.pack()

    for i in range(700):
        for j in range(650):
            r, g, b = get_RGB(i, j)
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(i, j, i+1, j, fill=color)

    root.mainloop()

def get_RGB(x, y):
    cx = (x - 350) / 150
    cy = (y - 325) / 150
    iter = 570
    return compute_RGB(cx, cy, 0, 0, iter)

def compute_RGB(cx, cy, zx, zy, iter):
    while zx * zx + zy * zy < 4 and iter > 0:
        tmp = zx * zx - zy * zy + cx
        zy = 2 * zx * zy + cy
        zx = tmp
        iter -= 1

    iterF = iter | (iter << 15)
    r = iterF >> 16
    iter1 = iterF - (r << 16)
    g = iter1 >> 8
    b = iter1 - (g << 8)
    return r, g, b

mandelbrot()