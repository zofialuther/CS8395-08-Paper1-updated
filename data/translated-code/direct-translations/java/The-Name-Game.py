from typing import List

def print_verse(name: str) -> None:
    x = name.capitalize()
    y = x.lower() if x[0] in "AEIOU" else x[1:]
    b = "b" + y
    f = "f" + y
    m = "m" + y
    if x[0] == 'B':
        b = y
    elif x[0] == 'F':
        f = y
    elif x[0] == 'M':
        m = y
    print(f"{x}, {x}, bo-{b}")
    print(f"Banana-fana fo-{f}")
    print(f"Fee-fi-mo-{m}")
    print(f"{x}!\n")

def main(names: List[str]) -> None:
    for name in names:
        print_verse(name)

if __name__ == "__main__":
    names = ["Gary", "Earl", "Billy", "Felix", "Mary", "Steve"]
    main(names)