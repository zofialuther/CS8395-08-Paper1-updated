from itertools import count

from sympy import Integer

def babbage_(B, B, Sq):
    if Integer(B * B) == Sq:
        Sq_str = str(Sq)
        if Sq_str.endswith('2696969'):
            return True
    return False

def babbage():
    for B in count(start=1):
        Square = B * B
        if babbage_(B, B, Square):
            print(f"lowest number is {B} which squared becomes {Square}")
            break

babbage()