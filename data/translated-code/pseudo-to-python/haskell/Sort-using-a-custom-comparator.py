def lengthThenAZ(str1, str2):
    if len(str1) == len(str2):
        return 0 if str1 < str2 else 1
    return -1 if len(str1) < len(str2) else 1

def descLengthThenAZ(str1, str2):
    if len(str1) == len(str2):
        return 0 if str1 < str2 else 1
    return -1 if len(str1) > len(str2) else 1

def main():
    strings = ["Here", "are", "some", "sample", "strings", "to", "be", "sorted"]
    sorted_strings = sorted(strings, key=lambda x: (len(x), x))
    desc_sorted_strings = sorted(strings, key=lambda x: (-len(x), x))
    print("\n".join(sorted_strings))
    print("\n".join(desc_sorted_strings))

main()