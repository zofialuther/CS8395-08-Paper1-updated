```python
def main():
    with open('135-0.txt', 'r') as file:
        text = file.read()
        words = text.split()
        words = [word.lower() for word in words]
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        print_top_words(sorted_words[:10])

def print_top_words(words):
    print("Word\tCount")
    for word, count in words:
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
```