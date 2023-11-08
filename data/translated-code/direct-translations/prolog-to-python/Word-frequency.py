```python
def print_top_words(File, N):
    with open(File, 'r', encoding='utf-8') as f:
        String = f.read()
    
    Words = re.split(r"\w+", String)
    
    Lower = [(word.lower(), 1) for word in Words]
    Lower.sort(key=lambda x: x[0])
    
    Sorted = merge_words(Lower)
    
    Counted = sorted(Sorted.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Top {N} words:\nRank\tCount\tWord")
    print_top_words(Counted, N, 1)

def merge_words(words):
    result = {}
    for word, count in words:
        result[word] = result.get(word, 0) + count
    return result

def print_top_words(words, N, R):
    if N == 0:
        return
    print(f"{R}\t{words[N-1][1]}\t{words[N-1][0]}")
    print_top_words(words, N-1, R+1)

print_top_words("135-0.txt", 10)
```