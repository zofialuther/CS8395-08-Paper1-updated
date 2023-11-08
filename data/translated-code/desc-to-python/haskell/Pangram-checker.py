def pangram(input_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    input_string = input_string.lower()
    return not bool(set(alphabet) - set(input_string))

def main():
    sample_input = "The quick brown fox jumps over the lazy dog"
    result = pangram(sample_input)
    print(result)

main()