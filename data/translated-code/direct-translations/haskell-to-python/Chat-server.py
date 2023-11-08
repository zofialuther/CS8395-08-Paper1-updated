from threading import Lock
from select import select

mlck = Lock()
nCons = 0
cons = set()

def main():
    while True:
        with open(":12321", "na") as f:
            handle_client(f)
            with mlck:
                if nCons <= 0:
                    f.close()

def handle_client(f):
    global nCons, cons
    with mlck:
        nCons += 1
    while select([f], [], [], 1000)[0]:
        f.write("Name? ")
        nick = f.read().split('\t')[0]
        for c in cons:
            c.write(nick + " has joined.")
        cons.add(f)
        while True:
            s = f.read()
            if not s:
                break
            for c in cons:
                c.write(nick + ": " + s)
        cons.remove(f)
        for c in cons:
            c.write(nick + " has left.")
        with mlck:
            nCons -= 1