import os

def hInteract(f, hIn, hOut):
    content = hIn.read()
    hOut.write(f(content))

def processByTemp(f, name):
    with open(name, 'r') as hIn:
        tmp = name + "$"
        with open(tmp, 'w') as hOut:
            f(hIn, hOut)
    os.remove(name)
    os.rename(tmp, name)

def process(f, names):
    if not names:
        f(sys.stdin, sys.stdout)
    else:
        for name in names:
            processByTemp(f, name)