from typing import Generator

def fibStream() -> Generator[int, None, None]:
    lastFib = 0
    operand = 1
    while True:
        ret = operand + lastFib
        yield ret
        lastFib = operand
        operand = ret

def fib(n):
    stream = fibStream()
    limitedStream = (next(stream) for _ in range(n))
    return list(limitedStream)[-1]