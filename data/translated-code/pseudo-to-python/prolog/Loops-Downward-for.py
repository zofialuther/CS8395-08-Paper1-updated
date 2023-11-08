def rfor(Hi, Lo, Val):
    if Hi >= Lo:
        return
    else:
        Val = Hi
        Hi -= 1
        rfor(Hi, Lo, Val)

def reverse_iter():
    rfor(10, 0, Val)
    print(Val)
    reverse_iter()