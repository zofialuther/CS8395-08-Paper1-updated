```python
class DetermineUniqueCharacters:
    def main(self):
        words = ["hello", "world", "python", "java"]
        for word in words:
            seen_chars = set()
            repeated_chars = {}
            for i, char in enumerate(word):
                if char in seen_chars:
                    if char not in repeated_chars:
                        repeated_chars[char] = [i]
                    else:
                        repeated_chars[char].append(i)
                else:
                    seen_chars.add(char)
            if len(repeated_chars) > 0:
                for char, positions in repeated_chars.items():
                    print(f"{word} contains repeated character {char}, hexadecimal value: {hex(ord(char))}, at positions {positions}")
            else:
                print(f"{word} has all unique characters")

DetermineUniqueCharacters().main()
```