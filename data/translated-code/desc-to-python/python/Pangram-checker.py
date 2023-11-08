import sys

def ispangram(sentence, alphabet):
    return set(alphabet) <= set(sentence.lower())

if sys.version_info[0] < 3:
    input_func = raw_input
else:
    input_func = input

user_sentence = input_func("Enter a sentence: ")
result = ispangram(user_sentence, 'abcdefghijklmnopqrstuvwxyz')
print(result)