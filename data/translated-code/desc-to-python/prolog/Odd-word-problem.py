def extract_every_other_word(input_line):
    words = input_line.split()
    result = extract_words(words[1:], 1, '')
    print(result)

def extract_words(words, index, result):
    if len(words) == 0:
        return result
    elif index % 2 == 0:
        return extract_words(words[1:], index+1, result)
    else:
        return extract_words(words[1:], index+1, result + ' ' + words[0])