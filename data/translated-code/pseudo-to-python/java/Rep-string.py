def main(aArgs):
    tests = ["1001110011", "1110111011", "0010010010", "1010101010", "1111111111", "0100101101", "0100100", "101", "11", "00", "1"]
    print("The longest rep-strings are:")
    for test in tests:
        repeats = repString(test)
        if len(repeats) == 0:
            result = "Not a rep-string"
        else:
            result = repeats[-1]
        print(test + " -> " + result)

def repString(aText):
    repetitions = []
    for length in range(1, len(aText) // 2 + 1):
        possible = aText[:length]
        quotient = len(aText) // length
        remainder = len(aText) % length
        candidate = possible * quotient + possible[:remainder]
        if candidate == aText:
            repetitions.append(possible)
    return repetitions