```python
class AmbTask:
    @staticmethod
    def Amb(words):
        def amb(remaining, chain):
            if not remaining:
                return chain
            else:
                last_word = chain[-1]
                for word in remaining:
                    if last_word[-1] == word[0]:
                        result = amb([w for w in remaining if w != word], chain + [word])
                        if result:
                            return result
                return None
        
        result = amb(words, [words[0]])
        if result:
            print(result)
        else:
            print("No match found")

words = [["apple", "elephant", "tiger", "rabbit"], ["hello", "orange", "egg", "elephant"]]
AmbTask.Amb(words)
```