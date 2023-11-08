def countSubstring(subStr, str):
    count = 0
    index = 0
    while index < len(str):
        index = str.find(subStr, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

def main():
    testStr1 = "abababab"
    testSubStr1 = "ab"
    print(countSubstring(testSubStr1, testStr1))  # Output: 4

    testStr2 = "Hello, hello, hello"
    testSubStr2 = "hello"
    print(countSubstring(testSubStr2, testStr2))  # Output: 3

main()