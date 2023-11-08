def halfAdder(b, a):
    return (b and a, b != a)

def fullAdder(c, a, b):
    halfAdder1 = halfAdder(b, a)
    halfAdder2 = halfAdder(c, halfAdder1[0])
    result = (halfAdder2[0] or halfAdder1[1], halfAdder2[1])
    return result

def adder4(as):
    def helper(cy, fab):
        f, a, b = fab
        return f(cy, a, b)
    
    return mapAccumR(lambda cy, fab: helper(cy, fab), 0, zip(replicate(4, fullAdder), as))