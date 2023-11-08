#!/usr/bin/env python
from __future__ import print_function
import string
lets = string.ascii_lowercase
key = {x:y for (x,y) in zip(lets[13:]+lets[:13], lets)}
key.update({x.upper():key[x].upper() for x in key.keys()})
encode = lambda x: ''.join((key.get(c,c) for c in x))
if __name__ == '__main__':
    import fileinput
    for line in fileinput.input():
        print(encode(line), end="")