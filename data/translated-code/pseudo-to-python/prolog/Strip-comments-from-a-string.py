def stripcomment(A, B):
    stripcomment(A, B, 'a')

def stripcomment(AL, BL, a):
    if (A != ';' and A != '#' and A != 10 and A != 13):
        stripcomment(AL, BL, a)

def stripcomment(AL, BL, a):
    if ((A == ';;' or A == '#') and A != 10 and A != 13):
        stripcomment(AL, BL, 'b')

def stripcomment(AL, BL, b):
    if (A != 10 and A != 13):
        stripcomment(AL, BL, 'b')

def stripcomment(AL, BL, _M):
    if (A == 10 or A == 13):
        stripcomment(AL, BL, 'a')

def stripcomment([], [], _M):
    pass

def start():
    In = "apples, pears ; and bananas\napples, pears # and bananas"
    stripcomment(In, Out)
    print(Out)