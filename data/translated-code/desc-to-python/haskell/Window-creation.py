from hgl import *

def main():
    win = HGL.createWindow("Rosetta Code task: Creating a window", 300, 200)
    win.draw("text 100 100 Hello World")
    win.waitForKey()
    win.close()

if __name__ == "__main__":
    main()