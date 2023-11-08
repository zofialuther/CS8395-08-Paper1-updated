import Control.Exception as C

def check(x, y):
    try:
        x // y
        return False
    except:
        return True