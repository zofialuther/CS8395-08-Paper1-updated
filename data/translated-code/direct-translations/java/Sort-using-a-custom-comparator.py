from typing import List

class Test:
    @staticmethod
    def main(args: List[str]) -> None:
        strings = ["Here", "are", "some", "sample", "strings", "to", "be", "sorted"]

        strings.sort(key=lambda s: (-len(s), s.lower()))

        for s in strings:
            print(s, end=" ")