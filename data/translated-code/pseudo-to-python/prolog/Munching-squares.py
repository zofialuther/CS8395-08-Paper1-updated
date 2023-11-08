from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

# Create a new window called 'XOR Pattern'
window = tk.Tk()
window.title('XOR Pattern')

# Set the size of the window to 512x512
window.geometry('512x512')

# Create a new image called 'Img' with width 512, height 512, and kind pixmap
img = Image.new('RGB', (512, 512))

# For each value I in the range 0 to 511
for i in range(512):
    # For each value J in the range 0 to 511
    for j in range(512):
        # Calculate V as the result of I xor J
        v = i ^ j
        # Calculate R as (V * 1024) mod 65536
        r = (v * 1024) % 65536
        # Calculate G as (65536 - V * 1024) mod 65536
        g = (65536 - v * 1024) % 65536
        # If V mod 2 is 0 then calculate B as (V * 4096) mod 65536, else calculate B as (65536 - (V * 4096)) mod 65536
        if v % 2 == 0:
            b = (v * 4096) % 65536
        else:
            b = (65536 - (v * 4096)) % 65536
        # Set the pixel at position (I, J) in Img to the color with RGB values (R, G, B)
        img.putpixel((i, j), (r, g, b))

# Create a new bitmap 'Bmp' using Img
bmp = ImageTk.PhotoImage(img)

# Display Bmp at the position (0,0) in the window
label = tk.Label(window, image=bmp)
label.place(x=0, y=0)

# Open the window
window.mainloop()