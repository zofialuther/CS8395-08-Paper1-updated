def isSelfDescribing(a):
    s = str(a)
    for i in range(len(s)):
        s0 = s[i]
        b = int(s0)
        count = 0
        for j in range(len(s)):
            temp = int(s[j])
            if temp == i:
                count = count + 1
            if count > b:
                return False
        if count != b:
            return False
    return True

def main(args):
    for i in range(100000000):
        if isSelfDescribing(i):
            print(i)