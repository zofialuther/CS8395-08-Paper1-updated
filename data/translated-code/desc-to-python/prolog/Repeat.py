from typing import Callable

def repeat(func: Callable, times: int):
    for _ in range(times):
        func()

def test():
    print("Hello, World")
    print("Hello, [Name]")