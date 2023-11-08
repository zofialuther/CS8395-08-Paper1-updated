def vanEck(firstIndex, lastIndex):
    vanEckMap = {}
    last = 0
    if firstIndex == 1:
        print("VanEck[1] = 0")
    for n in range(2, lastIndex + 1):
        if last in vanEckMap:
            vanEck = n - vanEckMap[last]
        else:
            vanEck = 0
        vanEckMap[last] = n
        last = vanEck
        if n >= firstIndex:
            print("VanEck[" + str(n) + "] = " + str(vanEck))

def main():
    print("First 10 terms of Van Eck's sequence:")
    vanEck(1, 10)
    print("")
    print("Terms 991 to 1000 of Van Eck's sequence:")
    vanEck(991, 1000)

main()