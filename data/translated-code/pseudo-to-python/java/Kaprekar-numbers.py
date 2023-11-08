def splitAt(str, idx):
    ans = ["", ""]
    ans[0] = str[:idx]
    if ans[0] == "":
        ans[0] = "0"
    ans[1] = str[idx:]
    return ans

def main(args):
    count = 0
    base = int(args[0]) if len(args) > 0 else 10
    for i in range(1, 1000001):
        sqrStr = str(i * i)
        for j in range(len(sqrStr) // 2 + 1):
            parts = splitAt(sqrStr, j)
            firstNum = int(parts[0], base)
            secNum = int(parts[1], base)
            if secNum == 0:
                break
            if firstNum + secNum == i:
                print(str(i) + "\t" + str(i) + "\t" + sqrStr + "\t" + parts[0] + " + " + parts[1])
                count += 1
                break
    print(str(count) + " Kaprekar numbers < 1000000 (base 10) in base " + str(base))