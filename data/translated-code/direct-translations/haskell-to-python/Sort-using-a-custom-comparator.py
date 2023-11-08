from dataclasses import dataclass
from typing import List
import operator

def lengthThenAZ(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0 if s1.lower() < s2.lower() else 1 if s1.lower() > s2.lower() else 0

def descLengthThenAZ(s1: str, s2: str) -> int:
    return lengthThenAZ(s2, s1)

def main() -> None:
    strings = [ "Here", "are", "some", "sample", "strings", "to", "be", "sorted" ]
    sorted_strings_lengthThenAZ = sorted(strings, key=operator.cmp_to_key(lengthThenAZ))
    sorted_strings_descLengthThenAZ = sorted(strings, key=operator.cmp_to_key(descLengthThenAZ))
    print('\n'.join(sorted_strings_lengthThenAZ))
    print('\n'.join(sorted_strings_descLengthThenAZ))

if __name__ == "__main__":
    main()