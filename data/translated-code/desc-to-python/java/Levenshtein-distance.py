```python
class Levenshtein:
    def distance(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2+1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    def main(self, strings):
        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                print(f"Distance between {strings[i]} and {strings[j]} is {self.distance(strings[i], strings[j])}")

# Example usage
levenshtein = Levenshtein()
strings = ["kitten", "sitting", "sunday", "saturday"]
levenshtein.main(strings)
```