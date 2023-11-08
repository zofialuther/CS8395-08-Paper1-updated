```python
class Sound:
    def __init__(self, trigger, onomatopoeia):
        self.trigger = trigger
        self.onomatopoeia = onomatopoeia

    def generate_onomatopoeia(self, number):
        if number % self.trigger == 0:
            return self.onomatopoeia
        else:
            return str(number)

sounds = [Sound(3, "Fizz"), Sound(5, "Buzz")]

def main():
    for i in range(1, 21):
        result = ""
        for sound in sounds:
            result += sound.generate_onomatopoeia(i)
        print(result)

if __name__ == "__main__":
    main()
```