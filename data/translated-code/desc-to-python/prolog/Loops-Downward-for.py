def rfor(high, low):
    if high >= low:
        print(high)
        rfor(high-1, low)

def reverse_iter():
    high = 10
    low = 0
    while True:
        rfor(high, low)
        high -= 1
        if high < low:
            break