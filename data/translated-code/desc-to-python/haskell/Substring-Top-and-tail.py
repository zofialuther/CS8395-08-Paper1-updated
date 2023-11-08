def remFirst(s):
    if len(s) > 1:
        return s[1:]
    else:
        return ""

def remLast(s):
    if len(s) > 1:
        return s[:-1]
    else:
        return ""

def remBoth(s):
    if len(s) > 2:
        return s[1:-1]
    else:
        return ""

def main():
    input_string = "Some string"
    print(remFirst(input_string))
    print(remLast(input_string))
    print(remBoth(input_string))

main()