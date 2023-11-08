```python
class CharHandler:
    def handle(self, word):
        pass

class ForwardHandler(CharHandler):
    def handle(self, word):
        return word

class ReverseHandler(CharHandler):
    def handle(self, word):
        return word[::-1]

import threading

class Reverser(threading.Thread):
    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        reversed_word = self.word[::-1]
        print(f"Reversed word: {reversed_word}")

if __name__ == "__main__":
    while True:
        user_input = input("Enter a word: ")
        handler = ForwardHandler()
        processed_word = handler.handle(user_input)
        print(f"Processed word: {processed_word}")
        
        reverser = Reverser(user_input)
        reverser.start()
```