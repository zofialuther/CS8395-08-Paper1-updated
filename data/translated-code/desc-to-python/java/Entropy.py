def getShannonEntropy(input_string):
    char_count = {}
    entropy = 0
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    total_chars = len(input_string)
    for count in char_count.values():
        probability = count / total_chars
        entropy -= probability * log2(probability)
    return entropy

def log2(x):
    return math.log(x, 2)

def main():
    test_strings = ["hello", "world", "entropy", "shannon"]
    for string in test_strings:
        print(f"The Shannon entropy of '{string}' is {getShannonEntropy(string)}")

main()