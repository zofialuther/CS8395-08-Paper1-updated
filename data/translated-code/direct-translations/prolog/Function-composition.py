from lambda import *

def compose(F, G):
    return lambda x: G(F(x))