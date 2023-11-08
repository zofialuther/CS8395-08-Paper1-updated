def isSelfDescribing(a):
    s = str(a)
    for i in range(len(s)):
        s0 = s[i]
        b = int(s0)  # number of times i-th digit must occur for it to be a self describing number
        count = 0
        for j in range(len(s)):
            temp = int(s[j])
            if temp == i:
                count += 1
            if count > b:
                return False
        if count != b:
            return False
    return True

def main():
    for i in range(100000000):
        if isSelfDescribing(i):
            print(i)

main()