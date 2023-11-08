```python
import random

class BestShuffle:
    
    def shuffle(self, word):
        return ''.join(random.sample(word, len(word)))
    
    def count(self, word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2))
    
    def bestShuffle(self, word):
        shuffled_word = self.shuffle(word)
        max_count = self.count(word, shuffled_word)
        for i in range(len(word)):
            for j in range(i+1, len(word)):
                new_word = list(shuffled_word)
                new_word[i], new_word[j] = new_word[j], new_word[i]
                new_word = ''.join(new_word)
                new_count = self.count(word, new_word)
                if new_count > max_count:
                    max_count = new_count
                    shuffled_word = new_word
        return shuffled_word

if __name__ == "__main__":
    words = ["hello", "world", "python"]
    bs = BestShuffle()
    for word in words:
        print(bs.bestShuffle(word))
```