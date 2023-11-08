def runLengths(s):
    result = []
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            result.append((s[i], count))
            count = 1
    result.append((s[-1], count))
    return result

def showLengths(encoded):
    for char, count in encoded:
        print(f'{char}{count}', end=' ')
    print()

def main():
    test_string = "aaabbc"
    encoded_result = runLengths(test_string)
    showLengths(encoded_result)
    if ''.join([char*count for char, count in encoded_result]) == test_string:
        print("Encoding validated")
    else:
        print("Encoding not validated")

main()