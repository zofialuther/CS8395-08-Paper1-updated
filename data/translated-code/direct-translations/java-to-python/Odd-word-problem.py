```python
class OddWord:
    class CharHandler:
        def handle(self, c):
            pass

    fwd = CharHandler()
    def handle(self, c):
        print(c)
        return self.fwd if c.isalpha() else self.rev

    class Reverser(threading.Thread, CharHandler):
        def __init__(self):
            super().__init__()
            self.daemon = True
            self.start()
            self.ch = None

        def recur(self):
            self.notify()
            while self.ch is None:
                self.wait()
            c = self.ch
            ret = c
            self.ch = None
            if c.isalpha():
                ret = self.recur()
                print(c)
            return ret

        def run(self):
            try:
                while True:
                    print(self.recur())
                    self.notify()
            except Exception as e:
                pass

        def handle(self, c):
            while self.ch is not None:
                self.wait()
            self.ch = c
            self.notify()
            while self.ch is not None:
                self.wait()
            return self.fwd if c.isalpha() else self.rev

    rev = Reverser()

    def loop(self):
        handler = self.fwd
        while True:
            try:
                c = input()
                if not c:
                    break
                handler = handler.handle(c)
            except Exception as e:
                pass

    def main(self):
        self.loop()

OddWord().main()
```