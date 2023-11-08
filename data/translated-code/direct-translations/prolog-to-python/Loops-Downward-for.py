def rfor(Hi, Lo, Hi):
    return Hi >= Lo

def rfor(Hi, Lo, Val):
    if Hi > Lo:
        H = Hi - 1
        return rfor(H, Lo, Val)

def reverse_iter():
    Val = rfor(10, 0, Val)
    print(Val)
    reverse_iter()

reverse_iter()