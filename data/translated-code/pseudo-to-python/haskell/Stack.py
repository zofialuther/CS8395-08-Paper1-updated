from typing import TypeVar, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Stack:
    items: List[T]

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.empty():
            raise Exception("Stack empty")
        else:
            return self.items.pop()

    def empty(self) -> bool:
        return len(self.items) == 0

    def peek(self) -> T:
        if self.empty():
            raise Exception("Stack empty")
        else:
            return self.items[-1]