from Data.List import *
from Control.Monad import *
from Control.Arrow import *

def leaptext(x, b):
    if b:
        return str(x) + " is a leap year"
    else:
        return str(x) + " is not a leap year"

def isleapsf(j):
    if 0 == j % 100:
        return 0 == j % 400
    else:
        return 0 == j % 4