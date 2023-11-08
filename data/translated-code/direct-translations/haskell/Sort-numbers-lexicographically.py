from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    value: int

    def __repr__(self):
        return str(self.value)

def main():
    items = [Item(i) for i in range(1, 14)]
    sorted_items = sorted(items, key=lambda x: str(x))
    print(sorted_items)

if __name__ == "__main__":
    main()