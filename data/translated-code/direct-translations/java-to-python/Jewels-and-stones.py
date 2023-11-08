```python
class App:
    @staticmethod
    def countJewels(stones, jewels):
        bag = set(jewels)
        count = 0
        for c in stones:
            if c in bag:
                count += 1
        return count

    @staticmethod
    def main():
        print(App.countJewels("aAAbbbb", "aA"))
        print(App.countJewels("ZZ", "z"))

App.main()
```