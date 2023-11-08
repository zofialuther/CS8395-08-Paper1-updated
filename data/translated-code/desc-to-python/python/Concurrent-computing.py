import concurrent.futures

def print_word(word):
    print(word)

words = ['Enjoy', 'Rosetta', 'Code']

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(print_word, words)