import Control.Monad

def main():
    s = ""
    
    when(s == "", lambda: print("Empty."))
    when(s != "", lambda: print("Not empty."))