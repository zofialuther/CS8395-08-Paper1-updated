from Graphics.HGL import *

def aWindow(w):
    drawInWindow(w, Text(100, 100, "Hello World"))

aWindow(runGraphics(withWindow_("Rosetta Code task: Creating a window", (300, 200), aWindow)))

getKey()