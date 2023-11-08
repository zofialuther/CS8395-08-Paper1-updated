from Data.Modular import *

def f(x: ModularInteger(13)) -> ModularInteger(13):
    x = x.value
    result = (x**100 + x + 1) % 13
    return ModularInteger(13)(result)

def main() -> None:
    print(f(ModularInteger(13)(10)))