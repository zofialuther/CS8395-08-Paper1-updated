def day(n, name):
    return (n, name)

def gift(n, description):
    return (n, description)

def giftsFor(n, lst):
    if n == 0:
        return []
    else:
        return [gift(n, description)] + giftsFor(n-1, lst)

def writeln(s):
    print(s)

def writeList(lst):
    for item in lst:
        writeln(item)
    writeln('')

def writeGifts(n):
    nth_day = day(n, n)
    writeln(f"On the {nth_day} day of Christmas, my true love sent to me:")
    gift_list = giftsFor(n, [])
    writeList(gift_list)

def writeLoop(n):
    for i in range(n, 0, -1):
        day = 13 - i
        writeGifts(day)

def main():
    writeLoop(12)

main()