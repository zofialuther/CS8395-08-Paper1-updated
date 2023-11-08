```python
class Quibbler:

    @staticmethod
    def quibble(words):
        qText = "{"
        for wIndex in range(len(words)):
            qText += words[wIndex] + ("" if wIndex == len(words)-1 else
                                      " and " if wIndex == len(words)-2 else
                                      ", ")
        qText += "}"
        return qText

    @staticmethod
    def main():
        print(Quibbler.quibble([]))
        print(Quibbler.quibble(["ABC"]))
        print(Quibbler.quibble(["ABC", "DEF"]))
        print(Quibbler.quibble(["ABC", "DEF", "G"]))
        print(Quibbler.quibble(["ABC", "DEF", "G", "H"]))


Quibbler.main()
```