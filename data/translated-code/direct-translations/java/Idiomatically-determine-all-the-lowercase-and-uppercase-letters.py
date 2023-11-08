from typing import Iterator

class Letters:
    def main(self, args: Iterator[str]) -> None:
        print("Upper case: ", end="")
        for n in range(0, 0x10FFFF):
            if n.isupper():
                print(chr(n), end="")
        print("...")

        print("Lower case: ", end="")
        for n in range(0, 0x10FFFF):
            if n.islower():
                print(chr(n), end="")
        print("...")