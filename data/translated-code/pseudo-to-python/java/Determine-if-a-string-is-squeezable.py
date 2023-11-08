def main():
    testStrings = ["hello", "goodbye"]
    testChar = ["l", "o"]
    for testNum in range(len(testStrings)):
        s = testStrings[testNum]
        for c in testChar[testNum]:
            result = squeeze(s, c)
            print(result)

def squeeze(inStr, include):
    sb = []
    for i in range(len(inStr)):
        if i == 0 or inStr[i-1] != inStr[i] or (inStr[i-1] == inStr[i] and inStr[i] != include):
            sb.append(inStr[i])
    return ''.join(sb)

main()