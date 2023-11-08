def main():
    num = "1"
    
    for i in range(1, 11):
        print(num)
        num = lookandsay(num)

def lookandsay(s):
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1
    return result

if __name__ == "__main__":
    main()