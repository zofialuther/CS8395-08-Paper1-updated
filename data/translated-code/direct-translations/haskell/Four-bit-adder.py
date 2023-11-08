def band(x, y):
    return x and y

def xor(x, y):
    return x != y

def uncurry(func):
    return lambda args: func(*args)

halfAdder = uncurry(band) and uncurry(xor)

def fullAdder(c, a, b):
    return (lambda cy_s: (bor(cy_s[0])(halfAdder(b, cy_s[1])), halfAdder(c, a)))(halfAdder(c, a))

def adder4(as):
    return mapAccumR(lambda cy, f_a_b: f_a_b[0](cy, f_a_b[1], f_a_b[2]), 0, zip3(replicate(4, fullAdder), as))