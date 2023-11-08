```python
class NameGame:
    def printVerse(self, name):
        # generate verse using the input name
        # follow specific format and manipulate the name into rhyming phrases
        pass

def main():
    # create a list of names
    names = ["John", "Mary", "Bob"]

    # create an instance of NameGame
    ng = NameGame()

    # use a stream to pass the list of names to the printVerse method
    for name in names:
        ng.printVerse(name)

if __name__ == "__main__":
    main()
```