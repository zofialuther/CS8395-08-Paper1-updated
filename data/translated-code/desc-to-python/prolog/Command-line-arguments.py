import sys
from pyswip import Prolog

prolog = Prolog()
args = sys.argv
for arg in args:
    print(arg)