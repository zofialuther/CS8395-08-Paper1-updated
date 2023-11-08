```python
def count_same_position_chars(word1, word2):
    count = 0
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            count += 1
    return count

def best_shuffle(word):
    import itertools
    best_count = 0
    best_shuffle = word
    for perm in itertools.permutations(word):
        new_word = ''.join(perm)
        count = count_same_position_chars(word, new_word)
        if count > best_count:
            best_count = count
            best_shuffle = new_word
    return best_shuffle

words = ['hello', 'python', 'world']
for word in words:
    shuffled_word = best_shuffle(word)
    print(f"Original word: {word}, Shuffled word: {shuffled_word}, Same position count: {count_same_position_chars(word, shuffled_word)}")
```