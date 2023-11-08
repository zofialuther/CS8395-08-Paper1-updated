def stripcomment(A, B):
    return stripcomment_helper(A, B, 'a')

def stripcomment_helper(A, B, state):
    if A:
        if state == 'a':
            if A[0] != ';' and A[0] != '#' and A[0] != 10 and A[0] != 13:
                return stripcomment_helper(A[1:], B + [A[0]], 'a')
            elif (A[0] == ';' or A[0] == '#') and A[0] != 10 and A[0] != 13:
                return stripcomment_helper(A[1:], B, 'b')
            else:
                return stripcomment_helper(A[1:], B, 'a')
        elif state == 'b':
            if A[0] != 10 and A[0] != 13:
                return stripcomment_helper(A[1:], B, 'b')
            else:
                return stripcomment_helper(A[1:], B, 'a')
    else:
        return B

def start():
    In = "apples, pears ; and bananas\napples, pears # and bananas"
    Out = stripcomment(In, [])
    print(Out)

start()