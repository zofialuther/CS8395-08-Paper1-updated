```python
import psyco

nsolutions = 0

def search(sequences, ord_minc, curr_word, current_path, current_path_len, longest_path):
    global nsolutions
    current_path[current_path_len] = curr_word
    current_path_len += 1
    if current_path_len == len(longest_path):
        nsolutions += 1
    elif current_path_len > len(longest_path):
        nsolutions = 1
        longest_path = current_path[:current_path_len]
    last_char_index = ord(curr_word[-1]) - ord_minc
    if last_char_index >= 0 and last_char_index < len(sequences):
        for pair in sequences[last_char_index]:
            if not pair[1]:
                pair[1] = True
                search(sequences, ord_minc, pair[0], current_path, current_path_len, longest_path)
                pair[1] = False

def find_longest_chain(words):
    ord_minc = ord(min(words, key=lambda x: x[0]))
    ord_maxc = ord(max(words, key=lambda x: x[0]))
    sequences = [[] for _ in range(ord_maxc - ord_minc + 1)]
    for word in words:
        sequences[ord(word[0]) - ord_minc].append([word, False])
    current_path = [None] * len(words)
    longest_path = []
    for seq in sequences:
        for pair in seq:
            pair[1] = True
            search(sequences, ord_minc, pair[0], current_path, 0, longest_path)
            pair[1] = False
    return longest_path

def main():
    global nsolutions
    pokemon = sorted(list(set("pokemon")))
    sol = find_longest_chain(pokemon)
    print("Maximum path length:", len(sol))
    print("Paths of that length:", nsolutions)
    print("Example path of that length:")
    for i in range(0, len(sol), 7):
        print(' '.join(sol[i:i+7]))

psyco.full()
main()
```