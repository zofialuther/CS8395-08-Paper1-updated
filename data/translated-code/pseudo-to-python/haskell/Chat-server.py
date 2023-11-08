```python
import threading

mlck = threading.Lock()
nCons = 0
cons = set()

def main():
    global mlck, nCons, cons
    while True:
        with mlck:
            if nCons <= 0:
                break
        f = open(":12321","na")
        handle_client(f)
        with mlck:
            if nCons <= 0:
                close(f)

def handle_client(f):
    global mlck, nCons, cons
    with mlck:
        nCons += 1

    def create_thread():
        nonlocal f
        nonlocal cons
        select(f, 1000)
        writes(f, "Name? ")
        nick = read(f).split('\t')[0]
        with mlck:
            cons.add(f)
            for s in read(f):
                for c in cons:
                    if c != f:
                        write(c, nick + ": " + s)
            cons.remove(f)
        with mlck:
            nCons -= 1
```