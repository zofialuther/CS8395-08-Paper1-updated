def sampleFunction():
    print("a")

def main():
    replicateM_(5, sampleFunction)

def replicateM_(n, func):
    for _ in range(n):
        func()