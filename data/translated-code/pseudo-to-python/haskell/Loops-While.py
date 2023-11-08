from functools import partial

def main():
    n = 1024
    loop(n)

def loop(n):
    if n > 0:
        print(n)
        loop(n // 2)

main()