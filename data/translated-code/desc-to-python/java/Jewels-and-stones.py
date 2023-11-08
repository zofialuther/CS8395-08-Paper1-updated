```python
class App:
    def countJewels(self, stones, jewels):
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count

if __name__ == "__main__":
    app = App()
    stones1 = "abac"
    jewels1 = "a"
    print(app.countJewels(stones1, jewels1))  # Output: 2

    stones2 = "abcdefg"
    jewels2 = "xyz"
    print(app.countJewels(stones2, jewels2))  # Output: 0
```