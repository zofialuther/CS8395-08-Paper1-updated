class CharHandler:
    def handle(self, c):
        print(c)
        if c.isalpha():
            return fwd
        else:
            return rev

class Reverser(CharHandler):
    def __init__(self):
        self.ch = None

    def recur(self):
        # NOTIFY
        while self.ch is None:
            pass
        c = self.ch
        ret = c
        self.ch = None
        if c.isalpha():
            ret = self.recur()
            print(c)
        return ret

    def run(self):
        while True:
            print(self.recur())
            # NOTIFY

    def handle(self, c):
        while self.ch is not None:
            pass
        self.ch = c
        # NOTIFY
        while self.ch is not None:
            pass
        if c.isalpha():
            return rev
        else:
            return fwd

fwd = CharHandler()
fwd.handle = lambda c: (print(c), fwd if c.isalpha() else rev)

rev = Reverser()

def loop():
    handler = fwd
    while c != "end of input":
        c = # GET next character from input
        handler = handler.handle(c)

loop()